import helpers

from google.appengine.ext import db

class User(db.Model):
    name = db.StringProperty(required=True)
    password_hash = db.StringProperty(required=True)
    email = db.StringProperty(required=False)
    created = db.DateTimeProperty(auto_now_add=True)

    # Decorator
    # See http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
    # Or https://www.reddit.com/r/Python/comments/2lrhp5/could_someone_give_me_an_eli5_for_decorators/
    #
    # get_by_id -- https://cloud.google.com/appengine/docs/python/datastore/modelclass#Model_get_by_id
    @classmethod
    def by_id(cls, user_id):
        return User.get_by_id(user_id, parent=helpers.user_key())

    # Return User object for a given username
    # https://cloud.google.com/appengine/docs/python/datastore/modelclass#Model_all
    @classmethod
    def by_name(cls, username):
        u = User.all().filter('name =', username).get()
        return u

    @classmethod
    def login(cls, name, password):
        u = cls.by_name(name)
        if u and helpers.valid_pw(name, password, u.password_hash):
            return u

    @classmethod
    def register(cls, username, password, email=None):
        password_hash = helpers.make_pw_hash(username, password)
        return User(parent=helpers.user_key(),
                    name=username,
                    password_hash=password_hash,
                    email=email)