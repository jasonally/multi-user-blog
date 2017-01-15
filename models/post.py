import helpers

from google.appengine.ext import db

class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)

    # things to likely add, user_id and likes

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return helpers.render_str("post.html", post=self)