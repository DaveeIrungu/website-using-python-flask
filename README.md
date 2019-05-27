# Packages required
Using python and flask library for creating a functional website that can be deployed on a live web server.

Install the latest version of flask using pip by running the command:
pip install flask
pip install virtualenv


# Directories for the html, css and image files
Within the main directory, create a folder called templates to store the html files:

website-using-python-flask > templates > about.html, home.html, layout.html

website-using-python-flask > static > css > main.css

# Using the virtual environment
Run the following commands:
python -m venv virtual
virtual\Scripts\pip install flask
virtual\Scripts\python website-using-python-flask\script1.py

# Deploying on a free live server
Visit heroku.com and create free account.
Download and install heroku toolbelt.
Open command line and cd into directory then type: heroku login.
Enter credentials and login.
Create app by entering command: heroku create [a unique website name].

