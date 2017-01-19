import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.post import Post

class DeletePostHandler(BlogHandler):

    def get(self, post_id, post_user_id):
        if self.user and self.user.key().id() == int(post_user_id):
            key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())
            p = db.get(key)
            p.delete()

            self.redirect('/')
        elif not self.user:
            self.redirect('/login')

        # If a valid user is trying to delete a post he/she didn't create,
        # re-render the post with the error message
        else:
            key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())
            post = db.get(key)
            comments = db.GqlQuery(
            "SELECT * FROM Comment WHERE ancestor is :1 ORDER BY created ASC",
                key)
            error = "sorry, you don't have permission to delete this post"
            self.render("permalink.html", post=post, comments=comments,
                error=error)