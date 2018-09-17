import numpy as np
import pylab as pl

#infile = open("../data/xy.dat", "r")

#This closes the file automatically after use
with open("../data/xy.dat", "r") as infile:
    x = []
    y = []
    for line in infile:
        # x_, y_ = [ float(w) for w in line.split() ]
        x_, y_ = np.array( line.split(), dtype = float) # Alternative formulation
        x.append(x_)
        y.append(y_)

# infile.close()

x = np.array(x)
y = np.array(y)

pl.plot(x,y)
pl.grid()

pl.show()
