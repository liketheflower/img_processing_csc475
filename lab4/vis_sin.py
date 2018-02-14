import math
import matplotlib.pyplot as plt
x = [-2*math.pi+4*math.pi*(_/2000.) for _ in xrange(2000)]
sin_y_f1 = [math.sin(x_) for x_ in x]
sin_y_f2 = [math.sin(2*x_) for x_ in x]
plt.plot(x,sin_y_f1)
plt.plot(x,sin_y_f2)
plt.show()
plt.close()

sin_y_a1 = [math.sin(x_) for x_ in x]
sin_y_a2 = [4*math.sin(x_) for x_ in x]
plt.plot(x,sin_y_a1)
plt.plot(x,sin_y_a2)
plt.show()

