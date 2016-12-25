# Understanding Flask Web Framework
# Author: Prashant Nair
#
# You will need to install flask module using 'pip install flask'
#
# Part 1- Basic Website

# Importing flask class object
from flask import Flask
#Instantiating the class . Default goes to your script call else go for __main__
app=Flask(__name__)

@app.route('/') # home page location

def home():
    return " Welcome to SECRET page!!"

if __name__=="__main__":
    app.run(debug=True)
