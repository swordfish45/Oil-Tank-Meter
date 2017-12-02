import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BCM)

def signal_handler(signal,frame):
    print("exiting")
    GPIO.cleanup()
    sys.exit(0);

signal.signal(signal.SIGINT, signal_handler)

trig=23
echo=24

print "Distance Measurement In Progress"

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig,False)
print "waiting for sensor to settle"
time.sleep(2)

while(True):
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

    print "Distance:",distance,"in"

    time.sleep(1)

