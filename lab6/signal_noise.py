import matplotlib.pyplot as plt
import numpy as np
x = [i for i in xrange(1000)]
y = [0 for i in xrange(1000)]
for i in xrange(500,1000):
    y[i]=1
mu, sigma = 0,0.1
noise = np.random.normal(mu, sigma, 1000)
for i in xrange(1000):
    y[i] = y[i]+noise[i]

y_after_mean_filter = y[:]
for i in xrange(100,1000):
    y_after_mean_filter[i]=sum(y[i-99:i+1])/100.

plt.plot(x,y,color = 'blue')
plt.plot(x,y_after_mean_filter,color = 'green')
plt.title("signal")
plt.show()
plt.close()
y_derivate = [ y[i]-y[i-1] for i in xrange(1,1000)]
y_after_mean_filter_derivate = [ y_after_mean_filter[i]-y_after_mean_filter[i-1] for i in xrange(1,1000)]
plt.plot(x[:-1],y_derivate,color = 'blue')
plt.plot(x[:-1],y_after_mean_filter_derivate,color = 'green')
plt.title("first order derivative")
plt.show()
plt.close()

plt.plot(x[200:-1],y_after_mean_filter_derivate[200:],color = 'green')
plt.show()
