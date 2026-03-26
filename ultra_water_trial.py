from machine import I2C, Pin, DAC
import time, i2c_lcd, hcsr04
from hcsr04 import HCSR04

ultra = HCSR04(trigger_pin=18, echo_pin=5)

while True:
    
    distance = ultra.distance_cm()
    print(distance)
    time.sleep(1)