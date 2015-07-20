#!/usr/bin/env python

import logging
from button import Button
from lights import Lights
from open_ocd import OpenOCD
from tel_con import TelCon

if __name__ == '__main__':
    logging.basicConfig(format = "%(asctime)s:" + logging.BASIC_FORMAT)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    while True:
        try:
            with Lights(logger.getChild('lights')) as light:
                with Button(logger.getChild('button')) as button:
                    button.wait_for_button_press()
                    try:
                        with OpenOCD(logger.getChild('openocd')) as openOCD:
                            with TelCon(logger.getChild('telcon')) as telcon:
                                telcon.halt()
                                telcon.erase()
                                telcon.load()
                                light.success()
                    except Exception:
                        logging.warn("Provisioning failed")
                        light.failed()
        except Exception:
            logging.critical("Lights or Button initialisation failed")
