from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import pygame
from kivy.cache import Cache
from kivy.uix.image import Image
from threading import *
import socket
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
Config.set('graphics', 'resizable', 0)

Window.size = (600, 500)


kv = '''
main:
	BoxLayout:
		orientation: 'vertical'
		padding: root.width * 0.05, root.height * .05
		spacing: '5dp'
		BoxLayout:
			size_hint: [1,.85]
			Image:
				id: image_source
				source: 'inicial.jpg'
		BoxLayout:
			size_hint: [1,.15]
			GridLayout:
				cols: 3
				spacing: '10dp'
				Button:
					id: status
					text:'Play'
					bold: True
					background_color: (.27,.555,.85,1)
					on_press: root.playPause()
				Button:
					text: 'Close'
					bold: True
					background_color: (2.0, 0.0, 0.0, 1.0)
					on_press: root.close()
				Button:
					text: 'Setting'
					bold: True
					on_press: root.setting()

'''


class main(BoxLayout):
    ipAddress = None
    port = None

    def playPause(self):
        if self.ipAddress == None or self.port == None:
            box = GridLayout(cols=1)
            box.add_widget(Label(text="Ip or Port Not Set"))
            btn = Button(text="OK")
            btn.bind(on_press=self.closePopup)
            box.add_widget(btn)
            self.popup1 = Popup(title='Error', content=box, size_hint=(.8, .3))
            self.popup1.open()
        else:
            if self.ids.status.text == "Stop":
                self.stop()
            else:
                self.ids.status.text = "Stop"
                Clock.schedule_interval(self.recv, 0.1)

    def closePopup(self, btn):
        self.popup1.dismiss()

    def stop(self):
        self.ids.status.text = "Play"
        Clock.unschedule(self.recv)

    def recv(self, dt):
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(("127.0.0.1", 65432))
        received = []
        size = width, height = 640, 480
        while True:
            recvd_data = clientsocket.recv(1024000)
            if not recvd_data:
                break
            else:
                received.append(recvd_data)
        try:
            dataset = b''.join(v for v in received)
            # convert received image from string
            image = pygame.image.fromstring(dataset, size, "RGB")
        except Exception as err:
            print('Error'+err)
            pass
        try:
            pygame.image.save(image, "inicial.jpg")
            self.ids.image_source.reload()
        except:
            pass

    def close(self):
        App.get_running_app().stop()

    def setting(self):
        box = GridLayout(cols=2)
        box.add_widget(Label(text="IpAddress: ", bold=True))
        self.st = TextInput(id="serverText")
        box.add_widget(self.st)
        box.add_widget(Label(text="Port: ", bold=True))
        self.pt = TextInput(id="portText")
        box.add_widget(self.pt)
        btn = Button(text="Set", bold=True)
        btn.bind(on_press=self.settingProcess)
        box.add_widget(btn)
        self.popup = Popup(title='Settings', content=box, size_hint=(.6, .4))
        self.popup.open()

    def settingProcess(self, btn):
        try:
            self.ipAddress = self.st.text
            self.port = int(self.pt.text)
        except:
            pass
        self.popup.dismiss()


class videoStreamApp(App):
    def build(self):
        return Builder.load_string(kv)


videoStreamApp().run()
