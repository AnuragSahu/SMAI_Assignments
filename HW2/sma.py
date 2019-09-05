import numpy as np 
import matplotlib.pyplot as plt

AB = np.random.randn(100,2) #create a random array of [[A1,B1],[A2,B2],...] as example
print(AB)
x = np.linspace(-100.,100.)

fig,ax = plt.subplots()
for ABi in AB:
    A,B = ABi
    ax.plot(x, A*x+B )

ax.set_xlim((-100.,100.))
ax.set_ylim((-100.,100.))

plt.show()