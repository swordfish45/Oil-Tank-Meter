import RPi.GPIO as GPIO
import time
import signal
import sys
import statistics

class sensor:

    #
    # Ctrl c handler
    # 
    def signal_handler(signal,frame):
        print("exiting")
        cleanup()
        sys.exit(0);

    signal.signal(signal.SIGINT, signal_handler)


    def cleanup(self):
        GPIO.cleanup()

    #
    # Main
    #
    def initialize(self,debug=False):
        GPIO.setmode(GPIO.BCM)
        if (debug):
            print "Distance Measurement In Progress"

        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo,GPIO.IN)

        GPIO.output(self.trig,False)

        if (debug):
            print "waiting for sensor to settle"
        time.sleep(2)

    def __init__(self):
        self.trig=23
        self.echo=24
        self.initialize()

    def __del__(self):
        self.cleanup()

    #
    # Return single sample
    # Must be run after initialize, and cleanup must be run after
    #
    def get_sample(self,debug=False) :
        GPIO.output(self.trig,True)
        time.sleep(0.00001)
        GPIO.output(self.trig,False)

        while GPIO.input(self.echo)==0:
            pulse_start=time.time()

        while GPIO.input(self.echo)==1:
            pulse_end=time.time()

        pulse_duration=pulse_end-pulse_start

        distance=pulse_duration * 17150 

        distance=distance * 0.3937

        distance=round(distance,2)

        if (debug):
            print "Distance:",distance,"in"
        return distance
            

    def get_distance(self,debug=False):
        samples=[]
        #initialize()

        for x in range (0,5):
            samples.append(self.get_sample(debug))
            time.sleep(0.1)

        m = statistics.mean(samples)
        std = statistics.stdev(samples)
        if (debug):
            print samples
            print m
            print std
        if (std < 1.0) :    
            return m
        else:
            print "Error: sample invalid, std", std
        #cleanup()


#    if __name__ == "__main__":
#        get_distance()
