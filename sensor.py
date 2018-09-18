import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 20 #fehér kábel
ECHO = 21 #szürke kábel


print("Mérésre készen!")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print("Mérés indul!")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print ("Távolság:",distance,"cm")
time.sleep(2)

GPIO.cleanup()


















