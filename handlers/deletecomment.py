import helpers
import time

from google.appengine.ext import db
from handlers.blog import BlogHandler

class DeleteCommentHandler(BlogHandler):
    """Allows users to delete their own comments. Obtains the entry for the
    comment, deletes it, and redirects users back to the blog post page.
    """

    def get(self, post_id, post_user_id, comment_id):
        # The user who created the comment is the only one allowed to delete the
        # post.
        if self.user and self.user.key().id() == int(post_user_id):
            post_key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())
            key = db.Key.from_path('Comment', int(comment_id), parent=post_key)

            c = db.get(key)
            c.delete()

            time.sleep(0.1)     # Delay so deleted post is removed from front
            self.redirect('/' + post_id)
        elif not self.user:
            self.redirect('/login')
        else:
            access_error = "sorry, you don't have permission to delete this comment"
            self.render('front.html', access_error=access_error)
