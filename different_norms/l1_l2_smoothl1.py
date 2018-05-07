import matplotlib.pyplot as plt

x = [_*0.001 for _ in range(3000)]
l1 = [abs(_) for _ in x]
l2 = [_**2 for _ in x]
smooth_l1 =[]
for i in range(len(x)):
    if x[i]<1:
        smooth_l1.append(0.5*x[i]**2)
    else:
        smooth_l1.append(abs(x[i])-0.5)

plt.plot(x, l1, c ='red')
plt.plot(x, l2, c ='blue')
plt.plot(x, smooth_l1, c ='green')
plt.show()
