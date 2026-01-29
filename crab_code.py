from machine import Pin, I2C
import i2c_lcd #importing premade code

dennis = I2C(0, scl=Pin(22), sda=Pin(23))
devices = dennis.scan()
print(devices)

lcd = i2c_lcd.I2cLcd(dennis, 0x27, 2, 16) #telling it the device, address, number of rows, number of columns
lcd.clear() #clear the screen

lcd.move_to(1,0) #moves things (column, row)
lcd.putstr('(._.)') #writes things
lcd.move_to(2,1) #moves things (column, row)
lcd.putstr('^ ^') #writes things




