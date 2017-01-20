#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from handlers.addcomment import AddCommentHandler
from handlers.blogfront import BlogFrontHandler
from handlers.deletecomment import DeleteCommentHandler
from handlers.deletepost import DeletePostHandler
from handlers.editcomment import EditCommentHandler
from handlers.editpost import EditPostHandler
from handlers.likepost import LikePostHandler
from handlers.login import LoginHandler
from handlers.logout import LogoutHandler
from handlers.newpost import NewPostHandler
from handlers.post import PostHandler
from handlers.signup import SignupHandler
from handlers.unlikepost import UnlikePostHandler
from webapp2 import WSGIApplication

app = WSGIApplication([
    ('/(\d+)/add/(\d+)', AddCommentHandler),
    ('/', BlogFrontHandler),
    ('/([0-9]+)/([0-9]+)/delete/([0-9]+)', DeleteCommentHandler),
    ('/([0-9]+)/delete/([0-9]+)', DeletePostHandler),
    ('/([0-9]+)/([0-9]+)/edit/([0-9]+)', EditCommentHandler),
    ('/(\d+)/edit', EditPostHandler),
    ('/(\d+)/like', LikePostHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/newpost', NewPostHandler),
    ('/signup', SignupHandler),
    ('/(\d+)', PostHandler),
    ('/(\d+)/unlike', UnlikePostHandler),
], debug=True)
