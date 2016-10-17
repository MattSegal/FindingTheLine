from flask import * # Fix me
from functools import wraps

import email_db
from membership import Security

app = Flask(__name__)
app.config.from_object('config.Config')
security = Security()

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
    if security.is_valid_password(password):
        security.set_new_session_hash()
        session['ftl_logged_in'] = security.get_session_hash()
        emails = email_db.get_all_emails(test=False)
        return render_template('./email_list.html',emails=emails)
    else:
        return render_template('./email_login.html')

def login_required(func):
    @wraps(func)
    def wrapper (*args,**kwargs): # steal func's args
        if security.is_logged_in(session):
            # Go on your merry way
            return func(*args,**kwargs) 
        else:
            return redirect(url_for('login'))
    return wrapper

@app.route('/download/', methods=['GET'])
@login_required
def download():
    emails = email_db.get_all_emails(test=False) # This is yuck
    txt = ""
    for email in emails:
        txt += email+"\n"
    response = make_response(txt)
    response.headers["Content-Disposition"] = "attachment; filename=emails.txt"
    return response

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
