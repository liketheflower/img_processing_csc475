#x===
#y=e^(-x^2/2)
import math
import matplotlib.pyplot as plt
def get_y(x,sigma = 1.0):
    return math.exp(-x**2/2.0*sigma)

x,y=[],[]

for i in xrange(-400,400):
    tem_x = i/100.0
    x.append(tem_x)
    y.append(get_y(tem_x))

plt.plot(x,y)
plt.show()

