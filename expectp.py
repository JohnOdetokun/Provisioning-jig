#!/usr/bin/env python




import time
import getpass
import signal
import select
#from my_file import MyClass


OCDstatus = True
while True:
    from button import Button
    bu = Button()

    while bu.butpush():
        print("Button pushed")
        bu.clean()
    
    from lights import Lights
    c = Lights()
    
    if(OCDstatus):
        from open_ocd import OpenOCD
        a = OpenOCD()
        OCDstatus = False

        from tel_con import TelCon
        b = TelCon()
    b.halt()
    b.erase()
    b.load()
    c.success()
    
    
    User = input("Press<enter> to exit or <spacebar> then <enter> to continue")
    if (User == ""):
        break

c.clean()
