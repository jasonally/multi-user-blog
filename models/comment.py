# TODO(jasonally): Comments currently do not render line breaks. A
# render_text() method like in the Post model might help.

from google.appengine.ext import db

class Comment(db.Model):
    """Model for containing comments posted on the blog.
    """
    comment = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    user_id = db.IntegerProperty(required=True)
    user_name = db.TextProperty(required=True)