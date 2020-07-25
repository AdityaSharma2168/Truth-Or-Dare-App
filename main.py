from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from pathlib import Path
import random

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "login_screen_success"
        else:
            self.ids.login_wrong.text = "Sorry, The Username Or Password You Entered was Incorrect. Please Try Again!"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {'username': uname, 'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        with open("users.json", 'w') as file:
            json.dump(users,file)
        self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def go_to_login(self):
        
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "left"
        self.manager.current = "login_screen"

    def go_to_truths_and_dares_screen(self):
        self.manager.transition.direction = "right"
        self.manager.current = "truths_and_dares_screen"

class TruthsAndDaresScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = "left"
        self.manager.current = "login_screen"

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()