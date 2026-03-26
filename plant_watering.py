from machine import ADC, Pin
import time, hcsr04
from hcsr04 import HCSR04

# Soil moisture sensor on GPIO32 
soil_adc = ADC(Pin(32))
soil_adc.atten(ADC.ATTN_11DB)   
soil_adc.width(ADC.WIDTH_12BIT)

# Relay on GPIO25 (active LOW example)
relay = Pin(25, Pin.OUT)
relay.value(0)  # relay OFF at start (HIGH = OFF for active-LOW)

# read dry vs wet and pick a value between
DRY_THRESHOLD = 2500  # example: > 2500 = dry, < 2500 = wet

ultra = HCSR04(trigger_pin=18, echo_pin=5)

while True:
    moisture_raw = soil_adc.read()  # higher = drier
    print("Moisture raw:", moisture_raw)

    if moisture_raw > DRY_THRESHOLD:
        # soil is dry -> pump ON
        relay.value(1)  # active-LOW relay ON
        print("Pump ON")
    else:
        # soil is wet enough -> pump OFF
        relay.value(0)  # relay OFF
        print("Pump OFF")

    time.sleep(2)
