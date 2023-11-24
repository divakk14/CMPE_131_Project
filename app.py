from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# from flask import Flask


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firs_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(100),unique = True, nullable=False)
    password = db.Column(db.String(200),nullable=False)
    
@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        return redirect(url_for('index'))
    
@app.route('/')
def index():
    return 'Register Successful! Welcome to note taking App!'

if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()
    app.run(debug=True)

@app.route('/trash')
def trash():
    # Add logic for handling the trash route
    return render_template('trash.html')  # Replace 'trash.html' with the appropriate template

@app.route('/logout')
def logout():
    # Add logic for handling the logout route
    return redirect(url_for('index'))  # Redirect to the index route after logout

@app.route('/edit_profile')
def edit_profile():
    # Add logic for handling the edit profile route
    return render_template('edit_profile.html')  # Replace 'edit_profile.html' with the appropriate template

# ... (your existing routes)

if __name__ == '__main__':
    app.run(debug=True)  
    


# @app.route('/')
# def index():
#     return "Hello, world!"

# if __name__ == '__main__':
#     app.run()
    