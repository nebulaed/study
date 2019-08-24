# Annotation 标注

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2*x+1

plt.figure(num=1, figsize=(8,5),)
plt.plot(x,y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

x0 = 1
y0 = 2*x0+1
plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,0],'k--', lw=2.5) # k代表黑色，--代表虚线

# method 1

plt.annotate(r'$2x+1=%s$' % y0, xy=(x0,y0), xycoords='data', xytext=(+30,-30), textcoords='offset points',
        fontsize=16, arrowprops=dict(arrowstyle='->',connectionstyle='arc3, rad=.2'))
# 第一个参数是标注的文字，用tex形式更好看，第二个参数xy表示标注的位置，坐标轴是data，xytext和textcoords结合起来表示以标注点为参考点向右30，向下30，字号为16，arrowprops以字典形式制定箭头样式：arrowstyle表示箭头，connectionstyle表示箭头角度

# method 2
plt.text(-3.7,3,r'$THis\ is\ the\ some\ text.\ \mu \sigma_i\ \alpha_t$',
        fontdict={'size':16,'color':'r'})

plt.show()
