import tello
from kivy.uix.widget import Widget
import kivy
from kivy.lang import Builder
Builder.load_file('tello.kv')

class TelloController(Widget):
    def initialise(self):
        self.drone = tello.Tello('192.168.10.2', 8889)

    def takeoff(self):
        self.drone.takeoff()

    def land(self):
        self.drone.land()