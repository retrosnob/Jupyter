import matplotlib.pylab as pylab

# This is LV that is spelt out in 4.34 and 4.35


def initialize():
    global r, d, b, c, K, x, y, resultx, resulty, t, timesteps
    r = d = c = b = 1
    K = 5
    x = y = 1
    resultx = [x]
    resulty = [y]
    t = 0
    timesteps = [t]

def update():
    global r, d, b, c, x, y, K, resultx, resulty, t, timesteps
    nextx = x + r * x * (1 - x/K) - (1 - 1/(b * y + 1)) * x
    nexty = y - d * y + c * x * y
    x, y = nextx, nexty
    t = t + 0.1

def observe():
    # This function essentially records the current state of x, y and t so that 
    # they can be plotted over time.
    global x, y, resultx, resulty, t, timesteps
    resultx.append(x)
    resulty.append(y)
    timesteps.append(t)

initialize()
while t < 10:
    update()
    observe()

fig1 = pylab.figure()
fig2 = pylab.figure()

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)

ax1.plot(timesteps, resultx, 'r-')
ax1.plot(timesteps, resulty, 'b--')
ax2.plot(resultx, resulty)

pylab.show()