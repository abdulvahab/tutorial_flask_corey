from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home1")
def home():
    return render_template("home1.html")

@app.route("/about1")
def another_page():
    return render_template("about1.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
