import numpy as np
import matplotlib.pyplot as plt

def my_func(samples,k_len):
#samples = small_samples

	x = np.linspace(0,np.pi,samples)
	y = np.sin(x) + np.random.normal(5,5,samples)
	
	#k = 5
	mu_final = []
	sig_final = []
	for k in range(2,k_len):
		data = []
		for i in range(len(x)):
			data.append([x[i],y[i]])
		
		data = np.array(data)
		np.random.shuffle(data)
		x,y = data.T
		
		data_split = []
		g_val_split = []
		
		for i in range(0,k):
			data_split.append([])
			g_val_split.append([])
			for j in range(int(len(x)/k)):
				data_split[i].append(x[i+j])
				g_val_split[i].append(y[i+j])
		
		data_split = np.array(data_split)
		g_val_split = np.array(g_val_split)
		
		mu = 0
		sig = 0
		errors = []
		for i in range(k):
			error_final = 0
			test = np.array(data_split[i])
			test = test.reshape(len(test),1)
			g_test = np.array(g_val_split[i])
			g_test = g_test.reshape(1,len(test))
		
			train = []
			g_train = []
			for j in range(k):
				if(j!=i):
					train.append(data_split[j])
					g_train.append(g_val_split[j])
		
			#train.reshape((k-1)*(samples/k),1)
			train = np.array(train)
			g_train = np.array(g_train)
			train = train.reshape(1,(k-1)*int(samples/k))
			g_train = g_train.reshape(1,(k-1)*int(samples/k))
			w = np.linalg.inv(train.dot(train.T)).dot(train.dot(g_train.T))
			predict = w.dot(test.T)
			error_final = np.absolute(predict-g_test)
			mu += np.mean(error_final)
			sig += np.var(error_final)
		
		mu = mu/k
		sig = sig/k
		mu_final.append(mu)
		sig_final.append(sig)

	return mu_final,sig_final

mu_final1,sig_final1 = my_func(100,20)
x = np.arange(0,len(mu_final1))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,mu_final1,c='r',label="mean")
ax.plot(x,sig_final1,c='b',label="Variance")
ax.legend(loc='upper left')
ax.grid(color='y', linestyle='-', linewidth=1)

mu_final2,sig_final2 = my_func(1000,100)
x = np.arange(0,len(mu_final2))
fig1 = plt.figure()
bx = fig1.add_subplot(111)
bx.plot(x,mu_final2,c='r', label="mean")
bx.plot(x,sig_final2,c='b',label="Variance")
bx.legend(loc='upper left')
bx.grid(color='y', linestyle='-', linewidth=1)

plt.show()