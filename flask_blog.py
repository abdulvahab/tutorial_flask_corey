from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '001786'

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


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)  

if __name__ == "__main__":
    app.run(debug=True, port=5000)
