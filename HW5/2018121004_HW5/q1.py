import random
import numpy as np
import numpy.linalg as LA
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#test samples generate
data = np.random.uniform(0,10,[1000,2])

#part1
mean1 = np.array([3, 3])
mean2 = np.array([7, 7])
U1 = np.array([[3, 0], [0, 3]])
U2 = np.array([[3, 0], [0, 3]])

classified_a = []
classified_b = []
for x in data:
    P1 = (1/(2 * np.pi** 2)* (LA.det(U1)** 0.5)) * (math.exp(-((x - mean1).dot(LA.inv(U1)).dot((x - mean1).T))/2))
    P2 = (1/(2 * np.pi** 2)* (LA.det(U2)** 0.5)) * (math.exp(-((x - mean2).dot(LA.inv(U2)).dot((x - mean2).T))/2))
    if(P1>P2):
        classified_a.append([x[0],x[1],P1])
    else:
        classified_b.append([x[0],x[1],P2])
        
    
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
classified_a = np.array(classified_a)
classified_ax,classified_ay,classified_az = classified_a.T
ax.scatter(classified_ax,classified_ay,classified_az,c="r")

classified_b = np.array(classified_b)
classified_bx,classified_by,classified_bz = classified_b.T
ax.scatter(classified_bx,classified_by,classified_bz,c="b")

#plt.show()



U1 = np.array([[3, 1], [2, 3]])
U2 = np.array([[7, 2], [1, 7]])

classified_a = []
classified_b = []
for x in data:
    P1 = (1/(2 * np.pi** 2)* (LA.det(U1)** 0.5)) * (math.exp(-((x - mean1).dot(LA.inv(U1)).dot((x - mean1).T))/2))
    P2 = (1/(2 * np.pi** 2)* (LA.det(U2)** 0.5)) * (math.exp(-((x - mean2).dot(LA.inv(U2)).dot((x - mean2).T))/2))
    if(P1>P2):
        classified_a.append([x[0],x[1],P1])




















































































































        
    else:
        classified_b.append([x[0],x[1],P2])
        
    
fig1 = plt.figure()
bx = fig1.add_subplot(111,projection='3d')
classified_a = np.array(classified_a)
classified_ax,classified_ay,classified_az = classified_a.T
bx.scatter(classified_ax,classified_ay,classified_az,c="r")

classified_b = np.array(classified_b)
classified_bx,classified_by,classified_bz = classified_b.T
bx.scatter(classified_bx,classified_by,classified_bz,c="b")

plt.show()