import random
N = 60000
#toss_coin_results = [random.random() for _ in range(N)]
#toss_coin_results = [0 for _ in range(N)]
toss_coin_results = []
for i in range(N):
    if random.random()>0.5:
        toss_coin_results.append(1.0)
    else: 
        toss_coin_results.append(-1.0)


target = random.random()
print("target is: ", target)
learning_rate =0.0001
tartget_updates =[target]
for i in range(N):
    if toss_coin_results[i]>tartget_updates[-1]:
        target_new = tartget_updates[-1]+learning_rate*abs(toss_coin_results[i]-tartget_updates[-1])
    else:
        target_new = tartget_updates[-1]-learning_rate*abs(toss_coin_results[i]-tartget_updates[-1])
    tartget_updates.append(target_new)
print(sum(toss_coin_results)/N-target) 
import matplotlib.pyplot as plt
plt.plot(range(N+1), tartget_updates)
plt.show()
