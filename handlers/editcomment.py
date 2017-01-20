import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.comment import Comment

class EditCommentHandler(BlogHandler):
    """Handler for editing comments. The handler retrieves the data for the
    comment the user wants to edit, renders the comment text, and then updates
    the comment entity with the user's edits.
    """

    def render_editcomment(self, comment='', error=''):
        self.render('editcomment.html', comment=comment, error=error)

    def get(self, post_id, post_user_id, comment_id):
        # Users should only be allowed to edit comments they posted.
        if self.user and self.user.key().id() == int(post_user_id):
            # Obtain the key value for the post in question
            post_key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())
            # Get the comment data for the given comment_id and post_key.
            key = db.Key.from_path('Comment', int(comment_id),
                parent=post_key)

            # Retrieve the comment entry.
            c = db.get(key)
            # Render editcomment.html with the comment text stored in the entry.
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
            # Store the updated text entered in by the user.
            comment = self.request.get('comment')

            # Retrieve the entry saved in Comment.
            post_key = db.Key.from_path('Post', int(post_id),
                parent=helpers.blog_key())
            key = db.Key.from_path('Comment', int(comment_id),
                parent=post_key)

            c = db.get(key)
            # Update the text field in the Comment entry.
            c.comment = comment
            c.put()
            self.redirect('/' + post_id)
        else:
            access_error = "sorry, you don't have permission to edit this comment"
            self.render('front.html', access_error=access_error)
