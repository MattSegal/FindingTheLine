
from flask import Flask , render_template, request, Response
from hashlib import sha1
import email_db

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('./landing.html')

@app.route('/contact/')
def contact():
    return render_template('./contact.html')

@app.route('/email/',methods=['POST'])
def post_email():
    email = request.get_data()
    if email_db.is_valid_email(email) and email_db.post_email(email,test=False):
        resp = Response(response='Successfully posted email',status = 200)
    else:
        resp = Response(response='Failed to post email',status = 500)
    return resp

@app.route('/login/',methods=['GET'])
def get_email():
    return render_template('./email_login.html')

@app.route('/login/',methods=['POST'])
def login():
    password = request.form['password']
    if is_valid_password(password):
        emails = email_db.get_all_emails(test=False)
        return render_template('./email_list.html',emails=emails)
    else:
        return render_template('./email_login.html')

def is_valid_password(password):
    PASSWORD_HASH = "1ee7760a3190c95641442f2be0ef7774e139fb1f"
    return sha1(password).hexdigest() == PASSWORD_HASH

if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=False)
