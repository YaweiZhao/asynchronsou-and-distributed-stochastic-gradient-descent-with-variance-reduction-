import fileinput
import matplotlib.pyplot as plt

def read_x(x1,y1,x2,y2,x3,y3,x4,y4):
	fn_16='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation2_speedup/dna/16machines.txt'
	fn_32='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation2_speedup/dna/32machines.txt'
	fn_64='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation2_speedup/dna/64machines.txt'
	fn_128='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation2_speedup/dna/128machines.txt'

	f_16=open(fn_16,'r+')
	f_32=open(fn_32,'r+')
	f_64=open(fn_64,'r+')
	f_128=open(fn_128,'r+')
	
	index=0
	for line1 in fileinput.input(fn_16):
		_1arr=line1.split('\r')[0].split('\t')
		x1.append(float(_1arr[0]))
		y1.append(float(_1arr[1]))
	for line2 in fileinput.input(fn_32):
		_2arr=line2.split('\r')[0].split('\t')
		x2.append(float(_2arr[0]))
		y2.append(float(_2arr[1]))
		#print _2arr
	for line3 in fileinput.input(fn_64):
		#print line3
		_3arr=line3.split('\r')[0].split('\t')
		index=index+1
		x3.append(float(_3arr[0]))
		y3.append(float(_3arr[1]))
	for line4 in fileinput.input(fn_128):
		#print line3
		_4arr=line4.split('\r')[0].split('\t')
		index=index+1
		x4.append(float(_4arr[0]))
		y4.append(float(_4arr[1]))
	print x1
	f_16.close()
	f_32.close()
	f_64.close()
	f_128.close()


x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]

read_x(x1,y1,x2,y2,x3,y3,x4,y4)
plt.plot(x1,y1,'-k',linewidth=2.5,label="16 workers")
plt.plot(x2,y2,':b',linewidth=2.5,label="32 workers")
plt.plot(x3,y3,'-.g',linewidth=2.5,label="64 workers")
plt.plot(x4,y4,'--r',linewidth=2.5,label="128 workers")
plt.xticks(fontsize=16) 
plt.yticks(fontsize=16) 
plt.axis( [0,1200, 0.1, 0.3])

leg=plt.legend()
plt.ylabel("Objective value",fontsize=18)
plt.xlabel("Time (s)",fontsize=18)
for t in leg.get_texts(): 
     t.set_fontsize(16) 

plt.show()







