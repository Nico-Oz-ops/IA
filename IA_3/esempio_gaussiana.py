import numpy as np
import matplotlib as plt
from scipy.stats import norm 

# Parametri della gaussiana
mu = 100
var = 10
sigma = np.sqrt(var)

# Asse x
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Densità della distribuzione normale
y = norm.pdf(x, mu, sigma)

# Grafico
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("densità")
plt.show()


#-----------------------------------

mu = 170
var = 10
x_soglia = 150

zz = norm.cdf(x_soglia, mu, var)
print(zz)y78