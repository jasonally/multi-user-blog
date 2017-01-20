import helpers
import time

from google.appengine.ext import db
from handlers.blog import BlogHandler

class DeletePostHandler(BlogHandler):
    """Allows users to delete their own posts. Obtains the entry for the given
    post, deletes it, and redirects users back to the blog front page.
    """

    def get(self, post_id, post_user_id):
        # The user who created the post is the only one allowed to delete the
        # post.
        if self.user and self.user.key().id() == int(post_user_id):
            key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())

            p = db.get(key)
            p.delete()

            time.sleep(0.1)     # Delay so deleted comment is removed from page
            self.redirect('/')
        elif not self.user:
            self.redirect('/login')
        else:
            access_error = "sorry, you don't have permission to delete this post"
            self.render('front.html', access_error=access_error)
