from serial import Serial

def send(command):
    spec.write(('%s\n' % command).encode('utf-8'))
    spec.readlines()

#initialize instrument
spec = Serial('COM2', baudrate=9600, timeout=1) #need to know the name of the com port being used for the serial adaptor, need defult bodyrate since just powered on

spec.write('?K\n'.encode('utf-8'))  #\n and \r are line breaks, like pressing enter, need to know which one is needed or both 
print(spec.readlines())

#1s int and 1 avg
send('I1000')
# spec.write('I1000\n'.encode('utf-8'))
# print(spec.readlines()
send('A1')


spec.close()


