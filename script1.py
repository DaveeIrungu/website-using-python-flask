from flask import Flask, render_template

# Create a __name__ variable to store flask object instance or flask application
# Special variable that is in python scripts
# Instantiate the Flask class
app = Flask(__name__)


@app.route('/')  # homepage
def home():
    return render_template("home.html")


@app.route('/about/')  # about page
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
