import matplotlib.pyplot as plt
import numpy as np

# comparison between the analytical expression of the component x1 of the angular momentum and its second order power series expansion

#calculates the analytical expression of x1
#calculates the component x1 in terms of spherical componets r, theta, fi
#calculates the second order expansion of x1 (with built in python module)
#express second order expansion as a method

def x1Spherical(r, theta, fi):
    x1Quantization=[0,0,0]
    x1Quantization[0]=r*np.cos(theta)
    x1Quantization[1]=r*np.sin(theta)*np.sin(fi)
    x1Quantization[2]=r*np.sin(theta)*np.cos(fi)
    return x1Quantization

def AM_Components(r,theta,fi):
    x1=(x1Spherical(r,theta,fi)[0],x1Spherical(r,theta,fi)[1],x1Spherical(r,theta,fi)[2])
    x2=(r*np.sin(theta)*np.cos(fi),r*np.cos(theta),r*np.sin(theta)*np.sin(fi))
    x3=(r*np.sin(theta)*np.sin(fi),r*np.sin(theta)*np.cos(fi),r*np.cos(theta))
    return (x1,x2,x3)

def x1AM(x2,x3,I):
    x1=np.sqrt(np.power(I,2)-(np.power(x2,2)+np.power(x3,2)))
    return x1

def x1PSE(x2,x3,I):
    pse=I*(1-(np.power(x2,2)+np.power(x3,2))/(2*np.power(I,2)))
    return pse


xvalues=[]
xanal=[]
xpse=[]

#first axis quantization
I=9.5
theta=np.pi/6
fi=np.pi/9
for r in np.arange(0,I,0.1):
    xvalues.append(r)
    x2=AM_Components(r,theta,fi)[1][0]
    x3=AM_Components(r,theta,fi)[2][0]
    x1anal=x1AM(x2,x3,r)
    x1pse=x1PSE(x2,x3,r)
    xanal.append(x1anal)
    xpse.append(x1pse)

plt.plot(xvalues,xanal,'r-',xvalues,xpse,'b--')
plt.savefig("x1Approx.pdf",bbox_inches="tight")
