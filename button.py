import RPi.GPIO as GPIO
import logging

class Button:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def __enter__(self):
        return self

    def wait_for_button_press(self):
        self.logger.debug("Waiting for button press")
        GPIO.wait_for_edge(11, GPIO.RISING)

    def __exit__(self, type, value, traceback):
        self.logger.debug("Button exit")
