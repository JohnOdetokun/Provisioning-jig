import pexpect
import re
import sys
import telnetlib
from lights import Lights

class TelCon:
    def __init__(self):
        self.c= Lights()
        self.tel = pexpect.spawn("telnet localhost 4444", timeout = 3)
        telcon_start = self.tel.expect(["[\s\S]*\nConnected to localhost[\s\S]*", "[\s\S]unable to[\s\S]"])
        if telcon_start == 0:
            print("connected to telnet")
        else:
            self.c.failed()
            sys.exit()

    def __enter__(self):
        return self
    
    def halt(self):
        self.tel.sendline("reset halt")
        self.tel.expect("[\s\S]*target halted[\s\S]*")
        print("halted")

    def erase(self):
        self.tel.sendline("flash erase_sector 0 0 0")
        self.tel.expect("[\s\S]*erased sectors[\s\S]*")
        print("erased")

    def load(self):
        self.tel.sendline("flash write_image erase /home/pi/Downloads/demo.elf")
        #self.tel.sendline("flash write_image erase /media/TRANSCEND/debug/DFU_ST-Link-V2.hex")
        self.tel.expect("[\s\S]*wrote[\s\S]*from file[\s\S]*")

        self.tel.sendline("verify_image /home/pi/Downloads/demo.elf ")
        #self.tel.sendline("verify_image /media/TRANSCEND/debug/DFU_ST-Link-V2.hex")
        self.tel.expect("[\s\S]*verified[\s\S]*bytes in[\s\S]*")
        print("LOADED!")

    def __exit__(self, type, value, traceback):
        self.tel.send("exit")
