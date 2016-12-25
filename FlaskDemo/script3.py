# Understanding Flask Web Framework
# Author: Prashant Nair
#
# You will need to install flask module using 'pip install flask'
#
# Part 2- Using Render Template

# Importing flask class object
from flask import Flask,render_template

#Instantiating the class . Default goes to your script call else go for __main__
app=Flask(__name__)

@app.route('/') # home page location

def home():
    return render_template("home.html")

@app.route('/about') # secret page location

def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
