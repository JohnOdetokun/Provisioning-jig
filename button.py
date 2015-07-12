import RPi.GPIO as GPIO


class Button:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.mode = 0;

    def __enter__(self):
        return self

    def butpush(self):
        try:
            GPIO.wait_for_edge(11, GPIO.RISING)

        except KeyboardInterrupt:
            with Lights as light:
                light.failed()

    def __exit__(self, type, value, traceback):
        GPIO.cleanup()
