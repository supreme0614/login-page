import os

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='Sirojiddin',
    passwd='',
    database='Users'
)

my_cursor = mydb.cursor()


class User:

    def __init__(self, name=None, login=None, password=None, age=None):
        self.name = name
        self.login = login
        self.password = password
        self.age = age
        self.entering_values = ["1", "2", "3"]
        self.entering()

    def entering_massage(self):
        self.clear()
        print("""
                Hello, welcome
            1 -> Register
            2 -> Login
            3 -> Exit

        """)

    def entering(self):
        self.entering_massage()
        value = input(f"{entering_values}: ").strip()
        while not value.isdigit() or value not in self.entering_values:
            self.entering_massage()
            value = input(f"{entering_values}: ").strip()
        if value == self.entering_values[0]:
            self.register()

        elif value == self.entering_values[1]:
            self.log_in()
        else:
            self.clear()
            print("bye")
            exit()

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
        os.system('clear')

    def cheking_is_empty(self):
        pass
