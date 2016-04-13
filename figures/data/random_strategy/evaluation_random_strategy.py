import fileinput
import matplotlib.pyplot as plt

def read_x(x1,y1,x2,y2,x3,y3):
	fn_100='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/random_strategy/m100'
	fn_1000='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/random_strategy/m1000'
	fn_10000='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/random_strategy/m10000'
	
	f_100=open(fn_100,'r+')
	f_1000=open(fn_1000,'r+')
	f_10000=open(fn_10000,'r+')
	
	index=0
	for line1 in fileinput.input(fn_100):
		_1arr=line1.split('\r')[0].split('\t')
		x1.append(float(_1arr[0]))
		y1.append(float(_1arr[1]))
	for line2 in fileinput.input(fn_1000):
		_2arr=line2.split('\r')[0].split('\t')
		x2.append(float(_2arr[0]))
		y2.append(float(_2arr[1]))
		#print _2arr
	for line3 in fileinput.input(fn_10000):
		#print line3
		_3arr=line3.split('\r')[0].split('\t')
		index=index+1
		x3.append(float(_3arr[0]))
		y3.append(float(_3arr[1]))

	f_100.close()
	f_1000.close()
	f_10000.close()


x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]

read_x(x1,y1,x2,y2,x3,y3)
plt.plot(x1,y1,'-k',label="$m=10^2$")
plt.plot(x2,y2,'-r',label="$m=10^3$")
plt.plot(x3,y3,'-b',label="$m=10^4$")
plt.legend()
plt.ylabel("Objective value")
plt.xlabel("Time (s)")

plt.show()







