import pexpect
import re
import sys
import telnetlib


class TelCon:
    def __init__(self):
        global tel
        tel = pexpect.spawn("telnet localhost 4444", timeout = 3)
        tel.expect("[\s\S]*\nConnected to localhost[\s\S]*")
        print("connected to telnet")

    def halt(self):
        tel.sendline("reset halt")
        tel.expect("[\s\S]*target halted[\s\S]*")
        print("halted")

    def erase(self):
        tel.sendline("flash erase_sector 0 0 0")
        tel.expect("[\s\S]*erased sectors[\s\S]*")
        print("erased")

    def load(self):
        tel.sendline("flash write_image erase /home/pi/Downloads/demo.elf")
        tel.expect("[\s\S]*wrote[\s\S]*from file[\s\S]*")

        tel.sendline("verify_image /home/pi/Downloads/demo.elf ")
        tel.expect("[\s\S]*verified[\s\S]*bytes in[\s\S]*")
        print("LOADED!")

    def __exit__(self):
        tel.send("exit")
