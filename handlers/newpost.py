import helpers

from handlers.blog import BlogHandler
from models.post import Post

class NewPostHandler(BlogHandler):
    """If the user is logged in, this handler renders a form for new blog posts.
    After the user submits a post, it's stored in the Post entity and the user
    is redirected to the entry page containing the blog post.
    """

    def render_newpost(self, subject='', content='', error=''):
        self.render('newpost.html', subject=subject, content=content,
                    error=error)

    def get(self):
        if self.user:
            self.render_newpost()
        else:
            access_error = "you must be signed in to create a new post"
            self.render('front.html', access_error=access_error)

    def post(self):
        if not self.user:
            return self.redirect('/login')

        if self.user:
            subject = self.request.get('subject')
            content = self.request.get('content')
            error = "please enter both a subject and content"

        if subject and content:
            # key().id() is used throughout the blog to retrieve the unique
            # ID associated with users, posts, comments, and likes.
            p = Post(parent=helpers.blog_key(), subject=subject,
                content=content, user_id=self.user.key().id())
            p.put()
            self.redirect('/%s' % str(p.key().id()))
        else:
            self.render_newpost(subject, content, error)
