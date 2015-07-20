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
        GPIO.output(12,1)
        #fail LED
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,0)
        self.logger.info("LEDS initialised")

    def __enter__(self):
        return self

    def success(self):
        GPIO.output(7,1)
        time.sleep(2)
        GPIO.output(7,0)
        time.sleep(1)
        self.logger.info("Flashed success LED")

    def failed(self):
        GPIO.output(13,1)
        time.sleep(2)
        GPIO.output(13,0)
        time.sleep(1)
        self.logger.info("Flashed failed LED")

    def __exit__(self, type, value, traceback):
        self.logger.info("lights exited")
        GPIO.cleanup()
