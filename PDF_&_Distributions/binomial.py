# -*- coding: utf-8 -*-
"""Binomial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JfFEbTe-YsuIteF8RHgHcih_Q4WA9jIF
"""

from scipy.stats import binom
import matplotlib.pyplot as plt
# setting the values
# of n and p
n = 40
p0 = 0.05
p1= 0.20
p2= 0.5
p3= 0.8
p4= 0.95

# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance
mean, var = binom.stats(n, p)
# list of pmf values
dist0 = [binom.pmf(r, n, p0) for r in r_values ]
dist1 = [binom.pmf(r, n, p1) for r in r_values ]
dist2 = [binom.pmf(r, n, p2) for r in r_values ]
dist3 = [binom.pmf(r, n, p3) for r in r_values ]
dist4 = [binom.pmf(r, n, p4) for r in r_values ]
# printing the table
print("r\tp(r)")
for i in range(n + 1):
    print(str(r_values[i]) + "\t" + str(dist0[i]))
# printing mean and variance
print("mean = "+str(mean))
print("variance = "+str(var))

# plotting the graph
plt.bar(r_values, dist0)
plt.bar(r_values, dist1)
plt.bar(r_values, dist2)
plt.bar(r_values, dist3)
plt.bar(r_values, dist4)
plt.xlabel("n")
plt.ylabel("P(n)")
plt.title("Binomial Distribution")
plt.legend(['p=0.05','p=0.20','p=0.50','p=0.80','p=0.95'])
plt.show()