from handlers.blog import BlogHandler
from models.user import User

class LoginHandler(BlogHandler):

    def get(self):
        self.render('login.html', error='')

    def post(self):
        self.username = self.request.get('username')
        self.password = self.request.get('password')

        u = User.login(self.username, self.password)

        if u:
            self.login(u)
            self.redirect('/')
        else:
            error = "invalid login"
            self.render('login.html', error=error)
