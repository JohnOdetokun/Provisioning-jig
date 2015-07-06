import RPi.GPIO as GPIO


class Button:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        

    def __enter__(self):
        return self

    def butpush(self):
        GPIO.wait_for_edge(11, GPIO.RISING)
        return False

    def __exit__(self, type, value, traceback):
        GPIO.cleanup()
