import matplotlib.pylab as pylab

a = 1.1

def initialize():
    global x, y, resultx, resulty, t, timesteps
    x = 1
    y = 1
    resultx = [x]
    resulty = [y]
    t = 0
    timesteps = [t]

def observe():
    global x, y, resultx, resulty, t, timesteps
    resultx.append(x)
    resulty.append(y)
    timesteps.append(t)

def update():
    # This is Lotka-Volterra with x as predator, y as prey. The populations can go below zero.
    global x, y, resultx, resulty, t, timesteps
    nextx = 0.5 * x + y
    nexty = -0.5 * x + y
    x, y = nextx, nexty
    t = t + 0.1

initialize()
while t < 3:
    update()
    observe()

pylab.plot(timesteps, resultx, 'r-')
pylab.plot(timesteps, resulty, 'b--')
# pylab.plot(resultx, resulty)
pylab.show()

print("Done")