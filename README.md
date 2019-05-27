# Packages required
Using python and flask library for creating a functional website that can be deployed on a live web server.

1. Install the latest version of flask using pip by running the command:
2. pip install flask
3. pip install virtualenv


# Directories for the html, css and image files
1. Within the main directory, create a folder called templates to store the html files:

2. website-using-python-flask > templates > about.html, home.html, layout.html

3. website-using-python-flask > static > css > main.css

# Using the virtual environment
1. Run the following commands:
2. python -m venv virtual
3. virtual\Scripts\pip install flask
4. virtual\Scripts\python website-using-python-flask\script1.py

# Deploying on a free live server
1. Create an account on www.heroku.com if you don't have one already.
2. Download and install Heroku Toolbelt from www.toolbelt.heroku.com/
3. Install gunicorn with "pip install gunicorn". Make sure you're using pip from your virtual environment if you have one.
4. Create a requirement.txt file in the main app directory where the main Python app file is located. You can create that file by running "pip freeze > requirements.txt" in the command line. Make sure you're using pip from your virtual environment if you have one. The requirement.txt file should now contain a list of Python packages.
5. Create a file named "Procfile" in the main app directory. The file should not contain any extension. Then type in this line inside: "web: gunicorn script1:app" where "script1" should be replaced with the name of your Python script and "app" with the name of the variable holding your Flask app.
6. Create a runtime.txt file in the main app directory and type "python-3.7.3" inside.
***Confirm supported Python version on https://devcenter.heroku.com/articles/python-support#supported-runtimes***
If you're using Python 2, you may want to type in "python-python-2.7.16" instead.
7. Open your computer terminal/command line to point to the directory where the Python file containing your app code is located.
8. Using the terminal, log in to Heroku with "heroku login"
9. Enter your Heroku email address
10. Enter your Heroku password
11. Create a new Heroku app with "heroku create myawesomeappname"
17. Initialize a local git repository with "git init"
18. Add your local application files to git with "git add ."
19. Tell git your email address with "git config --global user.email "myemail@hotmail.com"". Make sure the email address is inside quotes here. 
20. Tell git your username (just pick whatever username) with "git config --global user.name "whateverusername"". The username should be in quotes. ***Using the real app name***
21. Commit the changes with "git commit -m "first commit"". Make sure "first commit" is inside quotes.
22. Before pushing the changes to Heroku, tell heroku the name of the app you want to use with "heroku git:remote --app myawesomeappname" ***Using the real app name***
23. Push the changes to Heroku with "git push heroku master"
26. That should do it. Go ahead and open your app with "heroku open".

# Maintaining the website
1. Open cmd and cd into directory
2. Using the terminal, log in to Heroku with "heroku login"
3. Enter the command "heroku git:remote --app myawesomeappname" ***Using the real app name***
4. Enter the command "git add."
5. Enter the command "git commit -m "Some commit comment""
6. Enter the command "git push heroku master"
