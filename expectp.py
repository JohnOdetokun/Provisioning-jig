#!/usr/bin/env python




import time
import getpass
import signal
import select

from button import Button
from lights import Lights
from open_ocd import OpenOCD
from tel_con import TelCon
#from my_file import MyClass



while True:
    with Button() as button:
        button.butpush()
            
        
        
        with Lights() as light:

            with OpenOCD() as openOCD:
            
                with TelCon() as telcon:
                    
                    telcon.halt()
                    telcon.erase()
                    telcon.load()
                    light.success()
    
    User = input("Press <enter> to exit or <spacebar> then <enter> to continue")
    if (User == ""):
        break

