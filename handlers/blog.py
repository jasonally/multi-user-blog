import helpers

from models.user import User
from webapp2 import RequestHandler

class BlogHandler(RequestHandler):

    def write(self, *a, **kwargs):
        self.response.out.write(*a, **kwargs)

    def render_str(self, template, **kwargs):
        kwargs['user'] = self.user
        return helpers.render_str(template, **kwargs)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

    # This function runs every time a page that inherits from Handler loads
    # If the user_id cookie is invalid, the page can trigger a redirect back
    # to the login page
    def initialize(self, *a, **kwargs):
        RequestHandler.initialize(self, *a, **kwargs)
        user_id = self.read_secure_cookie('user_id')
        self.user = user_id and User.by_id(int(user_id))

    def set_secure_cookie(self, name, val):
        cookie_val = helpers.make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie', '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and helpers.check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')