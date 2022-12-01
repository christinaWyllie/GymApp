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
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout


class RegForm(Screen):
    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    email = ObjectProperty(None)
    addr = ObjectProperty(None)
    phone = ObjectProperty(None)
    ssn = ObjectProperty(None)
    passw = ObjectProperty(None)
    pass

    def submit(self):
        fields = [self.fname,self.lname,self.email,self.addr,self.phone,self.ssn,self.passw]
        
        for field in fields:
            if (field.text == ""):
                invalidReg("empty")
                self.error = 1
                return

        if (self.email.text.find("@") != -1 and self.email.text.find(".") != -1):
            if len(self.phone.text) == 10:
                if len(self.ssn.text) == 9:
                    print("Name: ", self.fname.text, self.lname.text)
                    print("Email: ", self.email.text)
                    print("Address: ", self.addr.text)
                    print("Phone Number: ", self.phone.text)
                    print("SSN: ", self.ssn.text)
                    print("Password: ",self.passw.text)
                    self.reset()
                    return 0
                else:
                    invalidReg("ssn")
                    return 1
            else:
                invalidReg("phone")
                return 1
        else:
            invalidReg("email")
            return 1
    
    def reset(self):
        self.fname.text = ""
        self.lname.text = ""
        self.email.text = ""
        self.addr.text = ""
        self.phone.text = ""
        self.ssn.text = ""
        self.passw.text = ""

def invalidReg(type):
    if (type == "empty"):
        pop = Popup(title = "Error while creating account",
                    content = Label(text="Please fill in all fields."),
                    size_hint=(None,None), size=(400,400))
        pop.open()
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

class FourFieldLine(BoxLayout):
    pass

class FiveFieldLine(BoxLayout):
    pass


class ClientHomepage(Screen):

        tempClass = [["01/23/2022","9:50","0","test@gmail.com","John Smith"], ["01/24/2022","9:50","0","test2@gmail.com","Jalal Kawash"]]

        # tempClass = [{'date': '01/23/2022', 'time': '9:50', 'branchno': '0', 'email': 'test@gmail.com', 'tname':'John Smith'},
        #          {'date': '01/24/2022', 'time': '12:30', 'branchno': '0', 'email': 'test2@gmail.com', 'tname':'Jalal Kawash'},
        #          {'date': '01/25/2022', 'time': '9:50', 'branchno': '0', 'email': 'test3@gmail.com', 'tname':'Jane Smith'},
        #          {'date': '01/26/2022', 'time': '16:00', 'branchno': '0', 'email': 'test4@gmail.com', 'tname':'Kawhi Leonard'}
        #         ]

        # tempEquip = [{'equipno': '01', 'amount': '30', 'condition': 'Good', 'branchno': '0'},
        #          {'equipno': '02', 'amount': '25', 'condition': 'Maintenance', 'branchno': '0'},
        #          {'equipno': '03', 'amount': '122', 'condition': 'Good', 'branchno': '0'},
        #          {'equipno': '04', 'amount': '33', 'condition': 'Maintenance', 'branchno': '0'}
        #         ]

        def __init__(self, **kwargs):
            super(ClientHomepage, self).__init__(**kwargs)

            self.classes.data = [{'label_1': str(x['date']), 'label_2': str(x['time']), 'label_3': str(x['branchno']), 'label_4': x['email'], 'label_5': x['tname']} for x in self.getClasses()]
            # self.equipment.data = [{'label_1':str(x['equipno']), 'label_2': str(x['amount']), 'label_3': str(x['condition']), 'label_4': x['branchno']} for x in self.tempEquip]

        pass

        def getClasses(self):
            headers = ["date","time","branchno","email","tname"]
            result = [dict(zip(headers, data)) for data in self.tempClass]
            return result


class EmpHomepage(Screen):
    pass


Builder.load_file("pagemanager.kv")

sm = ScreenManager()
sm.add_widget(LoginForm(name="login"))
sm.add_widget(RegForm(name="registration"))
sm.add_widget(ClientHomepage(name="chomepage"))

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()