# Assignment 1 Part 2. Emily & Ollie
from machine import Pin, I2C
import time
import i2c_lcd
from time import sleep_ms

# Setup
screen = I2C(0, scl=Pin(23), sda=Pin(22))
led=Pin(2,Pin.OUT)
lcd = i2c_lcd.I2cLcd(screen, 0x27, 2, 16) #telling it the device, address, number of rows, number of columns
button = Pin(4, Pin.IN, Pin.PULL_UP)

Secret_Message = ['L', 'S', 'S' ,'S' ,'L'] # specify correct code to unlock the vault
input_code = []
reset_delay = 3000 # 3 seconds
input_active = False # not pressing button to enter a code

last_state = 1 # stores what button was doing when last checked, 1 since button starts unpressed
press_time = 0
last_release_time = 0 #stores when the button was last released, used in time calculation

def show_home(): # function that returns to/displays "home screen" message 
    lcd.clear()
    lcd.putstr("Enter Code")
    lcd.move_to(0, 1)
    lcd.putstr("To Unlock")

def blink_led(times): # function that blinks led
    for _ in range(times):
        led.value(1)
        time.sleep_ms(300)
        led.value(0)
        time.sleep_ms(300)
show_home() # start with fist message display

while True:
    current_state = button.value() 
    current_time = time.ticks_ms()

    # Button just pressed
    if current_state == 0 and last_state == 1:
        press_time = current_time
   
    # Button just released
    elif current_state == 1 and last_state == 0:
        duration = time.ticks_diff(current_time, press_time)
        lcd.clear()
        if duration > 50:  # debounce
            if duration < 500:
                input_code.append('S') #short press threshold
            else:
                input_code.append('L') #long press
            input_active = True # currently typing code (able to timeout)
            lcd.putstr(input_code) #display code as it is inputted
        
        if len(input_code) == len(Secret_Message): #when code reaches correct length 
            if input_code == Secret_Message: #code is correct
                lcd.clear()
                lcd.putstr('Vault Unlocked')
                input_active = False
                sleep_ms(3000)
                lcd.clear()
                input_code = []
            
            else: #code is incorecct 
                lcd.clear()
                lcd.putstr("Access Denied")
                blink_led(3) # runs LED function
                lcd.clear()
                lcd.move_to(4, 0) 
                lcd.putstr('Lockout') 
                lcd.move_to(3, 1) 
                lcd.putstr('Initiated')
                time.sleep(3)
                lcd.clear()
                for i in range(5, 0, -1): # count down until try again
                    lcd.clear()
                    lcd.move_to(7, 1)
                    lcd.putstr(f"{i} ")
                    time.sleep(1)
                input_code = []
                input_active = False 
                show_home() # reset back to first message aka "home screen"
        # Save last release time
        last_release_time = current_time

    # Reset input if too much time has passed since last button release
    elif input_active and time.ticks_diff(current_time, last_release_time) > reset_delay:
        lcd.clear()
        lcd.putstr("Timeout!")
        input_code = []
        input_active = False
        sleep_ms(3000)
        show_home()
        
    last_state = current_state #reset
