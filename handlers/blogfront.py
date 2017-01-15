from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.post import Post

class BlogFrontHandler(BlogHandler):

    def get(self):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 10")
        self.render('front.html', user=self.user, posts=posts)