import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 20 #fehér kábel
GPIO_ECHO = 21 #szürke kábel

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    print ("Mérés indul!")
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()


    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    
    TimeElapsed = StopTime - StartTime

    distance = (TimeElapsed * 34000) / 2
    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Mért távolság = %.1f cm" % dist)
            time.sleep(1)

    except KeyboardInterrupt:
        print("A mérés megszakadt, leáll")

GPIO.cleanup()


















