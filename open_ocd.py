import pexpect
import time
import os
import sys

class OpenOCD:
    
    def __init__(self):
        from lights import Lights
        c = Lights()
        self.ocd = pexpect.spawn("openocd -f interface/stlink-v2.cfg -f target/stm32f0x_stlink.cfg", timeout=3)
        test1 = self.ocd.expect(["Open On-Chip Debugger[\s\S]*hardware has 4 breakpoints, 2 watchpoints[\s\S]*","[\s\S]*Error: open failed[\s\S]*","[\s\S]*Error: couldn't bind to socket: Address already in use[\s\S]*"])
        if test1 == 0:
            print("On-Chip debugger opened")
        elif test1 == 1:
            print("openOCD failed")
            c.failed()
            sys.exit()
        elif test == 2:
            os.system("sudo killall openocd")
            print("openocd already active.... Now closed, run program again")
            c.failed()
            sys.exit()

        else:
            c.failed()
            sys.exit()

    def __exit__(self):
        #close openocd
        time.sleep(3)
        self.ocd.sendcontrol('c')
        self.ocd.kill()


        
