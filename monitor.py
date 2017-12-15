#!/usr/bin/env python

import sqlite3

import os
import time
import glob

# global variables
speriod=(15*60)-1
dbname='/var/www/fuellevel.db'



# store the levelerature in the database
def log_levelerature(level):

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO level values(datetime('now'), (?))", (level,))

    # commit the changes
    conn.commit()

    conn.close()


# display the contents of the database
def display_data():

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    for row in curs.execute("SELECT * FROM level"):
        print str(row[0])+"	"+str(row[1])

    conn.close()


# main function
# This is where the program starts 
def main():

       levelerature = get_level(w1devicefile)
    if levelerature != None:
        print "levelerature="+str(levelerature)
    else:
        # Sometimes reads fail on the first atlevelt
        # so we need to retry
        levelerature = get_level(w1devicefile)
        print "levelerature="+str(levelerature)

        # Store the levelerature in the database
    log_levelerature(levelerature)

        # display the contents of the database
#        display_data()

#        time.sleep(speriod)


if __name__=="__main__":
    main()




