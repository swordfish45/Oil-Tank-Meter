#!/usr/bin/env python

import sqlite3

import os
import time
import glob
import logger
import sensor

# global variables
tank_height=44



# main function
# This is where the program starts 
def main():

    s = sensor.sensor()
    dist = s.get_distance()
    level = tank_height - dist

    if level != None:
        print "level="+str(level)
        logger.log_level(level)
    else:
        print "Error in monitor. Failed to get level"


if __name__=="__main__":
    main()




