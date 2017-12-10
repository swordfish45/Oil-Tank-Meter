import RPi.GPIO as GPIO
import time
import signal
import sys
import statistics

trig=23
echo=24

def cleanup():
    GPIO.cleanup()

#
# Ctrl c handler
# 
def signal_handler(signal,frame):
    print("exiting")
    cleanup()
    sys.exit(0);

signal.signal(signal.SIGINT, signal_handler)

#
# Main
#
def initialize(debug=False):
    GPIO.setmode(GPIO.BCM)
    if (debug):
        print "Distance Measurement In Progress"

    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo,GPIO.IN)

    GPIO.output(trig,False)

    if (debug):
        print "waiting for sensor to settle"
    time.sleep(2)

#
# Return single sample
# Must be run after initialize, and cleanup must be run after
#
def get_sample(debug=False) :
    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)

    while GPIO.input(echo)==0:
        pulse_start=time.time()

    while GPIO.input(echo)==1:
        pulse_end=time.time()

    pulse_duration=pulse_end-pulse_start

    distance=pulse_duration * 17150 

    distance=distance * 0.3937

    distance=round(distance,2)

    if (debug):
        print "Distance:",distance,"in"
    return distance
        

def get_distance(debug=False):
    samples=[]
    initialize()

    for x in range (0,5):
        samples.append(get_sample(debug))
        time.sleep(0.1)
    if (debug):
        print samples
        print statistics.mean(samples)
        print statistics.stdev(samples)

    cleanup()


if __name__ == "__main__":
    get_distance()
