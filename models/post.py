import helpers

from google.appengine.ext import db

class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    user_id = db.IntegerProperty(required=True)
    likes = db.IntegerProperty(default=0)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    def render(self):
        key = db.Key.from_path('User', int(self.user_id),
            parent=helpers.user_key())
        user = db.get(key)

        self._render_text = self.content.replace('\n', '<br>')
        return helpers.render_str("post.html", post=self, username=user.name)