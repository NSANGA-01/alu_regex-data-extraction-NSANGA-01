
## Project Overview

This project is a Web-based Data Extraction Tool built using Python Flask and Regular Expressions (Regex).

The application reads a large text file that simulates data returned from an API and extracts specific types of structured data using Regular Expressions.

The extracted data includes:

- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Currency amounts

The goal of this project is to demonstrate how Regex can be used to extract meaningful information from large text responses, which is a common task in real-world backend and full-stack development.

---

## Project Objectives

The main objectives of this project are:

- Learn how to use Regular Expressions (Regex) for data extraction
- Build a simple web application using Flask
- Extract multiple types of data from a large text string
- Display extracted results on a web page
- Practice clean project structure and GitHub organization

---

## Technologies Used

- Python
- Flask Framework
- Regular Expressions (re module)
- HTML
- Git & GitHub

---

📁 Project Structure

alu_regex-data-extraction-yourusername/

│
├── app.py

├── data.txt

├── README.md

└── templates/

    └── extract.html

## File Descriptions

app.py
The main Flask application.
It reads the text file, performs Regex extraction, and sends results to the HTML template.

data.txt
A sample text file that simulates an API response containing mixed data types.

templates/extract.html
The front-end page that contains the Extract Info button and displays the extracted results.

---

## How the Application Works

1. The user opens the web application in the browser.
2. The page displays a button labeled Extract Info.
3. When the button is clicked:
   - A POST request is sent to the Flask server.
4. The Flask application:
   - Reads the content from "data.txt"
   - Applies several Regex patterns
   - Extracts matching data
5. The extracted results are displayed on the web page.

## Application Flow:

User clicks "Extract Info"
        ↓
Flask receives POST request
        ↓
Read data.txt
        ↓
Apply Regex patterns
        ↓
Extract matching data
        ↓
Display results in browser

---

## Implemented Regex Patterns

The following data types are extracted using Regex:

1️⃣ Email Addresses

Examples:

user@example.com

firstname.lastname@company.co.uk

2️⃣ URLs

Examples:

https://www.example.com

https://subdomain.example.org/page

3️⃣ Phone Numbers

Examples:

(123) 456-7890

123-456-7890

123.456.7890

4️⃣ Credit Card Numbers

Examples:

1234 5678 9012 3456

1234-5678-9012-3456

5️⃣ Currency Amounts

Examples:

$19.99

$1,234.56

---

##  Installation & Running the Project

1. Clone the repository

git clone https://github.com/NSANGA-01/alu_regex-data-extraction-NSANGA-01.git

2. Navigate to the project folder

cd alu_regex-data-extraction-yourusername

3. Install Flask

pip install flask

4. Run the Flask application

python app.py

5. Open the browser

Go to:

http://127.0.0.1:5000


Click Extract Info to see the extracted data.

---

##  Example Input

Example data in "data.txt":

Contact us at user@example.com.
Visit https://www.example.com.
Call 123-456-7890.
Price: $19.99.

---

📊 Expected Output

The application will extract and display:

- Emails
- URLs
- Phone numbers
- Credit cards
- Currency values

---

## Learning 

From this project, i learned:

- How Regular Expressions work
- How to extract structured data from unstructured text
- How to build a simple Flask web application
- How to organize a professional GitHub repository

---

## Author

Vedaste Ngiruwonsanga

fullstack software developer

# contact info 

linkedin : https://www.linkedin.com/in/ngiruwonsanga-vedatse-4947283b3

github : https://GitHub.com/NSANGA-01

watssap : https://wa.me/250796962532





---

📄 License

for education