import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Homepage(Screen):
    pass


class RegForm(Screen):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    email = ObjectProperty(None)
    addr = ObjectProperty(None)
    phone = ObjectProperty(None)
    ssn = ObjectProperty(None)
    pass

    def submit(self):
        print("Name: ", self.fname.text, self.lname.text)
        print("Email: ", self.email.text)
        print("Address: ", self.addr.text)
        print("Phone Number: ", self.phone.text)
        print("SSN: ", self.ssn.text)


class LoginForm(Screen):
    # fname = ObjectProperty(None)
    # lname = ObjectProperty(None)
    # email = ObjectProperty(None)
    # addr = ObjectProperty(None)
    pass

    # def submit(self):
    #     #Possible SQL query
    #     print("First Name:", self.fname.text, "Email:", self.email.text)
    #     self.fname.text = ""
    #     self.lname.text = ""
    #     self.email.text = ""
    #     self.addr.text = ""

class PageManager(ScreenManager):
    pass


pageManager = Builder.load_file("pagemanager.kv")

class MainApp(App):
    def build(self):
        return pageManager

if __name__ == "__main__":
    MainApp().run()