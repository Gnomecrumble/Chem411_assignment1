#scl yellow to pin 23, sda oragange pin 22
#trip purp to pin 18, echo green to pin 5
#Vio to pin 12
from machine import I2C, Pin, DAC
import time, i2c_lcd, hcsr04
from hcsr04 import HCSR04


i2c = I2C(0, scl=Pin(23), sda=Pin(22)) # setup the I2C connection 

buzzer = Pin(12,Pin.OUT) #set buzzer Pin
buzzer.value(1) #set buzzer off


lcd = i2c_lcd.I2cLcd(i2c, 0x27, 2, 16) # Format: (I2C Object, Address, Rows, Columns)

ultra = HCSR04(trigger_pin=18, echo_pin=5)

button = Pin(4, Pin.IN, Pin.PULL_UP)

distance_max = 0
distance_min = 250
distance = ultra.distance_cm()
time.sleep(1)
lcd.clear()

while True:
    lcd.move_to(0,0)
    lcd.putstr('                ') #clear only line 1
    distance = ultra.distance_cm() #print distance in cm
    current_state = button.value()

    lcd.move_to(0, 0)       # write on Line 1
    lcd.putstr(str(distance))
    if current_state == 0:
        distance_max = 0
        distance_min = 250
        
        
    if distance > distance_max:
        distance_max = distance
        lcd.move_to(0, 1) #write on line 2
        lcd.putstr('Max:%.1f' %(distance_max))
    
    if distance < distance_min:
        distance_min = distance
        lcd.move_to(8, 1) #write on line 2
        lcd.putstr('Min:%.1f'%(distance_min))
    
    
   
    if distance> 10: #distance over which no alarm
        buzzer.value(1)
    else:   #alarm sounds under 10 cm
        buzzer.value(0) #turn on buzzer
        time.sleep(0.1) #leave buzzer on for quick chirp then shutoff for sanity sake
        buzzer.value(1)
    time.sleep(1)
    