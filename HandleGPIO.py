import time
import gpiozero

class Car:
    def __init__(self, backmotor1, backmotor2, frontservo, frontservoReverser: bool, throttleMaxAfter: float):
        self.throttleMaxAfter = abs(throttleMaxAfter)
        self.frontservoReverser = frontservoReverser
        self.backmotor = gpiozero.Motor(forward=backmotor1, backward=backmotor2, pwm=True)

    def moveForward(self, speed: float):
        # -1<=speed<=1
        if speed < 0:
            self.backmotor.backward(speed=-speed)
        else:
            self.backmotor.forward(speed=speed)
    
    def setFR(self, f: float, r: float):
        if abs(f) >= self.throttleMaxAfter:
            if f > 0:
                f = 1
            elif f < 0:
                f = -1
        if self.frontservoReverser:
            r = -r
        self.moveForward(speed=f)

    def cleanup(self):
        pass