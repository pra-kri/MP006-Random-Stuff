# a quick inverse transform sampling example

# reference: https://am207.github.io/2017/wiki/inversetransform.html#box-muller-algorithm
# AM207 lecture series.


# PDF = probability distribution function
# CDF = cumulative distribution fuinction
# rand(0,1) = random uniform distribution, between 0 and 1.

# For a given PDF with a CDF, you get: CDF(PDF) = rand(0,1)
# So, if you do inverseCDF(rand(0,1)), you end up with the PDF.

import numpy as np
import matplotlib.pyplot as plt 



def PDF_1(x):
    """ 
    f(x) ~ exp(-x).
    We want to draw randomly from this distribution..."""
    return np.exp(-x)


def CDF_1(x):
    """ The CDF for f(x) ~ exp(-x)
    Can easily calculate by integrating the PDF.
    """
    return 1 - np.exp(-x)



def invCDF_1(y):
    """ Inverse CDF for PDF f(x) ~ exp(-x)
    """
    return -np.log(1-y)



# set some domain limits for x:
x_min = 0
x_max = 8

# find the limits of the CDF
y_min = CDF_1(x_min)
y_max = CDF_1(x_max)


print(x_min, x_max, y_min, y_max)


# Goal: We want to sample randomly from our PDF. But we dont have a function to do that.
# So instead, we will sample randomly from the uniform random distribution, then apply the inverse CDF to it.
# The end result will be a bunch of random samples that follow the PDF that we originally wanted.

random_uniform = np.random.uniform(y_min, y_max, 1000) #1000 samples, randomly distributed between (y_min, y_max)

inv_transformed = [invCDF_1(element) for element in random_uniform]


inv_transformed_mapped = map(invCDF_1, random_uniform)

print(inv_transformed_mapped[0:10])


real_values = np.linspace(x_min, x_max, 1000)
real_values1 = map(PDF_1, real_values)
real_values_scaled = [70*element for element in real_values1] # just a quick plot of the real distribution, scaled up a bit.
plt.plot(real_values,real_values_scaled)


plt.hist(inv_transformed_mapped, bins = 100, label = 'inverse-transformed samples')
plt.legend()
plt.show()

