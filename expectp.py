#!/usr/bin/env python

import pexpect
import RPi.GPIO as GPIO
import re
import os
import sys
import time
import telnetlib
import getpass
import signal
import select
#from my_file import MyClass
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,0)
OCDstatus = True
while True:
    GPIO.wait_for_edge(11, GPIO.RISING)
    GPIO.output(7, GPIO.input(11))
    if(OCDstatus):
        from open_ocd import OpenOCD
        a = OpenOCD()
        OCDstatus = False


    tel = pexpect.spawn("telnet localhost 4444", timeout = 3)
    tel.expect("[\s\S]*\nConnected to localhost[\s\S]*")
    print("connected to telnet")

    tel.sendline("reset halt")
    tel.expect("[\s\S]*target halted[\s\S]*")
    print("halted")

    tel.sendline("flash erase_sector 0 0 0")
    tel.expect("[\s\S]*erased sectors[\s\S]*")
    print("erased")

    tel.sendline("flash write_image erase /home/pi/Downloads/demo.elf")
    tel.expect("[\s\S]*wrote[\s\S]*from file[\s\S]*")

    tel.sendline("verify_image /home/pi/Downloads/demo.elf ")
    tel.expect("[\s\S]*verified[\s\S]*bytes in[\s\S]*")

    print("LOADED!")

    #close telnet
    tel.send("exit")
    User = raw_input("Press<enter> to exit or <spacebar> then <enter> to continue")
    if (User == ""):
        break
        

GPIO.cleanup()
