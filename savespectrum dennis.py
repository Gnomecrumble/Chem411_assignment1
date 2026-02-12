from serial import Serial
import time
from matplotlib import pyplot

# function for command
def send(command):
    spec.write(('%s\n' % command).encode('utf-8'))
    spec.readlines()

#open serial port
spec = Serial('COM2', baudrate=115200, timeout=1)

#specify that was want ascii
send('a')
spec.write('K0\n'.encode('utf-8'))

#set integration time
send('I1000')

#set number of averages
send('A1')

#ask for the values of the 2048 pixels
spec.write('S\n'.encode('utf-8'))
time.sleep(2) #lets it sleep for the exposure time

spec.read(8) #reads 8 bytes
signal=[] 
for x in range(2048):  #continously giving values
    temp = spec.read(7) #reading 7 bytes for each pixel
    signal.append(float(temp.decode().strip())) #strip takes away special characters from string from both right and left
spec.close()

# get ready for plotting
pyplot.rc('font', size=8)
fig = pyplot.figure(figsize=(3.25, 2.25))
ax = fig.add_subplot()
pixels = range(1, 2049)

ax.plot(pixels, signal)
ax.set_xlabel('pixel number')
ax.set_ylabel('intensity / a.u.')

fig.set_tight_layout(True)
pyplot.savefig('Savespectrum.png', dpi=300)