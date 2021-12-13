import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,4096,0.1)
y = 1 - (1 - (1/ x)) ** x

plt.ylim([0.5, 1])

plt.title("Sirakami Pain Peko")
plt.xlabel('Akai na...')
plt.ylabel('Gold Koiking')

plt.minorticks_on()
plt.grid(which="major", color="black", alpha=0.5)
plt.grid(which="minor", color="gray", linestyle=":")
plt.plot(x, y, c='blue')
plt.show()