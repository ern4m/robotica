import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import builtins
from dataclasses import dataclass 

println = builtins.print

# gamma = None
# max_gamma = 30
# delta_time = 0.05
# v = 1
# theta = lambda v, gamma :( v * np.tan(gamma))/ L
# x = lambda v, theta : v * np.cos(np.radians(theta))
# y = lambda v, theta : v * np.sin(np.radians(theta))

@dataclass
class Model:
    base: float
    max_gamma: float
    delta_time: float = 0.05

    def move(self, x: float, y: float, theta: float, velocity: float, acceleration: float, gamma: float) -> tuple[float,float,float]:
        
        # to use when there's velocity changes
        # velocity = velocity + self.delta_time * acceleration
        velocity = velocity

        # gamma changes
        if gamma < -self.max_gamma:
            gamma = -self.max_gamma
        else:
            if gamma > self.max_gamma:
                gamma = self.max_gamma
            else:
                gamma = gamma
        
        # coords changes
        _x = x + velocity*np.cos(theta) * self.delta_time
        _y = y + velocity*np.sin(theta) * self.delta_time


        # theta change
        # _theta = int(np.degrees((velocity / self.base) * np.tan(gamma)))
        _theta = (velocity / self.base) * np.tan(gamma)

        return (_x, _y ,_theta)

myModel = Model(base = 1., max_gamma = 40., delta_time = 1.)


x = []
y = []
theta = []

size = 40

# gamma = list(map(lambda x: x*np.random.choice(range(-30,30,1)), np.random.choice([0,1], size=(size,))))

gamma = np.random.choice(range(-30,30,1), size=(size,))

# gamma = np.ones(size)*30

# gamma = [0, 0, 0, 1, 0, -1, 1, 0, 0, 0, 0] * 30

for k in range(len(gamma)):
    if len(x) == 0:
        _x, _y, _theta = myModel.move(0., 0., 0., 1., 0., gamma[k])
    else:
        _x, _y, _theta = myModel.move(x[-1], y[-1], theta[-1], 1., 0., gamma[k])

    print(_x, _y, _theta, "\n")

    x.append(_x)
    y.append(_y)
    theta.append(_theta)

# print(x, "\n",  y, "\n", theta)

# plt.plot(x,y)
# plt.show()

fig, ax = plt.subplots()

line = ax.plot(x[0],y[0])[0]
ax.set(xlim=[0, 40], ylim=[-5, 5], xlabel='x', ylabel='y')
ax.legend()

def update(frame):
    # for each frame, update the data stored on each artist.
    _x = x[:frame]
    _y = y[:frame]

    # scatter
    data = np.stack([_x, _y])


    # update the line plot:
    line.set_xdata(x[:frame])
    line.set_ydata(y[:frame])
    return (line)


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=100)

plt.show()

