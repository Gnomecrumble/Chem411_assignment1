from machine import Pin, ADC, I2C
import i2c_lcd, time


# setup for devices
i2c_device = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(i2c_device, 0x27, 2, 16)
lightsensor = ADC(Pin(34))
lightsensor.ATTN_11DB #device. attenuation ammount
led = Pin(12, Pin.OUT)

while True:
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr('light: %d' %(4095-lightsensor.read())) #light sensor reading on scree just to see #"x: (printed directly) %d" (interger placeholder) %xxxxxx (specifices the interger to fill into %d)
    time.sleep (0.5)
    if (4095-lightsensor.read())<2000: #light value to cause light to turn on
        led.value(1)
    else:
        led.value(0)