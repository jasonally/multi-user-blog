import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.post import Post

class EditPostHandler(BlogHandler):
    """Allows users to edit their own blog posts. Handler gets the data for the
    post the user wants to edit, renders the post text, and then updates the
    post entity with the user's edits.
    """

    def render_editpost(self, subject='', content='', post_id='',
        error=''):
        self.render('editpost.html', subject=subject, content=content,
            post_id=post_id, error=error)

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id),
            parent=helpers.blog_key())
        p = db.get(key)

        # The user who created the post is the only one allowed to edit the
        # post.
        if self.user and self.user.key().id() == p.user_id:
            self.render_editpost(p.subject, p.content, post_id)
        elif not self.user:
            self.redirect('/login')
        else:
            access_error = "you can't edit a post you didn't create"
            self.render('front.html', access_error=access_error)

    def post(self, post_id):
        if not self.user:
            return self.redirect('/login')

        # Get the entry data for the given post.
        key = db.Key.from_path('Post', int(post_id), parent=helpers.blog_key())
        p = db.get(key)

        if self.user and self.user.key().id() == p.user_id:
            subject = self.request.get('subject')
            content = self.request.get('content')
            error = "please enter both a subject and content"

            if subject and content:
                # Update the subject and content fields for the given post.
                p.subject = subject
                p.content = content
                p.put()
                self.redirect('/%s' % str(p.key().id()))
            else:
                self.render_editpost(subject, content, post_id, error)

        else:
            access_error = "you can't edit a post you didn't create"
            self.render('front.html', access_error=access_error)
