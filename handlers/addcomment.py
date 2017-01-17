import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.comment import Comment

class AddCommentHandler(BlogHandler):

    def render_addcomment(self, comment='', error=''):
        self.render('addcomment.html', comment=comment, error=error)

    def get(self, post_id, user_id):
        if self.user:
            self.render_addcomment()
        else:
            self.render('front.html', access_error="you must be signed in to add a comment")

    def post(self, post_id, user_id):
        comment = self.request.get('comment')
        error = "Please enter a comment."

        #key = db.Key.from_path('Post', int(post_id), parent=helpers.blog_key())

        if comment:
            c = Comment(user_id=int(user_id), comment=comment,
                        user_name = self.user.name)
            c.put()
            self.redirect('/' + post_id)
        else:
            self.render_addcomment(error=error)