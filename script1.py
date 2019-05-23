# Import class Flask from the flask library
from flask import Flask

# Create a __name__ variable to store flask object instance or flask application
# Special variable that is in python scripts
# Instantiate the Flask class
app = Flask(__name__)


@app.route('/')  # homepage
def home():
    return "Homepage content"


@app.route('/about/')  # about page
def about():
    return "About page content"


if __name__ == "__main__":
    app.run(debug=True)
