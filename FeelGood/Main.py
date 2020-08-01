import glob
import random
from datetime import datetime
from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json

Builder.load_file('design.kv')


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "Signup_screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "Loginscreen_success"
        else:
            self.ids.login_wrong.text = "Wrong username or password!"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname, 'password': pword,
                        'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}
        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.current = "Signup_screen_success"


class SignUpScreenSuccess(Screen):
    def login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Login_screen"


class LoginScreenSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Login_screen"

    def get_quote(self, feelings):
        feel = feelings.lower()
        available_feelings = glob.glob("quotes/*.txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quotes.text = random.choice(quotes)
        else:
            self.ids.quotes.text = "Try again"


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
