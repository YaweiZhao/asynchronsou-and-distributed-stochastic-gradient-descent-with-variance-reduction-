import fileinput
import matplotlib.pyplot as plt

def read_x(x1,y1,x2,y2,x3,y3,x4,y4):
	fn_4='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation2_speedup/yearPredictMSD/4nodes.txt'
	fn_8='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation2_speedup/yearPredictMSD/8nodes.txt'
	fn_16='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation2_speedup/yearPredictMSD/16nodes.txt'
	fn_32='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation2_speedup/yearPredictMSD/32nodes.txt'

	f_4=open(fn_4,'r+')
	f_8=open(fn_8,'r+')
	f_16=open(fn_16,'r+')
	f_32=open(fn_32,'r+')
	
	index=0
	for line1 in fileinput.input(fn_4):
		_1arr=line1.split('\r')[0].split('\t')
		x1.append(float(_1arr[0]))
		y1.append(float(_1arr[1]))
	for line2 in fileinput.input(fn_8):
		_2arr=line2.split('\r')[0].split('\t')
		x2.append(float(_2arr[0]))
		y2.append(float(_2arr[1]))
		#print _2arr
	for line3 in fileinput.input(fn_16):
		#print line3
		_3arr=line3.split('\r')[0].split('\t')
		index=index+1
		x3.append(float(_3arr[0]))
		y3.append(float(_3arr[1]))
	for line4 in fileinput.input(fn_32):
		#print line3
		_4arr=line4.split('\r')[0].split('\t')
		index=index+1
		x4.append(float(_4arr[0]))
		y4.append(float(_4arr[1]))
	print x1
	f_4.close()
	f_8.close()
	f_16.close()
	f_32.close()


x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]

read_x(x1,y1,x2,y2,x3,y3,x4,y4)
plt.plot(x1,y1,'-k',linewidth=2.5,label="4 workers")
plt.plot(x2,y2,':b',linewidth=2.5,label="8 workers")
plt.plot(x3,y3,'-.g',linewidth=2.5,label="16 workers")
plt.plot(x4,y4,'--r',linewidth=2.5,label="32 workers")
plt.xticks(fontsize=16) 
plt.yticks(fontsize=16) 

leg=plt.legend()
plt.ylabel("Objective value",fontsize=18)
plt.xlabel("Time (s)",fontsize=18)

for t in leg.get_texts(): 
     t.set_fontsize(16) 
plt.show()







