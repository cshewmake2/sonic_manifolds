#############
# The Torus #
#############

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Source: https://en.wikipedia.org/wiki/Torus
def torus(th, ph, R = 5, r = 1):
    '''
    Generates a torus with parameters:
    th - angle wrt tube
    ph - angle wrt torus
    R - distance from tube center to torus center
    r - radius of tubbe
    '''
    x = (R + r*np.cos(th))*np.cos(ph)
    y = (R + r*np.cos(th))*np.sin(ph)
    z = r*np.sin(th)
    return np.array([x,y,z])


# Define torus parameters
R = 5
r = 1

# ths = np.arange(0,360,10)
# phs = np.arange(0,360,10)

def plot_torus(R,r):
    ths = 2*np.pi*np.random.rand(1,1000)
    phs = 2*np.pi*np.random.rand(1,1000)
    pts = np.array([torus(th,ph,R,r) for th in ths for ph in phs])

    # Plot the torus
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(pts[:,0],pts[:,1],pts[:,2])
    plt.xlim(-8, 8)
    plt.ylim(-8, 8)
    ax.set_zlim(-4,4)
    plt.autoscale(False)
    return fig,ax
