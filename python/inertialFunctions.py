import numpy as np
import matplotlib.pyplot as plt

def j_AM(theta):
    thetadeg=theta*np.pi/180.0
    
    # define the single particle angular momentum value j
    # *******************
    j=5.5
    # *******************

    j1=j*np.cos(thetadeg)
    j2=j*np.sin(thetadeg)
    return (j1,j2)

##the function takes the argument theta for construcing the angular momentum componets of the odd particle
## the angular momentum components are calculated in a tuple (j1,j2)
##the value of the spin is defined as a constant inside the angular momentum method 
def A(I,A1,A2,theta):
    j2=j_AM(theta)[1]
    a=A2*(1-j2/I)-A1
    return a

def u(I,A1,A2,A3,theta):
    fA=A(I,A1,A2,theta)
    result=(A3-A1)/fA
    return result

def v0(I,A1,A2,theta):
    j1=j_AM(theta)[0]
    fa=A(I,A1,A2,theta)
    v=-(A1*j1)/fa
    return v

def inertiaFactors(mois):
    A1=1.0/(2.0*mois[0])
    A2=1.0/(2.0*mois[1])
    A3=1.0/(2.0*mois[2])
    return (round(A1,4),round(A2,4),round(A3,4))

# constants
mois1=(89,12,48)
mois2=(6,0.25,4)
mois3=(1.9,0.63,0.18)

theta1=-71
theta2=77
theta3=55

axes=(inertiaFactors(mois1),mois2,mois3)
thetas=(theta1,theta2,theta3)
plotnames=("1axis-quant.pdf","2axis-quant.pdf","3axis-quant.pdf")

def avg(array):
    sump=0.0
    for x in array:
        sump=sump+x
    average=sump/len(array)
    return average

def plotInertialParameters(k,plotnames,axes,thetas):
    A1=axes[k][0]
    A2=axes[k][1]
    A3=axes[k][2]
    spins=[]
    udata=[]
    vdata=[]
    avgval=()
    # generate the spin values
    for I in np.arange(0.1,35.5,0.1):
        spins.append(I)
    # generate the (u,v0) data
    for I in spins:
        uval=u(I,A1,A2,A3,thetas[k])
        vval=v0(I,A1,A2,thetas[k])
        udata.append(uval)
        vdata.append(vval)
    #calculate the average u and v0 from the entire data set
    avgval=(avg(udata),avg(vdata))
    # plot the data
    plt.plot(spins,udata,'r-',spins,vdata,'b-')
    plt.hlines(avgval[0],spins[0],spins[len(spins)-1],linestyles='dashed',colors='r')
    plt.hlines(avgval[1],spins[0],spins[len(spins)-1],linestyles='dashed',colors='b')
    plt.savefig(plotnames[k],bbox_inches='tight')
    # clear the plot for other calls
    plt.clf()
    print(avgval)

plotInertialParameters(0,plotnames,axes,thetas)
plotInertialParameters(1,plotnames,axes,thetas)
plotInertialParameters(2,plotnames,axes,thetas)