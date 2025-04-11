import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(size=10000)
y = np.random.normal(size=10000)

plt.figure(figsize=(5, 4))
hist, xedges, yedges, image = plt.hist2d(x, y, bins=100, density=True, cmap='Blues')
plt.show()