from machine import Pin, I2C
import i2c_lcd
import utime

dennis = I2C(0, scl=Pin(22), sda=Pin(23)) #what pins its attached to
devices = dennis.scan()
print(devices)

lcd = i2c_lcd.I2cLcd(dennis, 0x27, 2, 16) #device, address, and columns and rows of devices
lcd.clear() #clear screen

button = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
   if button.value() == 0:
        lcd.move_to(5, 0) #text location
        lcd.putstr('Access') #text to print
        lcd.move_to(5, 1) #text location
        lcd.putstr('granted')
        utime.sleep(3)
        lcd.clear()
   if button.value() == 1: #lockout followed by count down
        lcd.move_to(5, 0) #text location
        lcd.putstr('Access') #text to print
        lcd.move_to(5, 1) #text location
        lcd.putstr('Denied')
        utime.sleep(3)
        lcd.move_to(4, 0) #text location
        lcd.putstr('lockout') #text to print
        lcd.move_to(3, 1) #text location
        lcd.putstr('Initiated')
        utime.sleep(3)
        lcd.clear()
        lcd.move_to(7, 0)
        lcd.putstr('5')
        utime.sleep(1)
        lcd.move_to(7, 0)
        lcd.putstr('4')
        utime.sleep(1)
        lcd.move_to(7, 0)
        lcd.putstr('3')
        utime.sleep(1)
        lcd.move_to(7, 0)
        lcd.putstr('2')
        utime.sleep(1)
        lcd.move_to(7, 0)
        lcd.putstr('1')
        utime.sleep(1)
        lcd.move_to(7, 0)
        lcd.putstr('0')
        utime.sleep(1)
        lcd.clear()
   #else:
        #lcd.clear() #clear screen
    #utime.sleep(0.1) #check for button less often (0.1s) 