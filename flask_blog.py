from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '001786'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique= True, nullable=False)
    email = db.Column(db.String(120), unique= True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False )
    #posts = db.relationship('Post', backref='author', lazy=True)

    def __rep__(self):
        return f"User('{self.username}','{self.email}','{self.imagefile}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, default=datetime.utcnow)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False, )
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __rep__(self):
        return f"Post('{self.title}','{self.date_posted}')"

p = [
{
'name' : "Abdulvahab Kharadi",
'age': 38,
'address' : "56 Asquith road Oxford- OX4 4RH",
'email':"vahab_n@yahoo.com"
},
{
'name' : "Mohammadwasim Saiyed",
'age':37,
'address': "14, chester road, Ilford, London- IG3 8PS",
'email': "wasim.saiyed@gmail.com"
}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/persons")
def persons():
    return render_template("persons.html", persons=p, title='Persons')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)  

if __name__ == "__main__":
    app.run(debug=True, port=5000)
