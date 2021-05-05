
from flask import (Flask, render_template, request, flash, session,
                   redirect)

import crud
from model import connect_to_db, User, Blog
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    return render_template('homepage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_user', methods=['POST'])
def login_user():

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        if (user.password == password):
            flash("Welcome!")
            session['user_id'] = user.user_id

            return redirect("/all_blogs")
        else:
            flash("Invalid password or email try again")
            return redirect("/login") 

@app.route('/logout_user')
def logout_user():
    """ user logout"""
    del session['user']
    return redirect("/")



@app.route('/register_user')
def register():
    return render_template('register_user.html')



@app.route('/handle_register_user', methods=['POST'])
def register_user():

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash ("Email exists in database try another email")
        return redirect('')
    else:
        crud.create_user(username, email, password)
        flash("Account created")
        return redirect('/all_blogs')



@app.route('/all_blogs')
def all_photos():
    """ Displaying all photos"""

    blogs = crud.get_all_blogs()

    result = list()
    for blog in blogs:
        comments = crud.get_comments_by_blog_id(blog.blog_id)
        result.append({
            "blog": blog,
            "comments": comments, 
        })

    return render_template('all_blogs.html',result=result)


@app.route("/add_comment", methods=['POST'])
def add_comment():
    """User adding a comment to a blog"""

    user_id = session.get("user_id")
    blog_id = request.form.get("blog_id")
    comment = request.form.get("comment")


    blog = crud.get_blog_by_id(blog_id)

    add_comment = crud.create_comment(comment=comment, user_id=user_id, blog_id=blog_id)

    flash("Your Comment has been added")

    return redirect('/all_blogs')
   

    
    



    
if __name__ == '__main__':
    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0', debug=True)