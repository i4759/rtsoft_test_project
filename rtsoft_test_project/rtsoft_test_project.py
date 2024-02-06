import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize, Bounds

def objective_function(V, p):
    return V*1.25*p-0.25*V    



# Generate data
obj_counts = int(input("Type objects count: "))
V = np.random.randint(1,250, size=obj_counts)
print(len(V), V[:obj_counts])

p = np.random.uniform(1,100, size=obj_counts)
p = [round(elm) for elm in p]
print(len(p), p[:obj_counts])

results = objective_function(V, p)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(V, p, results, s=1, color='b')

ax.set_xlabel('$V$')
ax.set_ylabel('$p$')
ax.set_zlabel('$f(x)$')




plt.show()
