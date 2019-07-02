from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.graphics import Color, Rectangle




class LoginWindow(Screen):
 

    def loginBtn(self):
       
            sm.current = "main"

class Salir(Screen):
    
    def exit(self):
       
            sm.current = "main"
      
class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.after.clear()
        with self.canvas.after:
            Color(0, 1, 0, 0.25)
            Rectangle(pos=self.pos, size=self.size)
            
             
class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""
    
    def logOut(self, instance):
        sm.current = "salir"

    def on_enter(self, *args):
        
        archivo = open("users.txt", "r")
        for text in archivo.readlines():
            label = MyLabel(
                            text=text,
                            pos=(20, 20),
                            size_hint=(0.5, 0.5))
            self.container.add_widget(label)
        archivo.close()
        boton = Button(text="cerrar",on_press=self.logOut)
        
        self.container.add_widget(boton)
        
        
        
class WindowManager(ScreenManager):
    pass






kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"),MainWindow(name="main"),Salir(name="salir")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
