import RPi.GPIO as GPIO
import time

class Lights:
    def __enter__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(13,GPIO.OUT)
        #success LED
        GPIO.setup(7,GPIO.OUT)
        GPIO.output(7,0)

        #Busy LED
        GPIO.setup(13,GPIO.OUT)
        GPIO.output(13,1)
        #fail LED
        GPIO.setup(12,GPIO.OUT)
        GPIO.output(12,0)

        

    

    def success(self):
        GPIO.output(7,1)
        time.sleep(1)
        GPIO.output(7,0)
        time.sleep(1)
        GPIO.output(7,1)
        time.sleep(2)
        GPIO.output(7,0)
        

    def failed(self):
        GPIO.output(12,1)
        time.sleep(1)
        GPIO.output(12,0)
        time.sleep(1)
        GPIO.output(12,1)
        time.sleep(2)
        GPIO.cleanup()

    def clean(self):
        GPIO.cleanup()

    def __exit__(self, type, value, traceback):
        GPIO.cleanup()


        
