import fileinput
import matplotlib.pyplot as plt

def read_x(x1,y1,x2,y2,x3,y3,x4,y4):
	fn_constant_00001='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/accelerated/constant00001.txt'
	fn_accelerated_00001='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/accelerated/accelerated00001.txt'
	fn_constant_000001='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/accelerated/constant000001.txt'
	fn_accelerated_000001='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/accelerated/accelerated000001.txt'
	
	f_constant_00001=open(fn_constant_00001,'r+')
	f_accelerated_00001=open(fn_accelerated_00001,'r+')
	f_constant_000001=open(fn_constant_000001,'r+')
	f_accelerated_000001=open(fn_accelerated_000001,'r+')
	index=0
	for line1 in fileinput.input(fn_constant_00001):
		_1arr=line1.split('\r')[0].split('\t')
		x1.append(float(_1arr[0]))
		y1.append(float(_1arr[1]))
	for line2 in fileinput.input(fn_accelerated_00001):
		_2arr=line2.split('\r')[0].split('\t')
		x2.append(float(_2arr[0]))
		y2.append(float(_2arr[1]))
		#print _2arr
	for line3 in fileinput.input(fn_constant_000001):
		#print line3
		_3arr=line3.split('\r')[0].split('\t')
		index=index+1
		x3.append(float(_3arr[0]))
		y3.append(float(_3arr[1]))
	for line4 in fileinput.input(fn_accelerated_000001):
		_4arr=line4.split('\r')[0].split('\t')
		x4.append(float(_4arr[0]))
		y4.append(float(_4arr[1]))

	f_constant_00001.close()
	f_accelerated_00001.close()
	f_constant_000001.close()
	f_accelerated_000001.close()


x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]

read_x(x1,y1,x2,y2,x3,y3,x4,y4)
plt.plot(x3,y3,'-b',linewidth=2.5,label="$\\theta=10^{-6},\,constant$")
plt.plot(x4,y4,'--b',linewidth=2.5,label="$\\theta=10^{-6},\,accelerated$")
plt.plot(x1,y1,'-r',linewidth=2.5,label="$\\theta=10^{-5},\,constant$")
plt.plot(x2,y2,'--r',linewidth=2.5,label="$\\theta=10^{-5},\,accelerated$")
plt.xticks(fontsize=16) 
plt.yticks(fontsize=16) 

plt.ylabel("Objective value",fontsize=18)
plt.xlabel("Time (s)",fontsize=18)

leg=plt.legend(bbox_to_anchor=(0.99,0.57))
for t in leg.get_texts(): 
     t.set_fontsize(16) 

plt.show()







