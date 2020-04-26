import matplotlib.pyplot as plt
import numpy as np
from sympy.solvers import solve
from sympy import Symbol
from sympy import solveset, S

a = 5.5
b = 4.5

# the angular momentum 2D section of radius I 
def AMSphere(I):
    xdata=[]
    ydataPlus=[]
    ydataMinus=[]
    limit=1000
    x=-I
    for i in range(limit+1):
        xdata.append(round(x,2))
        x=x+2.0*I/limit
    for x in xdata:
        sol=np.sqrt(np.power(I,2)-np.power(x,2))
        ydataPlus.append(sol)
        ydataMinus.append(-sol)
    plt.plot(xdata,ydataMinus,'b-',xdata,ydataPlus,'b-')
    plt.axes().set_aspect(1)
    # plt.savefig("plot.pdf", bbox_inches="tight")

def EnergySurface(a,b,E):
    xdata=[]
    ydataPlus=[]
    ydataMinus=[]
    limit=1000
    x0=round(a*np.sqrt(E),2)
    x=-x0
    for i in range(limit+1):
        xdata.append(x)
        x=x+2.0*x0/limit
    print(xdata)
    for x in xdata:
        sol=b*np.sqrt(E-round(np.power(x,2)/np.power(a,2),2))
        ydataMinus.append(-sol)
        ydataPlus.append(sol)
    plt.plot(xdata,ydataMinus,'k--',xdata,ydataPlus,'k--')


# generate the ellipse through the parametric equations
# x0 = []
# y0 = []
# for i in np.arange(0, 2*np.pi+step, step):
#     x0.append(a*np.cos(i))
#     y0.append(b*np.sin(i))

x1 = []
y11 = []
y12 = []

x=-a
limit=1000
for i in range(limit+1):
    x1.append(round(x,2))
    x=x+2.0*a/limit

for x in x1:
    diff=np.power(a,2)-np.power(x,2)
    if(diff>=0.0):
        sol=(b*np.sqrt(diff))/a
        y11.append(sol)
        y12.append(-sol)

EnergySurface(3.0,2.0,1.00)
AMSphere(2)
plt.show()

# plt.plot(x1,y11,'r-',x1,y12,'r-')
# plt.axes().set_aspect(b/a)
