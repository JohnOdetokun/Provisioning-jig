import RPi.GPIO as GPIO
import time
import logging

class Lights:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13,GPIO.OUT)
        #success LED
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7,0)
        #Busy LED
        GPIO.setup(12,GPIO.OUT)
        GPIO.output(12,0)
        #fail LED
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,0)
        self.logger.info("LEDS initialised")

    def __enter__(self):
        return self

    def busy(self):
        GPIO.output(12,1)

    def busyOff(self):
        GPIO.output(12,0)

    def success(self):
        for _ in range(6):
            GPIO.output(7,1)
            time.sleep(0.3)
            GPIO.output(7,0)
            time.sleep(0.3)
        self.logger.info("Flashed success LED")

    def failed(self):
        for _ in range(6):
            GPIO.output(13,1)
            time.sleep(0.3)
            GPIO.output(13,0)
            time.sleep(0.3)
        self.logger.info("Flashed failed LED")

    def __exit__(self, type, value, traceback):
        self.logger.info("lights exited")
        GPIO.cleanup()
