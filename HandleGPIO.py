import time
import RPi.GPIO as GPIO

def pinsSetup():
    GPIO.setmode(GPIO.BOARD)

class Pin:
    def __init__(self, boardPinNum: int, IO):
        self.pin = boardPinNum
        self.IO = IO
        GPIO.setup(self.pin, self.IO)

class Servo:
    def __init__(self, pin: int, pulseClock):
        self.Pin = Pin(pin, GPIO.OUT)
        self.pulse = pulseClock # in Hz
        self.servo = GPIO.PWM(self.Pin.pin, self.pulse)
        self.start()

    def start(self, n = 0):
        self.servo.start(n)

    def setAngle(self, angle = 90.0):
        # angle in deg, between 0 and 180
        self.servo.ChangeDutyCycle(2+(angle/18))

    def stop(self):
        self.servo.stop()

    def stopMoving(self):
        self.servo.ChangeDutyCycle(0)

class Motor:
    def __init__(self, enablePin, pin1, pin2):
        self.enablePin = Pin(enablePin, GPIO.OUT)
        self.pin1 = Pin(pin1, GPIO.OUT)
        self.pin2 = Pin(pin2, GPIO.OUT)
    
    def enableDisable(self, tOrF):
        self.enablePin

def pinsCleanup():
    GPIO.cleanup()
