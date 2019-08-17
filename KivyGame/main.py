import emoji
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from random import shuffle
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from colorama import Fore
from kivy.core.window import Window
from threading import Timer
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import ObjectProperty

contador =0
cont2=0
class InicioWindows(Screen):

    def cargarTrain(self):
        sm.current = 'TrainMint'

    def cargarFurious(self):
        sm.current = 'Remember'


class Colormania(Screen, BoxLayout):
    def __init__(self, **kwargs):
        super(Colormania, self).__init__(**kwargs)
        
        self.first = Button(text="Nivel 1", pos=(
            80, 500), size_hint=(0.6, 0.2))
        self.first.bind(on_press=self.colNivelUno)

        self.second = Button(text="Nivel 2", pos=(
            80, 350), size_hint=(0.6, 0.2))
        self.second.bind(on_press=self.colNivelDos)

        self.back = Button(text="Regresar", pos=(80, 50), size_hint=(0.6, 0.2))
        self.back.bind(on_press=self.backMenu)
       
        
        self.add_widget(self.first)
        self.add_widget(self.second)
        self.add_widget(self.back)

    def colNivelUno(self, button):
        self.clear_widgets()
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Toca la caja que indica la tarea debes buscar\n un color especifico bien o el icono \n debes obtener 5 puntos para pasar")
        closeButton = Button(text="Cerrar")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        pop = Popup(title='Informacion', content=layout,
                    size_hint=(None, None), size=(350, 200))
        pop.open()
        closeButton.bind(on_press=pop.dismiss)
        self.cargarData()


    def validarEstrella(self, button):
        global contador
        if contador == 5:
            self.mensajeWin()
        elif contador != 5:
            if self.color[0] == (1,1,0,1) and self.labelEvento.text=='Color':
                contador += 1
                self.openScore()
            if self.labelEvento.text=='Significado' and self.labelObject.text == 'Estrella':
                contador += 1
                self.openScore()
            if self.labelEvento.text =='Significado' and self.labelObject.text == 'Amarrillo':
                contador += 1
                self.openScore()         
            

    def validarDos(self, button):
        global contador
        if contador == 5:
            self.mensajeWin()
        elif contador != 5:
            if self.color[0] == (0.250,0.250,0.6,1) and self.labelEvento.text=='Color':
                contador += 1
                self.openScore()
            if self.labelEvento.text=='Significado' and self.labelObject.text == 'Dos':
                contador += 1
                self.openScore()
            if self.labelEvento.text =='Significado' and self.labelObject.text=='Azul':
                contador += 1
                self.openScore()

    def validarCuadrado(self, button):
        global contador
        if contador == 5:
            self.mensajeWin()
        elif contador != 5:
            if self.color[0] == (1,0.150,.225,1) and self.labelEvento.text=='Color':
                contador += 1
                self.openScore()
            if self.labelEvento.text=='Significado' and self.labelObject.text == 'Cuadrado':
                contador += 1
                self.openScore()
            if self.labelEvento.text =='Significado' and self.labelObject.text=='Rojo':
                contador += 1
                self.openScore()

    def backMenu(self, button):
        sm.current = 'inicio'
    
    def mensajeWin(self):
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Felicidades has obtenido los "+str(contador)+ " puntos")
        nextLevel = Button(text="Siguiente Nivel")
        closeButton = Button(text="Cerrar")
        layout.add_widget(popupLabel)
        layout.add_widget(nextLevel)
        layout.add_widget(closeButton)
        pop = Popup(title='Informacion', content=layout,
            size_hint=(None, None), size=(350, 200))
        pop.open()
        nextLevel.bind(on_press=self.colNivelDos)
        closeButton.bind(on_press=self.backMenu)
        Clock.schedule_once(pop.dismiss, 2)
        self.cargarData()
        

    def cargarData(self):
        self.clear_widgets()
        with self.canvas:
            self.rect1 = Rectangle(pos=(30, 20), size=(80, 80), source='estrella.png')
            self.rect2 = Rectangle(pos=(150, 20), size=(80, 80), source='dos.png')
            self.rect = Rectangle(pos=(260, 20), size=(80, 80), source='cuadrado.png')
        self.yellow=(1,1,0,1)
        self.blue =(0.250,0.250,0.6,1)
        self.red=(1,0.150,.225,1)
        self.event=['Significado','Color']
        self.objectos=['Cuadrado','Estrella','Dos','Amarrillo','Azul','Rojo']
        self.color=[self.yellow,self.blue,self.red]
        shuffle(self.event)
        shuffle(self.objectos)
        shuffle(self.color)
        grid = GridLayout(rows=3, cols=2, row_default_height=550)
        floatLayout = FloatLayout(size=(100, 100))
        button1 = Button(size_hint=(.4, .13), pos=(32, 25), background_color=(0, 0, 0,0))
        button2 = Button(size_hint=(.4, .13), pos=(152, 25), background_color=(0, 0, 0, 0))
        button3 = Button(size_hint=(.4, .13), pos=(262, 25), background_color=(0, 0, 0, 0))
        floatLayout.add_widget(button1)
        floatLayout.add_widget(button2)
        floatLayout.add_widget(button3)
        self.labelEvento = Label(text=str(self.event[0]),color=self.color[0],font_size='30sp')
        self.labelObject = Label(text=str(self.objectos[0]),color=self.color[0],font_size='30sp')
        grid.add_widget(self.labelEvento)
        grid.add_widget(self.labelObject)
        grid.add_widget(floatLayout)
        button1.bind(on_press=self.validarEstrella)
        button2.bind(on_press=self.validarDos)
        button3.bind(on_press=self.validarCuadrado)
        self.add_widget(grid)

    def openScore(self):
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Has acertado ahora tienes \n " + str(contador) +" puntos")
        closeButton = Button(text="Cerrar")
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)
        pop = Popup(title='Informacion', content=layout,
            size_hint=(None, None), size=(350, 200))
        pop.open()
        closeButton.bind(on_press=pop.dismiss)
        self.cargarData()

    def colNivelDos(self, button):
        self.clear_widgets()
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Toca la caja que indica la tarea debes buscar\n un color especifico bien o el icono \n debes obtener 10 puntos para pasar")
        closeButton = Button(text="Cerrar")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        pop = Popup(title='Informacion', content=layout,
                    size_hint=(None, None), size=(350, 200))
        pop.open()
        closeButton.bind(on_press=pop.dismiss)

        self.cargarNivel2()

    def cargarNivel2(self):
        self.clear_widgets()
        with self.canvas:
            self.rect1 = Rectangle(pos=(30, 20), size=(80, 80), source='estrella.png')
            self.rect2 = Rectangle(pos=(150, 20), size=(80, 80), source='dos.png')
            self.rect = Rectangle(pos=(260, 20), size=(80, 80), source='cuadrado.png')
        self.yellow=(1,1,0,1)
        self.blue =(0.250,0.250,0.6,1)
        self.red=(1,0.150,.225,1)
        self.event=['Significado','Color']
        self.objectos=['Cuadrado','Estrella','Dos','Amarrillo','Azul','Rojo']
        self.color=[self.yellow,self.blue,self.red]
        shuffle(self.event)
        shuffle(self.objectos)
        shuffle(self.color)
        grid = GridLayout(rows=3, cols=2, row_default_height=550)
        floatLayout = FloatLayout(size=(100, 100))
        button1 = Button(size_hint=(.4, .13), pos=(32, 25), background_color=(0, 0, 0,0))
        button2 = Button(size_hint=(.4, .13), pos=(152, 25), background_color=(0, 0, 0, 0))
        button3 = Button(size_hint=(.4, .13), pos=(262, 25), background_color=(0, 0, 0, 0))
        floatLayout.add_widget(button1)
        floatLayout.add_widget(button2)
        floatLayout.add_widget(button3)
        self.labelEvento = Label(text=str(self.event[0]),color=self.color[0],font_size='30sp')
        self.labelObject = Label(text=str(self.objectos[0]),color=self.color[0],font_size='30sp')
        grid.add_widget(self.labelEvento)
        grid.add_widget(self.labelObject)
        grid.add_widget(floatLayout)
        button1.bind(on_press=self.validarEstrella2)
        button2.bind(on_press=self.validarDos2)
        button3.bind(on_press=self.validarCuadrado2)
        self.add_widget(grid)

    def mensajeWin2(self):
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Felicidades has obtenido los "+str(cont2)+ " puntos")
        closeButton = Button(text="Cerrar")
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)
        pop = Popup(title='Informacion', content=layout,
            size_hint=(None, None), size=(350, 200))
        pop.open()
        closeButton.bind(on_press=self.backMenu)

        Clock.schedule_once(pop.dismiss, 2)
        self.cargarNivel2()

    def openScore2(self):
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Has acertado ahora tienes \n " + str(cont2) +" puntos")
        closeButton = Button(text="Cerrar")
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)
        pop = Popup(title='Informacion', content=layout,
            size_hint=(None, None), size=(350, 200))
        pop.open()
        closeButton.bind(on_press=pop.dismiss)
        self.cargarNivel2()

    def validarEstrella2(self, button):
        global cont2
        if cont2 == 10:
            self.mensajeWin2()
        elif cont2 != 10:
            if self.color[0] == (1,1,0,1) and self.labelEvento.text=='Color':
                cont2 += 1
                self.openScore2()
            if self.labelEvento.text=='Significado' and self.labelObject.text == 'Estrella':
                cont2 += 1
                self.openScore2()
            if self.labelEvento.text =='Significado' and self.labelObject.text == 'Amarrillo':
                cont2 += 1
                self.openScore2()
            

    def validarDos2(self, button):
        global cont2
        if cont2 == 10:
            self.mensajeWin2()
        elif cont2 != 10:
            if self.color[0] == (0.250,0.250,0.6,1) and self.labelEvento.text=='Color':
                cont2 += 1
                self.openScore2()
            if self.labelEvento.text=='Significado' and self.labelObject.text == 'Dos':
                cont2 += 1
                self.openScore2()
            if self.labelEvento.text =='Significado' and self.labelObject.text=='Azul':
                cont2 += 1
                self.openScore2()

    def validarCuadrado2(self, button):
        global cont2
        if cont2 == 10:
            self.mensajeWin2()
        elif cont2 != 10:
            if self.color[0] == (1,0.150,.225,1) and self.labelEvento.text=='Color':
                cont2 += 1
                self.openScore2()
            if self.labelEvento.text=='Significado' and self.labelObject.text == 'Cuadrado':
                cont2 += 1
                self.openScore2()
            if self.labelEvento.text =='Significado' and self.labelObject.text=='Rojo':
                cont2 += 1
                self.openScore2()
        
