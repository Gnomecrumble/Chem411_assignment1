import machine
from machine import I2C, Pin
import i2c_lcd
import time

# setup the I2C connection with SDA = GPIO 21, SCL = GPIO 22
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# find the I2C device address
devices = i2c.scan()
print(devices)
print(hex(devices[0]))

# Format: (I2C Object, Address, Rows, Columns)
lcd = i2c_lcd.I2cLcd(i2c, 0x27, 2, 16)

# clear the screen
lcd.clear()
        
# write some text on line 1
lcd.move_to(0, 0)       # Line 1
lcd.putstr('CHEM 411/511/560')
        
# write some text on line 2
lcd.move_to(0, 1)
lcd.putstr('ESP32 + LCD')
count = 0
while True:
    lcd.move_to(12, 1) 
    lcd.putstr(str(count))
    count += 1
    time.sleep(1)