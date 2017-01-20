from handlers.blog import BlogHandler

class LogoutHandler(BlogHandler):
    """Logs users out of the blog web app. The logout() method clears the
    user_id cookie on the user's device and redirects them back to the blog
    front page.
    """

    def get(self):
        self.logout()
        self.redirect('/')
