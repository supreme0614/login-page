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
        self.all_data = []
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
        self.clear()
        name_input = input("Enter your name :").strip().capitalize()
        while not name_input.isalpha():
            self.clear()
            name_input = input("Enter your name: ").strip().capitalize()
        self.name = name_input
        login_input = input("Enter your login: ").strip().lower()
        while not self.cheking_is_empty(login_input) or not self.cheking_login_from_db(login_input):
            self.clear()
            login_input = input("Enter your login: ").strip().lower()
        self.login = login_input
        password_input = input("Enter your password: ").strip()
        confirm = input("Confirm your password: ").strip()
        while not self.cheking_is_empty(password_input) or password_input != confirm:
            self.clear()
            password_input = input("Enter your password: ").strip()
            confirm = input("Confirm your password: ").strip()
        self.password = password_input

        age_input = input("Enter your age: ").strip()
        while not age_input.isdigit():
            self.clear()
            age_input = input("Enter your age: ").strip()
        self.age = age_input

        self.insert_to_db(name_input, login_input, password_input, age_input)
        self.collect(self.login)
        self.actions_after_entering()

    def insert_to_db(self, name, login, password, age):
        q = f"insert into Persons(name, login, oassword, age)"\
            f"values('{name}', '{login}', '{password}', '{age}')"
        my_cursor.execute(q)
        mydb.commit()


    def cheking_login_from_db(self, values):
        q = f"select * from Persons where login='{values}'"
        my_cursor.execute(q)

        if my_cursor.fetchall():
            return False
        return True


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

    def collect(self, value):
        q = f"select * from Persons where login='{value}'"
        my_cursor.execute(q)
        self.all_data = my_cursor.fetchall()
    def clear(self):
        os.system('clear')

    def cheking_is_empty(self, value):
        if value:
            return True
        return False

