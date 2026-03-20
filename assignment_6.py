from machine import Pin, I2C, ADC
import i2c_lcd, time

# SETUP

# LCD
screen = I2C(0, scl=Pin(22), sda=Pin(21))
lcd = i2c_lcd.I2cLcd(screen, 0x27, 2, 16)

# Light sensor
lightsensor = ADC(Pin(34))
lightsensor.atten(ADC.ATTN_11DB)

# Rotary encoder pins
Sw1 = Pin(26, Pin.IN, Pin.PULL_UP) 
Sw2 = Pin(25, Pin.IN, Pin.PULL_UP)

# Encoder push button
button = Pin(23, Pin.IN, Pin.PULL_UP)
button_last = button.value()
button_last_change = time.ticks_ms()

# LEDs
led_b = Pin(13, Pin.OUT)   # above MAX
led_a = Pin(14, Pin.OUT)   # below MIN

# Thresholds
MIN_val = 0       # dark limit
MAX_val = 4095    # bright limit

# Encoder state
mode = "MIN"
last_b = Sw2.value()


#FUNCTIONS

#read lightsensor
def read_brightness():
    raw = lightsensor.read()
    return 4095 - raw          # 0 = darkest, 4095 = brightest

# check if encoder has moved and update mode and lcd
def update_mode_and_lcd(last_b, mode):

    b = Sw2.value()
    if last_b == 1 and b == 0:
        a = Sw1.value()
        if a == 1:
            mode = "MIN"        # one direction
        else:
            mode = "MAX"        # other direction

    lcd.move_to(0, 1)
    if mode == "MIN":
        lcd.putstr("[MIN]  MAX ")
    else:
        lcd.putstr(" MIN  [MAX] ")

    return b, mode #return to update for next loop

#draw bar on 1-16 scale and update if max or min val is updated
def draw_bar(MIN_val, MAX_val):
    brightness = read_brightness()  # read level

    # LED on if outside range
    led_b.value(1 if brightness < MIN_val or brightness > MAX_val else 0)

    # if vaue is outside range, set to max or min
    if brightness < MIN_val:
        brightness = MIN_val
    elif brightness > MAX_val:
        brightness = MAX_val

    span = MAX_val - MIN_val or 1

    #calculate how many bars to display
    position = (brightness - MIN_val) / span 
    bars = int(position * 16)                  

    #display bars and add spaces so they will clear as it updates
    bar_str = "-" * bars + " " * (16 - bars)
    lcd.move_to(0, 0)
    lcd.putstr(bar_str)

# press button to store new min or max depending on the mode
def change_level(button_last, button_last_change, mode, MIN_val, MAX_val):
    now = time.ticks_ms()
    val = button.value()
    if val != button_last and time.ticks_diff(now, button_last_change) > 50: #debounce
        button_last_change = now
        button_last = val
        if val == 0:  # pressed
            brightness = read_brightness()
            if mode == "MIN":
                MIN_val = brightness #update min
            else:
                MAX_val = brightness #update max

    return button_last, button_last_change, MIN_val, MAX_val


while True:
    last_b, mode = update_mode_and_lcd(last_b, mode)
    button_last, button_last_change, MIN_val, MAX_val = change_level(
        button_last, button_last_change, mode, MIN_val, MAX_val
    )
    draw_bar(MIN_val, MAX_val)
    time.sleep_ms(5)

