import os
import time
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='Sirojiddin',
    passwd='',
    database='Users'
)
my_cursor = mynew_logindb.cursor()


class User:

    def __init__(self, name=None, login=None, password=None, age=None):
        self.nnew_loginame = name
        self.login = login
        self.password = password
        self.age = age
        self.entering_values = ["1", "2", "3"]
        self.all_data = []
        self.passmin = 8
        self.options_after_entering = ["1", "2", "3", "4", "5"]
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
        value = input(f"{self.entering_values}: ").strip()
        while not value.isdigit() or value not in self.entering_values:
            self.entering_massage()
            value = input(f"{self.entering_values}: ").strip()
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
        q = f"insert into Persons(name, login, password, age)"\
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
        self.clear()
        login_login = input("Enter your login: ").strip().lower()
        self.collect(login_login)
        while not self.cheking_is_empty(login_login) or \
            not self.cheking_is_empty(self.all_data):
            self.clear()
            login_login = input("Enter your login: ").strip().lower()
            self.collect(login_login)

        self.clear()
        print(f"Welcom {self.all_data[0][1]}")
        password_password = input("Enter your password: ").strip()
        while password_password != self.all_data[0][3]:
            self.clear()
            password_password = input("Enter your password: ").strip()
        self.actions_after_entering()


    def actions_after_entering(self):
        self.massage_after_entering()
        option = input(f"{self.options_after_entering}: ").strip()
        while not option.isdigit() or option not in self.options_after_entering:
            self.massage_after_entering()
            option = input(f"{self.options_after_entering}: ").strip()
        if option == self.options_after_entering[0]:
            self.log_out()
        elif option == self.options_after_entering[1]:
            self.update_login()
        elif option == self.options_after_entering[2]:
            self.update_password()
        elif option == self.options_after_entering[3]:
            self.delete_account()
        else:
            self.clear()
            print("bye")
            exit()


    def log_out(self):
        self.entering()


    def update_login(self):

        self.clear()
        new_login = input("Enter new login: ").strip().lower()
        while not self.cheking_is_empty(new_login) or not self.cheking_login_from_db(new_login):
            self.clear()
            new_login = input("Enter new login: ").strip().lower()
        q = f"update Persons set login='{new_login}' where login='{self.all_data[0][2]}'"
        my_cursor.execute(q)
        mydb.commit()
        self.clear()
        print("login updated")
        time.sleep(3)
        self.massage_after_entering()
        self.actions_after_entering()

    def update_password(self):
        self.clear()
        new_password = input("Enter new password: ").strip()
        while not self.cheking_is_empty(new_password) :
            self.clear()
            new_password = input("Enter new password: ").strip()
        q = f"update Persons set password='{new_password}' where password='{self.all_data[0][3]}'"
        my_cursor.execute(q)
        mydb.commit()
        self.clear()
        print("password updated")
        time.sleep(3)
        self.massage_after_entering()
        self.actions_after_entering()
    def massage_after_entering(self):
        self.clear()
        print(f"""
        welcome {self.all_data[0][1]}
        1 log out 
        2 update login
        3 update password
        4 delete account
        5 exit
""")


    def delete_account(self):
        q = f"delete from Persons where login='{self.all_data[0][2]}'"
        my_cursor.execute(q)
        mydb.commit()
        self.clear()
        print("deleted")
        time.sleep(3)
        self.entering()

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


person = User()