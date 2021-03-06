# Project: Multi-User Blog

### About
This project uses material from Udacity's [Intro to Backend](https://www.udacity.com/course/intro-to-backend--ud171) course to build a multi-user blog. Users can create accounts on the blog, post entries, and like and comment on other users' posts.

### Directory contents
1. `handlers/` - Contains the handlers that generate pages on the blog.
2. `models/` - Contains the [Google App Engine](https://cloud.google.com/appengine/) datastores which contain data about the users, posts, comments, and likes.
3. `static/` - Contains the Bootstrap CSS files as well as main.css, which provides custom CSS formatting for the blog.
4. `templates/` - Contains the [Jinja](http://jinja.pocoo.org/) templates used to render HTML on the blog's pages.
5. `helpers.py` - A file containing Python helper functions each handler uses.
As well as main.py, app.yaml, and index.yaml files which are customary in webapp2 web applications.

### How to view the blog
1. Clone this repo to your computer, open Terminal and navigate to the directory.
2. Run dev_appserver.py . to launch the blog at localhost:8080.

Alternatively, this blog is on the web at [jasonally-fsnd-blog.appspot.com](http://jasonally-fsnd-blog.appspot.com/).

### Areas for improvement
The blog's appearance could be improved by installing a different theme, though it already has the basics of responsive design. Blog comments also do not properly display line breaks, as already noted in a TODO in comment.py.

### Thank you
The Udacity, Stack Overflow, and GitHub communities were invaluable in helping me finish this project. I'm happy to return the favor to others as they learn about web development.
