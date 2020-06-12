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
    def __init__(self, fwPin: int, speedPin: int):
        self.fwPin = Pin(fwPin, GPIO.OUT)
        self.speedPin = Pin(speedPin, GPIO.OUT)


pinsSetup()
# rearMotorPin = Pin(7, GPIO.OUT)
frontServo = Servo(11, 50)

def pinsCleanup():
    GPIO.cleanup()

def setMotion(frState):
    setRtLtMotion(frState["r"])
    setFdBkMotion(frState["f"])

def setFdBkMotion(fFloat):
    pass

def setRtLtMotion(rFloat):
    pass
