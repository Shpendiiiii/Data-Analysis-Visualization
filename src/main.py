import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot([1, 2, 3, 4], [1, 4, 9, 16])
ax1.yaxis.set_major_locator(plt.MaxNLocator(nbins=10))


ax2 = fig.add_subplot(2, 2, 2)
ax2.plot([1, 2, 3, 4], [10, 20, 30, 40])

ax3 = fig.add_subplot(2, 2, 3)
ax3.scatter([1, 2, 3, 4], [100, 200, 300, 400])
plt.show()