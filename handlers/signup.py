import helpers

from handlers.blog import BlogHandler
from models.user import User

class SignupHandler(BlogHandler):

    def get(self):
        self.render('signup.html', username='', password='', verify='',
                    email='', username_error='', password_error='',
                    verify_error='', email_error='')

    def post(self):
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        params = dict(username=self.username, email=self.email)
        has_error = False

        if not helpers.valid_username(self.username):
            params['username_error'] = "that's not a valid username"
            has_error = True

        if not helpers.valid_password(self.password):
            params['password_error'] = "that's not a valid password"
            has_error = True

        # Only need to check self.verify if self.password is valid.
        elif self.password != self.verify:
            params['verify_error'] = "your passwords didn't match"
            has_error = True

        # Email address is optional
        if self.email:
            if not helpers.valid_email(self.email):
                params['email_error'] = "that's not a valid email address"
                has_error = True

        # **params -- The way to pass a dictionary into render as a parameter.
        # **[dictionary_name] is the notation.
        if has_error:
            self.render('signup.html', **params)
        else:
            self.done()

    def done(self):
        u = User.by_name(self.username)
        if u:
            username_error = "that username already exists"
            self.render('signup.html', username_error=username_error)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()
            self.login(u)
            self.redirect('/')
