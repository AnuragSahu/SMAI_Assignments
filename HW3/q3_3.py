import numpy as np
import random 
import matplotlib.pyplot as plt

data = []
# Generating Random Points
for z in range(1000):
	x = random.randint(-10,10) + random.randint(-10,10)/10
	y = x + random.randint(-10,10)/10
	a = [x,y]
	data.append(a)

# Plotting the Points
x,y = np.array(data).T
mean_x = np.mean(x)
mean_y = np.mean(y)

print ("covariance : ")
#covaar_mat = np.cov(x,y)
covaar_mat = np.corrcoef(x,y)
print(covaar_mat)

print ("Eigen Values : ")
Eigen_values, Eigen_vectors = np.linalg.eig(covaar_mat)
print(Eigen_values)
print ("Eigen Vectors : ")
print(Eigen_vectors)
plt.scatter(x,y)
plt.arrow(mean_x,mean_y,Eigen_vectors[0][0],Eigen_vectors[1][0],head_width=0.5,head_length=0.2,color="r")
plt.arrow(mean_x,mean_y, Eigen_vectors[0][1]/4,Eigen_vectors[1][1]/4,head_width=0.5,head_length=0.2,color="g")
plt.show()