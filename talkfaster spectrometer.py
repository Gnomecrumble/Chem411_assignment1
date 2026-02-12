from serial import Serial

spec = Serial('COM2', baudrate=9600, timeout=1)
spec.write('K0\n'.encode('utf-8'))
print(spec.readlines())
spec.close()