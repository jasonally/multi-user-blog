import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.comment import Comment

class AddCommentHandler(BlogHandler):
    """Handler for adding comments to blog posts. Only users who are logged in
    can comment on blog posts. Comments are stored in the Comment entity and
    users are redirected back to the blog post permalink page. If a user doesn't
    enter text in the comment box, the page reloads with an error message.
    """

    def render_addcomment(self, comment='', error=''):
        self.render('addcomment.html', comment=comment, error=error)

    def get(self, post_id, user_id):
        if self.user:
            self.render_addcomment()
        else:
            access_error = "sorry, you must be signed in to add a comment"
            self.render('front.html', access_error=access_error)

    def post(self, post_id, user_id):
        comment = self.request.get('comment')
        error = "please enter a comment"
        # Used to make sure the comment has an association to the correct
        # blog post.
        key = db.Key.from_path('Post', int(post_id), parent=helpers.blog_key())

        if comment:
            c = Comment(parent=key, user_id=int(user_id), comment=comment,
                        user_name=self.user.name)
            c.put()
            self.redirect('/' + post_id)
        else:
            self.render_addcomment(error=error)
