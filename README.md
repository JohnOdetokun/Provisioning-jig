# Provisioning-jig
Provisioning-jig for stm32F0 type.
Initially created to be used by second year Electrical Engineering students at the University of Cape Town.
Raspberry pi is connected to hardware that is connected to the chip. A push button (button.py) sends a signal to the main.py program which initiates the process of loading code onto the chip.

telcon.py - Establishes a telnet connection which is used to erase and write the chip
open_ocd.py - Establishes a connection with the debugger
lights.py - Display green if loading was successful and red if loading failed.
