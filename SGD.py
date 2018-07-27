import numpy as np
import matplotlib.pyplot as plot


def f(x):
    y = np.power(x,4) - 5 * np.square(x) + 2 * x
    return y

def diff_f(x):
    y = 4 * np.power(x,3) - 10 * x + 2
    return y
x_data = np.linspace(-2,2,500)[:,np.newaxis]
fig = plot.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, f(x_data))
plot.ion()
plot.show()

stepsize = 0.0001 # learning rate (alpha)
start_x = (np.random.rand(1) - 0.5) * 4 # initial random input (-2,2)
count = 0
delta = 10 
while delta > 10e-12: # cost value
    start_y = f(start_x)
    start_x = start_x - stepsize * diff_f(start_x)
    delta = start_y - f(start_x)
    count = count + 1
    if(count%100) == 0 :
        try:
            ax.points.remove(points[0])
        except Exception:
            pass
        points = ax.plot(start_x,f(start_x),'ro')
        plot.pause(0.5)
        print('Conunter : %d ; x = %f ; f(x) = %f ;' % (count,start_x,f(start_x)))
print('Conunter : %d ; x = %f ; f(x) = %f ;' % (count,start_x,f(start_x)))

