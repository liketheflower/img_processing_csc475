# this is used to visulize the gaussian noise
import matplotlib.pyplot as plt
import numpy as np
x = [i for i in xrange(1000)]
mu, sigma = 0, 0.1
y = np.random.normal(mu, sigma, 1000)
print np.mean(y[:10]),np.mean(y[:100]),np.mean(y[:500]),np.mean(y[:1000]), 
plt.plot(x,y)
plt.show()

plt.close()
plt.hist(y, bins='auto')
plt.show()
