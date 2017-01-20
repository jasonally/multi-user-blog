import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.comment import Comment

class PostHandler(BlogHandler):
    """Generates a specific blog post as well as its associated comments. The
    comments can be obtained by looking for the entries in the Comment entity
    whose ancestor is the key for a specific blog post.
    """

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=helpers.blog_key())
        post = db.get(key)

       # key is passed in to the query to get the associated comments.
        comments = db.GqlQuery(
        "SELECT * FROM Comment WHERE ancestor is :1 ORDER BY created ASC", key)

        if not post:
            self.error(404)
            return
        self.render('permalink.html', post=post, comments=comments)
