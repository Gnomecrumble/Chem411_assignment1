import numpy as np
from matplotlib import pyplot 

pixel = [891, 1737, 297, 569, 1167, 1427, 738]
wavelength = [630, 712, 546, 587, 661, 678, 611]

pyplot.rc('font', size=9)

fig, ax =pyplot.subplots(2, 1)  # 2 rows, 1 column
ax[0].plot(pixel, wavelength, 'ro') #data, will plot calibration of pixel number to wavelength

#fitting
fit = np.polyfit(pixel, wavelength, 1) #x value, y value, order of polynomial gives [m,b] of mx+b, if given 3rd order polynomial would give [a, b, c, d] 
# print(fit) #used to finde the slope
xFine = range(2048) #list of 2048 numbers
y = np.polyval(fit, xFine) #([coefficents], x's) (gives the y's that correspond to the coefficent and x values)
ax[0].plot (xFine, y, 'k-', label = '1st order, slope = 0.112x') #plot xaxis,yaxis, 'line type colour', data point marker, and label 


fit2 = np.polyfit(pixel, wavelength, 2)
y2 = np.polyval(fit2, xFine)
ax[0].plot(xFine, y2, 'b-', label = '2nd order, slope = -2.89*10^-5 x^2 + 0.171 x')

fit3 = np.polyfit(pixel, wavelength, 3)
y3 = np.polyval(fit3, xFine)
ax[0].plot(xFine, y3, 'r-', label = '3rd order, slope =2.43*10^-8 x^3 + -1.02*10^-5 x^2 + 4.84 x')
ax[0].legend()

ax[0].set_xlabel('pixel number')
ax[0].set_ylabel('wavelength/nm')





# residuals
a, b = np.polyfit(pixel, wavelength, 1) #get the m and +b components 
e = np.array(pixel) #set as an array so can be multiplied by a non integer
predy = e*a +b #predicted values for 
# print(a, b) #check a and b values 
#print(predy) #check that values were calculated correctly
residuals = predy-wavelength
#print(residuals)
ressq = np.square(residuals) #square the residuals
#print(ressq)
sumrssq = sum(ressq) #sum the squares of the residual
#print(sumrssq)
ax[1].plot(pixel, residuals, 'ko', label = '1st order residuals, sum of squares =%d' %(sumrssq) )

a2, b2, c2 = np.polyfit(pixel, wavelength, 2) 
predy2 = np.square(e)*a2 +e*b2 +c2
print(a2, b2, c2)
residuals2 = predy2-wavelength
ressq2 = np.square(residuals2)
sumrssq2 = sum(ressq2)
print(sumrssq2)
ax[1].plot(pixel, residuals2, 'bo', label = '2nd order residuals, sum of squares = %d' %(sumrssq2) )

a3, b3, c3, d3 = np.polyfit(pixel, wavelength, 3) 
predy3 =  e*e*e*a3 +np.square(e)*b3 +e*c3 +d3
residuals3=predy3-wavelength
ressq3 = np.square(residuals3)
sumrssq3 = sum(ressq3)
print(sumrssq3)
ax[1].plot(pixel, residuals3, 'ro', label = '3rd order residuals, sum of squares = %d' %(sumrssq3) )

ax[1].legend()
ax[1].set_xlabel('pixel number')
ax[1].set_ylabel('residual/nm')

pyplot.axhline(0)

fig.set_tight_layout(True)
pyplot.show()

pyplot.savefig('411_ass5p1_and_2.png')

