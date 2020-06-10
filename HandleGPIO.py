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
        piin = Pin(pin, GPIO.OUT)
        self.Pin = piin
        self.pulse = pulseClock # in Hz
        self.servo = GPIO.PWM(self.Pin.pin, self.pulse)
        self.start()

    def start(self, n = 0):
        self.servo.start(n)

    def setAngle(self, angle = 90):
        # angle in deg
        pass

pinsSetup()
rearMotorPin = Pin(7, GPIO.OUT)
frontServo = GPIO.PWM(11, 50)

def pinsCleanup():
    GPIO.cleanup()
