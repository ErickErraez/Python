from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase



#definir ventanas tipo Screen
class Inicio(Screen):
    nombre =ObjectProperty(None)
    ciudad =ObjectProperty(None)
    
    def enviarBtn(self):
        if self.nombre.text !="" and self.ciudad.text !="":
            self.reset()
            #envia a la siguiente ventana
            sm.current ="datos"
        else:
            formularioInvalido()
    #poner en blanco los valores
    def reset(self):
        self.nombre.text =""
        self.ciudad.text =""
    
class Datos(Screen):
    ciudad =ObjectProperty(None)
    edad =ObjectProperty(None)
    def siguienteBtn(self):
        
    
class Fin(Screen):
    





class WindowManager(ScreenManager):
    pass


#Nuestro html
kv = Builder.load_file("my.kv")
#Para manejar las ventanas
sm = WindowManager()
db = DataBase("users.txt")
#añadir ventanas al widget
screens = [Inicio(name="inicio"), Datos(name="datos"),Fin(name="fin")]
for screen in screens:
    sm.add_widget(screen)
#la ventana con la que quiero iniciar 
sm.current = "inicio"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__practica__":
    MyMainApp().run()
