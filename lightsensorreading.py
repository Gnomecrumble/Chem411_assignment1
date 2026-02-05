from machine import Pin, ADC, I2C
import i2c_lcd, time

i2c_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(i2c_device, 0x27, 2, 16)
lightsensor = ADC(Pin(34))
lightsensor.ATTN_11DB


while True:
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('light: %d' %(4095-lightsensor.read()))
    time.sleep (0.5)