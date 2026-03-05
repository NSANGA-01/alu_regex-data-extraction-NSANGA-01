#importing the necessary libraries
from flask import Flask, render_template, request
import re


app = Flask(__name__)

#route for the home page
@app.route('/')
def index():
    return render_template('extract.html')








if __name__ == '__main__':
    app.run(debug=True) 
