from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    blogs = db.relationship('Blog', backref='users')

    def __repr__(self):
        return f'<User user_id={self.user_id}, username={self.username}, email={self.email}>'
  

class Blog(db.Model):
    """A blog."""

    __tablename__ = "blogs"

    blog_id = db.Column(db.Integer,primary_key=True)
    blog_created_datetime = db.Column(db.Integer)
    title = db.Column(db.String)
    overview = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    blogentries = db.relationship('BlogEntry', backref='blogs')


    def __repr__(self):
        return f'<Blog blog_id={self.blog_id}, title={self.title}, overview={self.overview} >'

class BlogEntry(db.Model):
    """A entry."""

    __tablename__ = "blogentries"

    entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.blog_id'))
    entry_datetime = db.Column(db.Integer)
    content=db.Column(db.String)

    # blogcomments = db.relationship('BlogEntries', backref='blogentries', secondary='entry_id')

    def __repr__(self):
        return f'<BlogEntry={self.entry_id} blog={self.blog_id}>'

class Comment(db.Model):
    """A comment."""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
     
    blog_id= db.Column(db.ForeignKey('blogs.blog_id'))
    user_id= db.Column(db.ForeignKey('users.user_id'))
    comment = db.Column(db.String)
    
    
    def __repr__(self):
        return f'<comment user_id={self.user_id} comment={self.comment_id}>'




# db.create_all()


def connect_to_db(flask_app, db_uri='postgresql:///hellosisters', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    db.create_all()
