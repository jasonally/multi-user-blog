import hashlib
import hmac
import jinja2
import os
import re

from google.appengine.ext import db
from random import choice
from string import ascii_letters

##### Initialize Jinja2
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape = True)

##### Account validation
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

##### Rendering Jinja2 templates
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

##### Datastore keys
# Worth having so it's easier to build more blogs in the future using the same
# datastore
def blog_key(name='default'):
    return db.Key.from_path('blogs', name)

def user_key(name='default'):
    return db.Key.from_path('users', name)

##### Account security
SECRET = 'eiTh0aaD'

# xrange() doesn't exist in Python 3, FYI
def make_salt(length = 5):
    return ''.join(choice(ascii_letters) for x in range(length))

def make_pw_hash(name, password, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + password + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, password, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, password, salt)

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val