class RememberImage(Screen):
    def __init__(self, **kwargs):
        super(RememberImage, self).__init__(**kwargs)
        self.first = Button(text="Nivel 1", pos=(
            80, 500), size_hint=(0.6, 0.2))
        self.first.bind(on_press=self.nivelUno)

        self.second = Button(text="Nivel 2", pos=(
            80, 350), size_hint=(0.6, 0.2))
        self.second.bind(on_press=self.nivelDos)

        self.back = Button(text="Regresar", pos=(80, 50), size_hint=(0.6, 0.2))
        self.back.bind(on_press=self.backMenu)

        self.add_widget(self.first)
        self.add_widget(self.second)
        self.add_widget(self.back)

    def backMenu(self, button):
        sm.current = 'inicio'

    def nivelUno(self, button):
        self.clear_widgets()
        layout = GridLayout(cols=1, padding=10)

        popupLabel = Label(
            text="Tienes 10 segundos para memorizar la imagen \n despues de los 10 segundos la imagen se borrara\n y deberas contestar las preguntas")
        closeButton = Button(text="Cerrar")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        pop = Popup(title='Informacion', content=layout,
                    size_hint=(None, None), size=(350, 200))
        pop.open()
        closeButton.bind(on_press=pop.dismiss)

        grid = GridLayout(rows=1)
        imagen = Image(source="memoria1.jpg", size_hint=(200, 1))
        grid.add_widget(imagen)
        self.add_widget(grid)
        Clock.schedule_once(self.playMemoryGame1, 10)

    def playMemoryGame1(self, button):
        self.clear_widgets()
        grid = GridLayout(cols=2, rows=5)
        pregunta1 = Label(text="Que tiene Homero \n en su cabeza?")
        self.respuesta1 = TextInput()
        pregunta2 = Label(text='Quien esta alado \n  de Magguie?')
        self.respuesta2 = TextInput()
        pregunta3 = Label(text='Quien sostiene \n una espada?')
        self.respuesta3 = TextInput()
        pregunta4 = Label(text='Que color eran \n los Globos?')
        self.respuesta4 = TextInput()
        grid.add_widget(pregunta1)
        grid.add_widget(pregunta2)
        grid.add_widget(self.respuesta1)
        grid.add_widget(self.respuesta2)
        grid.add_widget(pregunta3)
        grid.add_widget(pregunta4)
        grid.add_widget(self.respuesta3)
        grid.add_widget(self.respuesta4)
        verificar = Button(text='Ver respuestas')
        verificar.bind(on_press=self.calificarNivel1)
        grid.add_widget(verificar)
        self.add_widget(grid)

    def calificarNivel1(self, button):
        contador = 0
        if self.respuesta1.text == 'sombrero' or self.respuesta1.text == 'orejas de raton':
            contador = contador+1
        if self.respuesta2.text == 'marge simpson' or self.respuesta2.text == 'Marge':
            contador = contador+1
        if self.respuesta3.text == 'dark veider':
            contador = contador+1
        if self.respuesta4.text == 'azules' or self.respuesta4.text == 'azules con blanco':
            contador = contador + 1

        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Tienes " + str(contador) + " puntos en este nivel")
        nextLevel = Button(text="Siguiente Nivel")
        closeButton = Button(text="Menu Principal")

        layout.add_widget(popupLabel)
        layout.add_widget(nextLevel)
        layout.add_widget(closeButton)

        pop = Popup(title='Informacion', content=layout,
                    size_hint=(None, None), size=(350, 200))
        pop.open()
        nextLevel.bind(on_press=self.nivelDos)
        closeButton.bind(on_press=self.backMenu)
        Clock.schedule_once(pop.dismiss, 2)

    def nivelDos(self, button):
        self.clear_widgets()
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Tienes 7 segundos para memorizar la imagen \n despues de los 7 segundos la imagen se borrara\n y deberas contestar las preguntas")
        closeButton = Button(text="Cerrar")
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)
        pop = Popup(title='Informacion', content=layout,
                    size_hint=(None, None), size=(350, 200))
        pop.open()
        closeButton.bind(on_press=pop.dismiss)

        grid = GridLayout(rows=1)
        imagen = Image(source="memoria2.jpg", size_hint=(200, 1))
        grid.add_widget(imagen)
        self.add_widget(grid)
        Clock.schedule_once(self.playMemoryGame2, 7)

    def playMemoryGame2(self, button):
        self.clear_widgets()
        grid = GridLayout(cols=2, rows=9)
        pregunta1 = Label(text="Que sostiene el \n control remoto?")
        self.respuesta1 = TextInput()
        pregunta2 = Label(text='Quien esta teniendo \n una rosquilla?')
        self.respuesta2 = TextInput()
        pregunta3 = Label(text='Quien esta dormido?')
        self.respuesta3 = TextInput()
        pregunta4 = Label(text='Que tiene un reloj?')
        self.respuesta4 = TextInput()
        pregunta5 = Label(text='Donde hay un cuadro \n con un barco?')
        self.respuesta5 = TextInput()
        pregunta6 = Label(text='Quien tiene el color de \n piel mas oscuro?')
        self.respuesta6 = TextInput()
        pregunta7 = Label(text='Quien esta usando \n audifonos?')
        self.respuesta7 = TextInput()
        pregunta8 = Label(text='Quien esta alado \n izquierdo de Marge?')
        self.respuesta8 = TextInput()
        grid.add_widget(pregunta1)
        grid.add_widget(pregunta2)
        grid.add_widget(self.respuesta1)
        grid.add_widget(self.respuesta2)
        grid.add_widget(pregunta3)
        grid.add_widget(pregunta4)
        grid.add_widget(self.respuesta3)
        grid.add_widget(self.respuesta4)
        grid.add_widget(pregunta5)
        grid.add_widget(pregunta6)
        grid.add_widget(self.respuesta5)
        grid.add_widget(self.respuesta6)
        grid.add_widget(pregunta7)
        grid.add_widget(pregunta8)
        grid.add_widget(self.respuesta7)
        grid.add_widget(self.respuesta8)
        verificar = Button(text='Ver respuestas')
        verificar.bind(on_press=self.calificarNivel2)
        grid.add_widget(verificar)
        self.add_widget(grid)

    def calificarNivel2(self, button):
        contador = 0
        if self.respuesta1.text == 'homero'or self.respuesta1.text == 'homero simpson':
            contador = contador+1
        if self.respuesta2.text == 'el jefe gorgory'or self.respuesta2.text == 'el policia' or self.respuesta2.text == 'jefe gorgory':
            contador = contador+1
        if self.respuesta3.text == 'el abuelo'or self.respuesta3.text == 'Abbe Simpson':
            contador = contador+1
        if self.respuesta4.text == 'krusty el payaso'or self.respuesta4.text == 'krusty':
            contador = contador+1
        if self.respuesta5.text == 'en la pared'or self.respuesta5.text == 'atras de marge':
            contador = contador+1
        if self.respuesta6.text == 'Apu'or self.respuesta6.text == 'apu':
            contador = contador+1
        if self.respuesta7.text == 'otto'or self.respuesta7.text == 'el conductor de bus':
            contador = contador+1
        if self.respuesta8.text == 'bart'or self.respuesta8.text == 'bart simpson':
            contador = contador+1

        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(
            text="Tienes " + str(contador) + " puntos en este nivel")
        closeButton = Button(text="Menu Principal")

        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        pop = Popup(title='Informacion', content=layout,
                    size_hint=(None, None), size=(350, 200))
        pop.open()
        closeButton.bind(on_press=self.backMenu)
        Clock.schedule_once(pop.dismiss, 2)


class WindowsManager(ScreenManager):
    pass


kv = Builder.load_file("estilos.kv")
sm = WindowsManager()
Window.size = (375, 667)

screens = [InicioWindows(name="inicio"), Colormania(
    name="TrainMint"), RememberImage(name="Remember")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "inicio"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
