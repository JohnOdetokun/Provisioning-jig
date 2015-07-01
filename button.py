import RPi.GPIO as GPIO


class Button:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        

    def butpush(self):
        GPIO.wait_for_edge(11, GPIO.RISING)
        return False

    def clean(self):
        GPIO.cleanup()
