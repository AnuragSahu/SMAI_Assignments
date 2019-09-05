# this is the Code for 3rd part of the Assignment

import random
import matplotlib.pyplot as plt
import numpy as np

def RC_Multiply(a,b):
	sum = int("0",10)
	for i in range(3):
		sum += a[i]*b[i]
	return sum;

Data = []
plt_dt = []
a = 0
for i in range(100):
	r_fra1 = random.randint(-1000,1000)/1000;
	r_fra2 = random.randint(-1000,1000)/1000;
	dat_plt = [r_fra1, r_fra2]
	plt_dt.append(dat_plt)
	a = [r_fra1, r_fra2,1]
	if(i < 50):
		clas = "A"
	else:
		clas = "B"
	Data.append([a,clas])

w1 = [1,1,0]  #plot this line
w2 = [-1,-1,0]
w3 = [0,0.5,0]
w4 = [1, -1,5] # plot this line
w5 = [1,1,0.3] # plot this line

acc_w1 = 0;
acc_w2 = 0;
acc_w3 = 0;
acc_w4 = 0;
acc_w5 = 0;
for i in range(100):
	if(RC_Multiply(w1,Data[i][0]) > 0 and Data[i][1]=="A"):
		acc_w1 += 1;
	elif(RC_Multiply(w1,Data[i][0]) <= 0 and Data[i][1]=="B"):
		acc_w1 += 1;
	if(RC_Multiply(w1,Data[i][0]) > 0 and Data[i][1]=="A"):
		acc_w2 += 1;
	elif(RC_Multiply(w2,Data[i][0]) <= 0 and Data[i][1]=="B"):
		acc_w2 += 1;
	if(RC_Multiply(w3,Data[i][0]) > 0 and Data[i][1]=="A"):
		acc_w3 += 1;
	elif(RC_Multiply(w3,Data[i][0]) <= 0 and Data[i][1]=="B"):
		acc_w3 += 1;
	if(RC_Multiply(w4,Data[i][0]) > 0 and Data[i][1]=="A"):
		acc_w4 += 1;
	elif(RC_Multiply(w4,Data[i][0]) <= 0 and Data[i][1]=="B"):
		acc_w4 += 1;
	if(RC_Multiply(w5,Data[i][0]) > 0 and Data[i][1]=="A"):
		acc_w5 += 1;
	elif(RC_Multiply(w5,Data[i][0]) <= 0 and Data[i][1]=="B"):
		acc_w5 += 1;

print("PART (i)")
print("Accuracy of a : "+str(acc_w1)+"%")
print("Accuracy of b : "+str(acc_w2)+"%")
print("Accuracy of c : "+str(acc_w3)+"%")
print("Accuracy of d : "+str(acc_w4)+"%")
print("Accuracy of e : "+str(acc_w5)+"%")

print("PART (ii)")
fig, ax = plt.subplots()
data_plot = np.array(plt_dt);
x,y = data_plot.T
ax.scatter(x,y)
x = np.array(range(-1,2))
y = (w1[0]/-w1[1])*x + (w1[2]/-w1[1])
la = ax.plot(x,y,label='line for a')
ax.set_title('With Boundry a')

fig,bx = plt.subplots()
data_plot = np.array(plt_dt);
x,y = data_plot.T
bx.scatter(x,y)
x = np.array(range(-1,2))
y = (w4[0]/-w4[1])*x + (w4[2]/-w4[1])
bx.plot(x,y,label='line for d')
bx.set_title('With Boundry b')

fig,cx = plt.subplots()
data_plot = np.array(plt_dt);
x,y = data_plot.T
cx.scatter(x,y)
x = np.array(range(-1,2))
y = (w5[0]/-w5[1])*x + (w5[2]/-w5[1])
le = cx.plot(x,y,label='line for e')
cx.set_title('With Boundry c')
plt.show()
