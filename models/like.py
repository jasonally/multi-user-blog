from google.appengine.ext import db

class Like(db.Model):
    """Model for containing unique data about each like users add to blog
    posts.
    """
    user_id = db.IntegerProperty(required=True)
    post_id = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)