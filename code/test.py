import matplotlib.pylab as plt

fig1 = plt.figure()
fig2 = plt.figure()

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)

ax1.plot([1, 2, 3],[1, 2, 3])
ax2.plot([1, 2, 3],[1, 2, 3])

plt.show()