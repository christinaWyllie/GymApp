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
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel

class Homepage(Screen):
    pass


class RegForm(Screen):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    email = ObjectProperty(None)
    addr = ObjectProperty(None)
    phone = ObjectProperty(None)
    ssn = ObjectProperty(None)
    passw = ObjectProperty(None)

    error = 0
    pass

    def submit(self):
        if (self.email.text.find("@") != -1 and self.email.text.find(".") != -1):
            if len(self.phone.text) == 10:
                if len(self.ssn.text) == 9:
                    print("Name: ", self.fname.text, self.lname.text)
                    print("Email: ", self.email.text)
                    print("Address: ", self.addr.text)
                    print("Phone Number: ", self.phone.text)
                    print("SSN: ", self.ssn.text)
                    print("Password: ",self.passw.text)
                    error = 0
                    self.reset()
                else:
                    error = 1
                    invalidReg("ssn")
            else:
                error = 1
                invalidReg("phone")
        else:
            error = 1
            invalidReg("email")
    
    def reset(self):
        self.fname.text = ""
        self.lname.text = ""
        self.email.text = ""
        self.addr.text = ""
        self.phone.text = ""
        self.ssn.text = ""
        self.passw.text = ""

def invalidReg(type):
    if (type == "email"):
        pop = Popup(title = "Error while creating account",
                    content = Label(text="Invalid email."),
                    size_hint=(None,None), size=(400,400))
        pop.open()
    elif (type == "phone"):
        pop = Popup(title = "Error while creating account",
                    content = Label(text="Invalid phone number."),
                    size_hint=(None,None), size=(400,400))
        pop.open()
    elif (type == "ssn"):
        pop = Popup(title = "Error while creating account",
                    content = Label(text="Invalid SSN."),
                    size_hint=(None,None), size=(400,400))
        pop.open()


class LoginForm(Screen):
    email = ObjectProperty(None)
    passw = ObjectProperty(None)
    pass

    def submit(self):
        #Possible SQL query
        print("Email:", self.email.text)
        print("Password:", self.passw.text)
        self.email.text = ""
        self.passw.text = ""

class PageManager(ScreenManager):
    pass


pageManager = Builder.load_file("pagemanager.kv")

class MainApp(App):
    def build(self):
        return pageManager

if __name__ == "__main__":
    MainApp().run()