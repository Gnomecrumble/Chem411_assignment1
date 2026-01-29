# Assignment 1 Part 1. Emily & Ollie
from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)

last_state = 1 # stores what button was doing when last checked, 1 since button starts unpressed
last_release_time = 0 #stores when the button was last released, used in time calculation

print("Ready! Press and hold the button") #just a message for user

while True:
    current_state = button.value()
    current_time = time.ticks_ms()

    # Button just pressed
    if current_state == 0 and last_state == 1:
        press_time = current_time

    # Button just released
    elif current_state == 1 and last_state == 0:
        duration = time.ticks_diff(current_time, press_time) # press time calculation

        if duration > 50:  # debounce
            if duration < 500:
                print(f"SHORT PRESS ({duration} ms)")
            else:
                print(f"LONG PRESS ({duration} ms)")

    last_state = current_state