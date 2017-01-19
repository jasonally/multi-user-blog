import helpers

from google.appengine.ext import db
from handlers.blog import BlogHandler
from models.like import Like

class LikePostHandler(BlogHandler):

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=helpers.blog_key())
        post = db.get(key)

        if self.user and self.user.key().id() == post.user_id:
            access_error = "sorry, you can't like your own post"
            self.render('front.html', access_error=access_error)
        elif not self.user:
            self.redirect('/login')
        else:
            user_id = self.user.key().id()
            post_id = post.key().id()

            l = Like.all().filter('user_id =', user_id).filter('post_id =',
                post_id).get()

            if l:
                self.redirect('/' + str(post.key().id()))
            else:
                like = Like(parent=key, user_id=user_id, post_id=post_id)
                like.put()

                post.likes += 1
                post.put()

                self.redirect('/' + str(post.key().id()))
