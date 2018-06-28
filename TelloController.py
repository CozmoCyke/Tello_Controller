import tello
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
import kivy
from kivy.lang import Builder
Builder.load_file('tello.kv')

class TelloController(Widget):
    speed = NumericProperty(0)

    def initialise(self):
        return
        #self.drone = tello.Tello('192.168.10.2', 8889)
        #self.update_speed()

    def takeoff(self):
        self.drone.takeoff()

    def update_speed(self):
        #max speed = 28.8 km/h
        self.speed = self.drone.get_speed() / 28.8

    def land(self):
        self.drone.land()

    def left(self):
        self.drone.move_left(2)

    def right(self):
        self.drone.move_right(2)

    def forward(self):
        self.drone.move_forward(2)
        update_speed()

    def backwards(self):
        self.drone.move_backward(2)
        update_speed()

    def moveup(self):
        self.drone.move_up(2)

    def movedown(self):
        self.drone.move_down(2)

    def rotatecw(self):
        #rotate 90 degrees clockwise
        self.drone.rotate_cw(90)

    def rotateccw(self):
        #rotate 90 degrees counterclockwise
        self.drone.rotate_ccw(90)