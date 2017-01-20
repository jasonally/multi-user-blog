from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.post import Post

class BlogFrontHandler(BlogHandler):
    """Renders the front page of the blog by selecting the 20 most recent
    entries from the Post entity.
    """

    def get(self):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 20")
        self.render('front.html', user=self.user, posts=posts)
