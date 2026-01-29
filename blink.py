from time import sleep_ms
from machine import Pin

led=Pin(2,Pin.OUT) #create LED object from pin2, Set Pin 2 to output 
while True:
        led.value(1) # Set led turn on
        sleep_ms(500)
        led.value(0) #Set led turn off 
        sleep_ms(100)
        