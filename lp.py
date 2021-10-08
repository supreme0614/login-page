import os

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='Sirojiddin',
    passwd='siroj2002',
    database='Users'
)

my_cursor = mydb.cursor()


class User:

    def __init__(self, name=None, login=None, password=None, age=None):
        pass

    def entering_massage(self):
        pass

    def entering(self):
        pass

    def register(self):
        pass

    def insert_to_db(self):
        pass

    def cheking_login_from_db(self):
        pass

    def log_in(self):
        pass

    def actions_after_entering(self):
        pass

    def log_out(self):
        pass

    def update_login(self):
        pass

    def update_password(self):
        pass

    def massage_after_entering(self):
        pass

    def delete_account(self):
        pass

    def collect(self):
        pass

    def clear(self):
        pass

    def cheking_is_empty(self):
        pass


person = User()

