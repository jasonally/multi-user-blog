import helpers

from google.appengine.ext import db

class Post(db.Model):
    """Creates the Post entity. For each entry, subject and content are provided
    by the user. user_id is obtained from the user's login cookie, and created
    and last_modified are updated as entries are created and/or updated. likes
    is set to 0 by default but is updated in its associated handlers as users
    like and unlike posts.
    """
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    user_id = db.IntegerProperty(required=True)
    likes = db.IntegerProperty(default=0)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def render(self):
        # Each post is tied to a specific user. This is used to get the data
        # for the user who created a particular post, which is used to control
        # what features a logged-in user can access on a blog permalink page.
        key = db.Key.from_path('User', int(self.user_id),
            parent=helpers.user_key())
        user = db.get(key)

        # Strips \n from blog posts and replaces them with <br> tags so posts
        # are properly rendered in HTML.
        self._render_text = self.content.replace('\n', '<br>')
        return helpers.render_str("post.html", post=self, username=user.name)

    @classmethod
    def by_id(cls, user_id):
        return Post.get_by_id(user_id, parent=helpers.blog_key())