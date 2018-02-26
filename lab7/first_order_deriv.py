import matplotlib.pyplot as plt
# y =x**2
# y' = 2*x
import math
x = [(i-500)/500 for i in xrange(1000)]
y= [math.exp(x_) for x_ in x]
y_deriv = [(y[i]-y[i-1])/(1/500.) for i in xrange(1,1000)]
print y_deriv[-10:]
plt.plot(x,y)
plt.show()
plt.close()

plt.plot(x[1:],y_deriv)
plt.show()
