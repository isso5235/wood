from numpy.random import *
 
mu = [0, 0]
sigma = [[30, 20], [20, 50]]
 
values = multivariate_normal(mu, sigma, 10)

print(values)
 