#!/usr/bin/env python

import sys
import time
import RPi.GPIO as io
import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format('/home/pi/', 'pir2.log')),
        logging.StreamHandler()
    ])

io.setmode(io.BCM)
SHUTOFF_DELAY = 60 # seconds
PIR_PIN = 24       # 23 originally


def main():
    io.setup(PIR_PIN, io.IN)
    turned_off = False
    last_motion_time = time.time()
    logger = logging.getLogger()
    logger.info("set up IR")
    subprocess.call("bash /home/pi/ga_on.sh", shell=True)

    while True:
        if io.input(PIR_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
                logger = logging.getLogger()
                logger.info("turned on")
        else:
            if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
                turned_off = True
                turn_off()
                logger = logging.getLogger()
                logger.info("turned off")
        time.sleep(.1)

def turn_on():
    logger = logging.getLogger()
    logger.info("turning on")
    subprocess.call("bash /home/pi/monitor_on.sh", shell=True)

def turn_off():
    logger = logging.getLogger()
    logger.info("turning off")
    subprocess.call("bash /home/pi/monitor_off.sh", shell=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()
