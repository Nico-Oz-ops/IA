import numpy as np

a = 2
b = 8
n_samples = 50000

samples = np.random.uniform(a, b, n_samples)

x = np.linspace(a,b,300)
pdf = np.ones_like(x) / (b-a)
