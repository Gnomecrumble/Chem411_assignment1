
from machine import Pin
from hid_services import Keyboard
import time 

Codes = {'a':0x04, 'b':0x05, 'c':0x06,'d':0x07, 'e':0x08, 'f':0x09} # creates a library of values, to use on of these us codes['b']

board = Keyboard('Grumpy_Goblin') #names the device grumpy goblij
board.start() #starts the bluetooth
board.get_device_name()
board.start_advertising() #starts advertising to connect
    #board.stop_advertising()
button = Pin(14, Pin.IN, Pin.PULL_UP)

#def __init__(self, letter):
    #self.letter = letter
    
#def __type__(letter):
 #   board.set_keys(Codes['letter'])
  #  board.notify_hid_report()
   # time.sleep(0.05)
    #board.set_keys()
    #board.notify_hid_report()
    #time.sleep(0.05)     

while True:
    if button.value() == 0:
        board.set_keys(Codes['d'])
        board.notify_hid_report()
        time.sleep(0.05)
        board.set_keys()
        board.notify_hid_report()
        time.sleep(0.05)
        board.set_keys(Codes['e'])
        board.notify_hid_report()
        time.sleep(0.05)
        board.set_keys()
        board.notify_hid_report()
        time.sleep(0.05)
        board.set_keys(Codes['f'])
        board.notify_hid_report()
        time.sleep(0.05)
        board.set_keys()
        board.notify_hid_report()
        time.sleep(0.05)
    else:
        pass
    time.sleep(0.05)
    
    
    
    
    
    
    
    