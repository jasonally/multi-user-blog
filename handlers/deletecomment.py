import helpers
import time

from google.appengine.ext import db
from handlers.blog import BlogHandler

class DeleteCommentHandler(BlogHandler):

    def get(self, post_id, post_user_id, comment_id):
        if self.user and self.user.key().id() == int(post_user_id):
            post_key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())
            key = db.Key.from_path('Comment', int(comment_id), parent=post_key)

            c = db.get(key)
            c.delete()

            time.sleep(0.1)     # Time delay so deleted post is removed
            self.redirect('/' + post_id)
        elif not self.user:
            self.redirect('/login')
        else:
            access_error = "sorry, you don't have permission to delete this comment"
            self.render('front.html', access_error=access_error)
