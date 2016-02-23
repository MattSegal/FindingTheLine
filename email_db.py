from mysql import connector as sql
import gc # garbage collection
import re as regex

PROD_DB = "findingtheline"
TEST_DB = "ftl_test"
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

def connect(test=True):
    config = {
        'user':'root',
        'password':'chloe000',
        'host':'localhost',
        'database': TEST_DB if test else PROD_DB
    }
    con = sql.connect(**config)
    cur = con.cursor()
    return con, cur

def disconnect(con,cur):
    con.commit()
    cur.close()
    con.close()
    gc.collect() # not sure if necessary, Sentdex guy thinks so

def is_valid_email(email):
    if regex.match(VALID_EMAIL_REGEX, email):
        return True
    else:
        return False

def post_email(email, test=False):
    print email
    (con,cur) = connect(test=test)
    add_email = "INSERT INTO emails(email) VALUES(%s)"
    cur.execute(add_email,(email,))
    disconnect(con,cur)
    return True
    try:
        pass
    except:
        return False

def get_all_emails(test=False):
    try:
        (con,cur) = connect(test=test)
        cur.execute("SELECT email FROM emails")
        emails_raw = cur.fetchall()
        emails = []
        for email in emails_raw:
            emails.append(email[0])
        disconnect(con,cur)
        return emails
    except:
        disconnect(con,cur)
        return [("Database error :(")]

def seed_emails(test=True):
    setup_email(test=test)
    for email in VALID_EMAILS:
        post_email(email,test=test)
    emails = get_all_emails(test=test)
    assert len(emails) == len(VALID_EMAILS)

def setup_email(test=True):
    (con,cur) = connect(test=test)
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS emails")
    create_users = "CREATE TABLE emails (id INT(11) AUTO_INCREMENT PRIMARY KEY,email VARCHAR(100))"
    cur.execute(create_users)
    cur.execute("DESCRIBE emails")
    output = cur.fetchall()
    print output
    disconnect(con,cur)

def test_post_email():
    setup_email(test=True)
    assert post_email("test@example.com",test=True)
    (con,cur) = connect(test=True)
    cur.execute("SELECT * FROM emails")
    print str(cur.fetchone())
    cur.execute("SELECT COUNT(email) FROM emails")
    count = cur.fetchone()
    assert count[0] == 1
    disconnect(con,cur)

def test_test_db():
    (con,cur) = connect(test=True)
    assert con.get_database() == u'ftl_test'

def test_prod_db():
    (con,cur) = connect(test=False)
    assert con.get_database() == u'findingtheline'

def test_is_valid_email():
    for email in VALID_EMAILS:
         assert is_valid_email(email)
    for email in INVALID_EMAILS:
         assert not is_valid_email(email) 

def test_seed_emails():
    seed_emails()

if __name__ == "__main__":
    pass
    setup_email(test=True)
    # setup_email(test=False)