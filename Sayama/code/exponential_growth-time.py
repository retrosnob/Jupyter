import matplotlib.pylab as pylab

a = 1.1

def initialize():
    global x, result, t, timesteps
    x = 1
    result = [x]
    t = 0
    timesteps = [t]

def observe():
    global x, result
    result.append(x)
    timesteps.append(t)

def update():
    global x, result, t, timesteps
    x = a * x
    t = t + 0.1

initialize()
while t < 3:
    update()
    observe()

pylab.plot(timesteps, result)
pylab.show()

print("Done")