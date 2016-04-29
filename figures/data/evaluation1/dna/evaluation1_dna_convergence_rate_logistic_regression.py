import fileinput
import matplotlib.pyplot as plt

def read_x(x1,y1,x2,y2,x3,y3,x4,y4):
	fn_without_tricks_disSVRG='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation1/dna/disSVRG-without-tricks.txt'
	fn_tricks_disSVRG='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation1/dna/disSVRG-with-tricks.txt'
	fn_petuumSGD='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation1/dna/petuumSGD.txt'
	fn_SSGD='/Users/yawei/Documents/papers/asynchronsou and distributed stochastic gradient descent with variance reduction /figures/data/evaluation1/dna/SSGD.txt'

	f_without_tricks_disSVRG=open(fn_without_tricks_disSVRG,'r+')
	f_tricks_disSVRG=open(fn_tricks_disSVRG,'r+')
	f_petuumSGD=open(fn_petuumSGD,'r+')
	f_SSGD=open(fn_SSGD,'r+')
	
	index=0
	for line1 in f_without_tricks_disSVRG:
		_1arr=line1.split('\r')[0].split('\t')
		x1.append(float(_1arr[0]))
		y1.append(float(_1arr[1]))
	for line2 in fileinput.input(fn_petuumSGD):
		_2arr=line2.split('\r')[0].split('\t')
		index=index+1
		x2.append(float(_2arr[0]))
		y2.append(float(_2arr[1]))
	for line3 in fileinput.input(fn_tricks_disSVRG):
		_3arr=line3.split('\r')[0].split('\t')
		x3.append(float(_3arr[0]))
		y3.append(float(_3arr[1]))
	for line4 in fileinput.input(fn_SSGD):
		_4arr=line4.split('\r')[0].split('\t')
		x4.append(float(_4arr[0]))
		y4.append(float(_4arr[1]))
	

	f_without_tricks_disSVRG.close()
	f_tricks_disSVRG.close()
	f_petuumSGD.close()
	f_SSGD.close()


x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]

read_x(x1,y1,x2,y2,x3,y3,x4,y4)
plt.plot(x2,y2,'-k',linewidth=2.5,label="PetuumSGD")
plt.plot(x1,y1,':b',linewidth=2.5,label="DisSVRG-without tricks")
plt.plot(x4,y4,'-.g',linewidth=2.5,label="SSGD")
plt.plot(x3,y3,'--r',linewidth=2.5,label="DisSVRG-tricks")
plt.xticks(fontsize=16) 
plt.yticks(fontsize=16)

leg=plt.legend()
for t in leg.get_texts(): 
     t.set_fontsize(18) 

plt.ylabel("Objective value",fontsize=18)
plt.xlabel("Time (s)",fontsize=18)

plt.show()







