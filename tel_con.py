import pexpect
import logging

class TelConFailed(Exception):
    pass

class TelCon:
    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger
        logging.basicConfig(level=logging.DEBUG)
        self.tel = pexpect.spawn("telnet localhost 4444", timeout = 3)
        telcon_start = self.tel.expect([
            "Connected to localhost", 
            "unable to"
        ])
        if telcon_start == 0:
            self.logger.info("connected to telnet")
        else:
            raise TelConFailed()

    def __enter__(self):
        return self
    
    def halt(self):
        self.tel.sendline("reset halt")
        self.tel.expect_exact("target halted")
        self.logger.info("halted")

    def erase(self):
        self.tel.sendline("flash erase_sector 0 0 0")
        self.tel.expect_exact("erased sectors")
        self.logger.info("erased")

    def load(self):
        self.tel.sendline("flash write_image erase /root/workspace/Provisioning-jig/demo_2015.elf")
        self.tel.expect("wrote[\s\S]*from file")
        self.tel.sendline("verify_image /root/workspace/Provisioning-jig/demo_2015.elf")
        self.tel.expect("verified[\s\S]*bytes in")
        self.logger.info("Loaded and verified")

    def __exit__(self, type, value, traceback):
        self.tel.terminate()
        self.logger.info("Telnet connection terminated")
