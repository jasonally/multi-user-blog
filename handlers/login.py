from handlers.blog import BlogHandler
from models.user import User

class LoginHandler(BlogHandler):
    """Renders login page. If user successfully logs in, the login() method
    puts a user_id cookie on the user's device and redirects them back to the
    blog front page. Otherwise, the login page reloads with an error message.
    """

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
