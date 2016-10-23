from hashlib import sha1
import random

class Security:
    def __init__(self):
        # Make this harder to crack
        self._password_hash = "1ee7760a3190c95641442f2be0ef7774e139fb1f"
        self._session_hash  = self.get_random_hash()

    def get_random_hash(self):
        return sha1(str(random.random())).hexdigest()

    def set_new_session_hash(self):
        self._session_hash  = self.get_random_hash()

    def get_session_hash(self):
        return self._session_hash

    def is_valid_password(self,password):
        return sha1(password).hexdigest() == self._password_hash

    def is_logged_in(self,session):
        return session.has_key('ftl_logged_in') and session['ftl_logged_in'] == self._session_hash