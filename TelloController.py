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

    def left(self):
        self.drone.move_left(2)

    def right(self):
        self.drone.move_right(2)

    def moveup(self):
        print('going up')
        #self.drone.move_up(2)

    def movedown(self):
        self.drone.move_down(2)