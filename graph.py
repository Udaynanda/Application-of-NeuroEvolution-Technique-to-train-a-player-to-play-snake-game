from snake1 import fitness
from matplotlib import pyplot as plt
fitness = [50,80,100,120,140,160, 180,200]
gen =     [20,15,26, 29, 46, 116,125, 195]
plt.plot(fitness,gen)

plt.legend()
plt.xlabel("fitness")
plt.ylabel("generation")
plt.show()