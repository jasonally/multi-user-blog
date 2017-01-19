import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.comment import Comment

class EditCommentHandler(BlogHandler):

    def render_editcomment(self, comment='', error=''):
        self.render('editcomment.html', comment=comment, error=error)

    def get(self, post_id, post_user_id, comment_id):
        if self.user and self.user.key().id() == int(post_user_id):
            post_key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())
            key = db.Key.from_path('Comment', int(comment_id),
                parent=post_key)
            c = db.get(key)
            self.render_editcomment(c.comment)
        elif not self.user:
            self.redirect('/login')
        else:
            access_error = "sorry, you don't have permission to edit this comment"
            self.render('front.html', access_error=access_error)

    def post(self, post_id, post_user_id, comment_id):
        if not self.user:
            return self.redirect('/login')

        if self.user and self.user.key().id() == int(post_user_id):
            comment = self.request.get('comment')

            post_key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())
            key = db.Key.from_path('Comment', int(comment_id),
                parent=post_key)

            c = db.get(key)
            c.comment = comment
            c.put()

            self.redirect('/' + post_id)

        else:
            access_error = "sorry, you don't have permission to edit this comment"
            self.render('front.html', access_error=access_error)
