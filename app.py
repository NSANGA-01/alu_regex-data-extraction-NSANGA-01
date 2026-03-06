#importing the necessary libraries
from flask import Flask, render_template, request
import re


app = Flask(__name__)

#route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    
    emails = []
    urls = []
    phones = []
    credit_cards = []
    currency = []

    if request.method == "POST":

        # reading the content of the file
        with open("data.txt", "r") as file:
            text = file.read()

        # Regex patterns
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        url_regex = r'https?://[^\s]+'
        phone_regex = r'(\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
        credit_card_regex = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
        currency_regex = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

        # Extracting data using regex
        emails = re.findall(email_regex, text)
        urls = re.findall(url_regex, text)
        phones = re.findall(phone_regex, text)  
        credit_cards = re.findall(credit_card_regex, text)
        currency = re.findall(currency_regex, text)  
                           
    return render_template('extract.html', 
                           emails=emails, 
                           urls=urls, 
                           phones=phones, 
                           credit_cards=credit_cards, 
                           currency=currency   )








if __name__ == '__main__':
    app.run(debug=True) 
