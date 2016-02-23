import sqlite3 as lite
import re as regex

VALID_EMAIL_REGEX = '^(([^<>()\[\]\.,;:\s@"]+(\.[^<>()\[\]\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
VALID_EMAILS = [
    "mattdsegal@gmail.com",
    "findingtheline@gmail.com",
    "bobby.jane@gmail.com.au",
    "bobby.jane@gmail.com",
    "koolkid90@hotmail.com",
    "gang99sta@it.bly",
    "example@email.com",]
INVALID_EMAILS = [
    "mattdsegalgmail.com",
    "findingtheline@gmailcom",
    "@gmail.com.au",
    "@gmail.com",
    "@.com",
    "gang99sta@bly",
    "example@email.com.",]

def is_valid_email(email):
    if regex.match(VALID_EMAIL_REGEX, email):
        return True
    else:
        return False

def post_email(email, test=False):
    db = 'test_db.sqlite' if test else 'database.sqlite'
    con = lite.connect(db)
    try:
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO emails(email) VALUES (?)",(email,))
        return True
    except sqlite3.OperationalError:
        return False

def get_all_emails(test=False):
    db = 'test_db.sqlite' if test else 'database.sqlite'
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute("SELECT email FROM emails")
        emails_raw = cur.fetchall()
        emails = []
        for email in emails_raw:
            emails.append(email[0])
        return emails

def seed_emails(test=True):
    setup_email(test=test)
    for email in VALID_EMAILS:
        post_email(email,test=test)
    emails = get_all_emails(test=test)
    assert len(emails) == len(VALID_EMAILS)

def setup_email(test=True):
    db = 'test_db.sqlite' if test else 'database.sqlite'
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS emails")
        create_users = "CREATE TABLE emails (id INTEGER PRIMARY KEY,email TEXT)"
        cur.execute(create_users)

def test_is_valid_email():
    for email in VALID_EMAILS:
         assert is_valid_email(email)
    for email in INVALID_EMAILS:
         assert not is_valid_email(email) 

def test_setup_email():
    setup_email(test=True)
    db = 'test_db.sqlite'
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='emails'")
        table = cur.fetchone()
        assert table[0] == "emails"

def test_seed_emails():
    seed_emails()

if __name__ == "__main__":
    pass
    # setup_email(test=True)
    # setup_email(test=False)