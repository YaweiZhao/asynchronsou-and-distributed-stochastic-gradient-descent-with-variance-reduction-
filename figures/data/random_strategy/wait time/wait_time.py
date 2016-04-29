import numpy
import matplotlib.ticker
import matplotlib.pyplot as plt
#m10e3=(383,370.47)
#m10e4=(711,592)
#m10e5=(192,170.55)
no_tricks=(383,711,192)
tricks=(370.47,592,170.55)
width=0.24
x=numpy.arange(3)

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(x, no_tricks,width, color='r')
rects2 = ax.bar(x+width, tricks, width, color='b')
#rects3 = ax.bar(x+width*2, m10e5, width, color='k')
ax.axis( [0,2.5, 100, 800])
#ax.set_yticks([100,800]) #plt.xticks(range(len(x)), ['a', 'b', 'c', 'd', 'e', 'f']); 


plt.xticks(fontsize=16) 
plt.yticks(fontsize=16) 
ax.set_xticks(x+width)
ax.set_xticklabels(('$10^3$','$10^4$','$10^5$'),fontsize=19)
ax.set_ylabel("Average wait time (s)",fontsize=18)
ax.set_xlabel("$m$",fontsize=19)
leg=ax.legend( (rects1[0], rects2[0]), ('Static sampling', 'Dynamic sampling') )
for t in leg.get_texts(): 
     t.set_fontsize(16) 


plt.show()







