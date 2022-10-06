NICKNAME = 'Goshaan4k'
import numpy as np
import matplotlib.pyplot as plt
def null_vec():
    a = np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    raise NotImplementedError()
    return a
def reverse_vec(v):
    v_rev = np.flip(v)
    raise NotImplementedError()
    return v_rev
def matrix():
    m = np.array([[0, 0, 0],
                  [0, 0, 0],
	              [0, 0, 0]])
    for i in range(0, 9):
        m[i//3][i%3] = i
    raise NotImplementedError()
    return m
def checkerboard(w, b):
    m = np.zeros((8,8),dtype=str)
    m[1::2,::2] = b
    m[::2,1::2] = b
    m[1::2,1::2] = w
    m[::2,::2] = w
    raise NotImplementedError()
    return m
def cartesian_to_polar(c):
    p = np.zeros((10, 2), dtype=float)
    p[:, 0] = np.sqrt((c[:, 0])**2 + (c[:, 1])**2)
    p[:, 1] = np.arctan((c[:, 1]/c[:, 0]))
    raise NotImplementedError()
    return p
def make_curve(n, a):
    phi = np.linspace(1, 10, num=n)
    r = a + np.cos(phi)
    xy = np.empty((n, 2))
    xy[:, 0] = r * np.cos(phi)
    xy[:, 1] = r * np.sin(phi)
    raise NotImplementedError()
    return xy
N = 50
A = 1
m = make_curve(N, A)
for a in np.arange(0, 2, 0.2):
    plt.plot(make_curve(500, a)[:, 0], make_curve(500, a)[:, 1])
plt.show()
raise NotImplementedError()
