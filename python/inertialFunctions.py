import numpy as np
import matplotlib.pyplot as plt


def j_AM(theta):
    thetadeg = theta*np.pi/180.0

    # define the single particle angular momentum value j
    # *******************
    j = 5.5
    # *******************

    j1 = j*np.cos(thetadeg)
    j2 = j*np.sin(thetadeg)
    return (j1, j2, 0)

# the function takes the argument theta for construcing the angular momentum componets of the odd particle
# the angular momentum components are calculated in a tuple (j1,j2)
# the value of the spin is defined as a constant inside the angular momentum method


def A(I, A1, A2, theta):
    j2 = j_AM(theta)[1]
    a = A2*(1-j2/I)-A1
    return a


def u(I, A1, A2, A3, theta):
    fA = A(I, A1, A2, theta)
    result = (A3-A1)/fA
    return result


def v0(I, A1, A2, theta):
    j1 = j_AM(theta)[0]
    fa = A(I, A1, A2, theta)
    v = -(A1*j1)/fa
    return v


def inertiaFactors(mois):
    A1 = 1.0/(2.0*mois[0])
    A2 = 1.0/(2.0*mois[1])
    A3 = 1.0/(2.0*mois[2])
    return (round(A1, 4), round(A2, 4), round(A3, 4))


def showmois(mois, theta, k):
    mois = inertiaFactors(mois)
    text1 = 'A1'+str(k)+'='+str(mois[0])+';'
    text2 = 'A2'+str(k)+'='+str(mois[1])+';'
    text3 = 'A3'+str(k)+'='+str(mois[2])+';'
    text4 = 'theta'+str(k)+'='+str(np.round(theta*np.pi/180, 2))+';'
    print(text1, text2, text3, text4)


# constants
mois1 = (89, 12, 48)
mois2 = (6, 0.25, 4)
mois3 = (1.90, 0.64, 0.18)

theta1 = -71.0
theta2 = 77.0
theta3 = 55.0

# alternative mois for obtaining ellipse-like trajectories for the 3-axis quantization
# the 3-axis is the axis with the largest moment of inertia
mois1_alternative = (63, 33, 13)
mois2_alternative = (12, 54, 18)
mois3_alternative = (14, 8, 48)

theta1_alternative = -112
theta2_alternative = -98
theta3_alternative = 94

showmois(mois1_alternative, theta1_alternative, 1)
showmois(mois2_alternative, theta2_alternative, 2)
showmois(mois3_alternative, theta3_alternative, 3)


def arbitraryEnergy(I, mois, theta, k):
    Ak = inertiaFactors(mois)[k-1]
    jk = j_AM(theta)[k-1]
    E = np.round(Ak*np.power(I-jk, 2), 4)
    return E


print(arbitraryEnergy(9.5, mois1_alternative, theta1_alternative, 1))
print(arbitraryEnergy(9.5, mois2_alternative, theta2_alternative, 2))
print(arbitraryEnergy(9.5, mois3_alternative, theta3_alternative, 3))

# axes = (inertiaFactors(mois1), mois2, mois3)
# alternative axes using the mois which give elliptic paraboloid H'
axes = (inertiaFactors(mois1_alternative),
        inertiaFactors(mois2_alternative), inertiaFactors(mois3_alternative))

# thetas = (theta1, theta2, theta3)
thetas = (theta1_alternative, theta2, theta3_alternative)
plotnames = ("1axis-quant.pdf", "2axis-quant.pdf", "3axis-quant.pdf")

# print(u(9.5, axes[0][0], axes[0][1], axes[0][2], thetas[0]),v0(9.5, axes[0][0], axes[0][1], thetas[0]))
print(axes[0][0], axes[0][1], axes[0][2])

# print(u(9.5, axes[1][0], axes[1][1], axes[1][2], thetas[1]),v0(9.5, axes[1][0], axes[1][1], thetas[1]))
print(axes[1][0], axes[1][1], axes[1][2])

# print(u(9.5, axes[2][0], axes[2][1], axes[2][2], thetas[2]),v0(9.5, axes[2][0], axes[2][1], thetas[2]))
print(axes[2][0], axes[2][1], axes[2][2])


def avg(array):
    sump = 0.0
    for x in array:
        sump = sump+x
    average = sump/len(array)
    return average


def plotInertialParameters(k, plotnames, axes, thetas):
    A1 = axes[k][0]
    A2 = axes[k][1]
    A3 = axes[k][2]
    spins = []
    udata = []
    vdata = []
    avgval = ()
    # generate the spin values
    for I in np.arange(0.1, 35.5, 0.1):
        spins.append(I)
    # generate the (u,v0) data
    for I in spins:
        uval = u(I, A1, A2, A3, thetas[k])
        vval = v0(I, A1, A2, thetas[k])
        udata.append(uval)
        vdata.append(vval)
    # calculate the average u and v0 from the entire data set
    avgval = (avg(udata), avg(vdata))
    # plot the data
    plt.plot(spins, udata, 'r-', spins, vdata, 'b-')
    plt.hlines(avgval[0], spins[0], spins[len(spins)-1],
               linestyles='dashed', colors='r')
    plt.hlines(avgval[1], spins[0], spins[len(spins)-1],
               linestyles='dashed', colors='b')
    plt.savefig(plotnames[k], bbox_inches='tight')
    # clear the plot for other calls
    plt.clf()
    print(avgval)

# plotInertialParameters(0, plotnames, axes, thetas)
# plotInertialParameters(1, plotnames, axes, thetas)
# plotInertialParameters(2, plotnames, axes, thetas)
