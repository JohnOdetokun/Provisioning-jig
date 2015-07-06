import pexpect
import time
import os
import sys
from lights import Lights
class OpenOCD:
    
    def __init__(self):
        self.c = Lights()
        try:
            
            self.ocd = pexpect.spawn("openocd -f interface/stlink-v2.cfg -f target/stm32f0x_stlink.cfg", timeout=3)
            openocd_start_state = self.ocd.expect(["Open On-Chip Debugger[\s\S]*hardware has 4 breakpoints, 2 watchpoints[\s\S]*","[\s\S]*Error: open failed[\s\S]*","[\s\S]*Error: couldn't bind to socket: Address already in use[\s\S]*"])
            if openocd_start_state == 0:
                print("On-Chip debugger opened")
            elif openocd_start_state == 1:
                print("openOCD failed")
                c.failed()
                sys.exit()
            elif openocd_start_state == 2:
                os.system("killall openocd")
                print("openocd already active.... Now closed, run program again")
                c.failed()
                sys.exit()

            else:
                c.failed()
                sys.exit()
        except:
            self.c.failed()
            sys.exit()


    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.ocd.sendcontrol('c')



        
