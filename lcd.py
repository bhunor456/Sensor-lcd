#lcd kijelző
#from RPLCD import CharLCD
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LCD1_E = 4 #7-es GPIO láb, Enable
LCD2_RS = 27 # 36-os GPIO láb, RS
LCD2_D4 = 17 #11-es GPIO láb, D4
LCD3_D5 = 27 #13-as GPIO lán, D5
LCD4_D6 = 22 #16-os GPIO láb, D6
LCD5_D7 = 5 #18-as GPIO láb, D7

#HC-SR04 szenzor
ECHO = 20 # echo, GPIO 20-as láb
TRIG = 21 #trig, GPIO, 21-es láb

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


print("Mérésre készen!")


GPIO.output(GPIO_TRIGGER, True)

time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)

   
while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time

pulse_duration = pulse_end - pulse_start 

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Távolság:",distance,"cm")

#HC_SR-04 szenzor


LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xcC

E_PULSE = 0.0005
E_DELAY = 0.0005

def main():
    GPIO.setup(LCD1_E,GPIO.OUT)
    GPIO.setup(LCD2_RS,GPIO.OUT)
    GPIO.setup(LCD3_D4,GPIO.OUT)
    GPIO.setup(LCD4_D5,GPIO.OUT)
    GPIO.setup(LCD5_D6,GPIO.OUT)
    GPIO.setup(LCD6_D7,GPIO.OUT)

lcd_init()

while True:
    lcd_string("Raspberry Pi3 model B",LCD_LINE_1)


#lcd = CharLCD(cols=16, rows=2, pin_rs=27, pin_e=4, pins_data=[17, 27, 22, 5])
def main():
    lcd_init()
    GPIO.output(LED_ON, True)
    time.sleep(0.001)
    GPIO.output(LED_ON, False)
    time.sleep(0.001)
    GPIO.output(LED_ON, True)
    time.sleep(0.001)

    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string("zsáámóóó",2)
    lcd_byte(LCD_LINE_2, LCD_CMD)
    lcd_string("zsámóózsá",2)

    time.sleep(3)

    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string("Szevasz baszdmeg!",1)
    lcd_byte(LCD_LINE_2, LCD_CMD)
    lcd_string("Mi a hányás?",1)

    time.sleep(3)

    lcd_byte(LCD_LINE_1, LCD_CMD)
    lcd_string("ásztálálibombá",3)
    lcd_byte(LCD_LINE_2, LCD_CMD)
    lcd_string("miivaaaaan",3)
    #GPIO.setup()
    #GPIO.setup()

    time.sleep(30)

    GPIO.output(LED_ON, False)


lcd_byte(0x33,LCD_CMD)
lcd_byte(0x33,LCD_CMD)
lcd_byte(0x28,LCD_CMD)
lcd_byte(0x0C,LCD_CMD)
lcd_byte(0x06,LCD_CMD)
lcd_byte(0x01,LCD_CMD)

def lcd_string(message,style)

#style1 = jobbra igazítás
#style2 = középre igazítás
#style3 = balra igazítás

if style === 1:
message = message.ljust(LCD_WIDTH," ")
elif === 2:
message = message.center(LCD_WIDTH," ")
elif === 3:
message = message.rjust(LCD_WIDTH," ")

for i in range (LCD_WIDTH):
    lcd_byte(ord(message[i]).LCD_CHR)

def lcd_byte(bits, mode):

#byte-ok küldése az adat pinekre
#bitek = adatok
#mód(mode): karakterekre IGAZ, parancsokra HAMIS

GPIO.output(LCD_RS, mode):

GPIO.output(LCD_D4, False)
GPIO.output(LCD_D5, False)
GPIO.output(LCD_D6, False)
GPIO.output(LCD_D7, False)

if bits&0x10==0x10:
    GPIO.output(LCD_D4,True)
    GPIO.output(LCD_D5,True)
    GPIO.output(LCD_D6,True)
    GPIO.output(LCD_D7,True)



GPIO.cleanup()
