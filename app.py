from flask import Flask,render_template,request
from model import classify_new_complaint
from vertexai import generate
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dotenv

dotenv.load_dotenv()


app = Flask(__name__)
dept=''
data=''
@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        data = request.form.get('textarea')
        dept = classify_new_complaint(data)
        send_letter(data,dept)
        return render_template("index.html")
    return render_template("index.html")

# Function to send the email
def send_letter(complaint, dept):
    vertex_ans = generate(complaint, dept)
    dic = {
        'credit_card': 'docsaniruddhasangule2001@gmail.com',
        'retail_banking': 'docsaniruddhasangule2001@gmail.com',
        'credit_reporting': 'docsaniruddhasangule2001@gmail.com',
        'mortgages_and_loans': 'docsaniruddhasangule2001@gmail.com',
        'debt_collection': 'docsaniruddhasangule2001@gmail.com'
    }
    email = dic[dept]

    # Environment variables for security
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")  # Replace with your email
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")  # Replace with your app password
    RECEIVER_EMAIL = email

    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "Forwarded Complaint to Appropriate Department"

    # Email body
    body = f"""Dear Customer,

    I hope this email finds you well.

    {vertex_ans}

    Best,
    AIComplaintHub
    """
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("Email sent successfully!")
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False


if __name__ == "__main__":
    app.run(debug=True)