import kivy
from kivy.app import App
from kivy.uix.popup import Popup
import TelloController

class TelloControllerBuilder(App):
    def build(self):
        menu = TelloController.TelloController()
        menu.initialise()
        self.popup = Popup(title='Controller', content=menu, auto_dismiss=False)
        self.popup.open()

if __name__ == '__main__':
    TelloControllerBuilder().run()