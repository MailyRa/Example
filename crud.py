from model import db, User,Blog,Comment,connect_to_db


def create_user(username, email, password):
    """Create and return a new user."""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

# USE THE CLASS NAMES NOT TABLE

def create_blog(title, overview):
    """Create and return a new blog."""

    blog=Blog(title=title,
                  overview=overview)

    db.session.add(blog)
    db.session.commit()

    return blog


def get_user_by_email(email):

    return User.query.filter(User.email==email).first()


def create_comment(comment, user_id, blog_id):
    """Create and return a new comment."""

    comment=Comment(comment=comment, user_id=user_id, blog_id=blog_id)

    db.session.add(comment)
    db.session.commit()

    return comment

def get_all_blogs():

    return Blog.query.all()

def get_blog_by_id(blog_id):

    return Blog.query.filter_by(blog_id=blog_id).one()

def get_comments_by_blog_id(blog_id):

    return Comment.query.filter_by(blog_id=blog_id).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)