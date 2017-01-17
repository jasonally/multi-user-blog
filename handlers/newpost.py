import helpers

from handlers.blog import BlogHandler
from models.post import Post

class NewPostHandler(BlogHandler):

    def render_newpost(self, subject='', content='', error=''):
        self.render('newpost.html', subject=subject, content=content,
                    error=error)

    def get(self):
        if self.user:
            self.render_newpost()
        else:
            self.render('front.html', access_error="you must be signed in to create a new post")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')
        error = "Please enter both a subject and content."

        if subject and content:
            p = Post(parent=helpers.blog_key(), subject=subject, comment=comment)
            p.put()
            self.redirect('/%s' % str(p.key().id()))
        else:
            self.render_newpost(subject, content, error)