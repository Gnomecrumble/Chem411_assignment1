from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP) #atttatch to pin 14, Pin.IN = microcontroler receives input from the pin

last_state = 1
last_release_time = 0

# A flag to track if we have started yet
first_press_has_happened = False
print("Ready! Click once to start, then click again to see the gap")

while True:
    current_state = button.value()
    current_time = time.ticks_ms()
    
    if current_state == 0 and last_state == 1:
        
        if not first_press_has_happened:
            first_press_has_happened = True #fix this typed wrong...
            print('Timer Started! (waiting for next press)')
        else:
            gap = time.ticks_diff(current_time, last_release_time)
        
            if gap > 50:
                if gap< 500:
                    print(f"SHORT GAP ({gap}ms)")
                else:
                    print(f"LONG GAP ({gap}ms)")
    elif current_state == 1 and last_state == 0:
        last_release_time = current_time
    last_state = current_state
    