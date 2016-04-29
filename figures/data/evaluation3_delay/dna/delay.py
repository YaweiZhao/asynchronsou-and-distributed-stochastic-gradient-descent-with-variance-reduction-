import numpy
import matplotlib.ticker
import matplotlib.pyplot as plt
#m10e3=(383,370.47)
#m10e4=(711,592)
#m10e5=(192,170.55)
compute_time=(1635.53,1643.59,1663.98,1680.39,1696.63)
wait_time=(4077,3032,2435,1796,1697)
width=0.24
x=numpy.arange(5)

fig = plt.figure()
ax = fig.add_subplot(111)

#rects3 = ax.bar(x+width*2, m10e5, width, color='k')
#ax.semilogy(x,compute_time)
#ax.semilogy(x,wait_time)
rects2 = ax.bar(x, wait_time, width, color='b')
rects1 = ax.bar(x, compute_time,width, color='r')

#plt.semilogy(x,compute_time)

ax.set_xticks(x+width/2)
ax.set_xticklabels(('10','20','30','40','50'))
plt.xticks(fontsize=16) 
plt.yticks(fontsize=16)
ax.set_ylabel("Time (s)",fontsize=18)
ax.set_xlabel("Delay $\\tau$",fontsize=18)
leg=ax.legend( (rects2[0],rects1[0]), ('Average wait time','Average computing time') )
for t in leg.get_texts(): 
     t.set_fontsize(16) 
plt.show()







