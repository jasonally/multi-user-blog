import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.comment import Comment

class PostHandler(BlogHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=helpers.blog_key())
        post = db.get(key)
        comments = db.GqlQuery(
        "SELECT * FROM Comment WHERE ancestor is :1 ORDER BY created ASC", key)
        if not post:
            self.error(404)
            return
        self.render("permalink.html", post=post, comments=comments)