import numpy
import matplotlib.ticker
import matplotlib.pyplot as plt
#m10e3=(383,370.47)
#m10e4=(711,592)
#m10e5=(192,170.55)
wait_time=(253.6,102.339,21.736,20.49,20.73)
compute_time=(17.46,17.7,19.39,20.38,20.37)
width=0.24
x=numpy.arange(5)

fig = plt.figure()
ax = fig.add_subplot(111)

rects2 = ax.bar(x, wait_time, width, color='b')
rects1 = ax.bar(x, compute_time,width, color='r')

ax.set_xticks(x+width/2)
ax.set_xticklabels(('10','100','200','300','400'))
plt.xticks(fontsize=16) 
plt.yticks(fontsize=16)
ax.set_ylabel("Time (s)",fontsize=18)
ax.set_xlabel("delay $\\tau$",fontsize=18)
leg=ax.legend( (rects2[0],rects1[0]), ('Average wait time', 'Averageg computing time') )
for t in leg.get_texts(): 
     t.set_fontsize(16) 
plt.show()







