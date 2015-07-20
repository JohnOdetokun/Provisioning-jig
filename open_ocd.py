import pexpect
import logging
import os
from lights import Lights

class OpenOCDFailed(Exception):
    pass

class OpenOCD:    
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.ocd = pexpect.spawn("openocd -f interface/stlink-v2.cfg -f target/stm32f0x_stlink.cfg", timeout=3)
        openocd_start_state = self.ocd.expect([
                "Open On-Chip Debugger[\s\S]*hardware has 4 breakpoints, 2 watchpoints",
		"Error: open failed",
		"Error: couldn't bind to socket: Address already in use", 
		"init mode failed \(unable to connect to the target\)"
	])
        if openocd_start_state == 0:
            self.logger.info("On-Chip debugger opened")
        elif openocd_start_state == 1:
            self.logger.critical("openOCD failed")
            raise OpenOCDFailed()
        elif openocd_start_state == 2:
            os.system("killall openocd")
            self.logger.critical("openocd already active.... Now closed, run program again")
            raise OpenOCDFailed()
        elif openocd_start_state == 3:
            self.logger.critical("Unable to connect to target")
            raise OpenOCDFailed()
        else:
            self.logger.critical("Unexpected problem")
            raise OpenOCDFailed()
     
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.ocd.terminate()
        self.logger.info("OpenOCD terminated")
