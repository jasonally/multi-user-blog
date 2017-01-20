import helpers

from models.user import User
from webapp2 import RequestHandler

class BlogHandler(RequestHandler):
    """Contains methods that help render Jinja templates and blog posts as well
    as help with user authentication. Every other handler inherits from this
    handler.
    """

    def write(self, *a, **kwargs):
        self.response.out.write(*a, **kwargs)

    def render_str(self, template, **kwargs):
        kwargs['user'] = self.user
        return helpers.render_str(template, **kwargs)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

    def initialize(self, *a, **kwargs):
        """Runs every time a page which inherits from BlogHandler loads. If
        the user_id cookie is invalid, self.user will be False and can be used
        to prevent unauthorized access to parts of the blog.
        """
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
