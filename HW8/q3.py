import numpy as np
import matplotlib.pyplot as plt

points = np.array([[2,0],
				   [0,2],
				   [3,3],
				   [5,1]])

mean_points = np.mean(points,axis=0)

covariance_mat = np.cov(points.T)

eigen_vals, eigen_vectors = np.linalg.eig(covariance_mat)


print(eigen_vectors)