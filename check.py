import matplotlib.pyplot as plt
import math
import scipy.optimize as scp
from scipy.optimize import curve_fit
import numpy as np

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
y9 = []
y10 = []
y_av = []
unc = []
logx = []
logy = []

with open('data1.txt', 'r') as data_file:
    for line in data_file:
        lines = [i for i in line.split()]
        x.append(float(lines[0]))
        y1.append(float(lines[1]))
        y2.append(float(lines[2]))
        y3.append(float(lines[3]))
        y4.append(float(lines[4]))
        y5.append(float(lines[5]))
        y6.append(float(lines[6]))
        y7.append(float(lines[7]))
        y8.append(float(lines[8]))
        y9.append(float(lines[9]))
        y10.append(float(lines[10]))

# print(x)
# print(x)
# print(y1)
# print(y2)
# print(y3)
# print(y4)
# print(y5)
# print(y6)
# print(y7)
# print(y8)
# print(y9)
# print(y10)

length = len(x)
dof = length - 2

for i in range(0, length, 1):
    y_av.append(float((y1[i] + y2[i] + y3[i] + y4[i] + y5[i] + y6[i] + y7[i] + y8[i] + y9[i] + y10[
        i]) / 10))  # Need to find way to generalize # of y data sets

# print(length)
# print(y_av)

plt.title("Test")
plt.xlabel('xdata')
plt.ylabel('ydata')
plt.yticks(y_av)
plt.plot(x, y_av, marker='o', c='g')

plt.show

for i in range(0, length, 1):
    unc.append(math.sqrt(((y1[i] - y_av[i]) ** 2 + (y2[i] - y_av[i]) ** 2 + (y3[i] - y_av[i]) ** 2 + (
                y4[i] - y_av[i]) ** 2 + (y5[i] - y_av[i]) ** 2 + (y6[i] - y_av[i]) ** 2 + (y7[i] - y_av[i]) ** 2 + (
                                      y8[i] - y_av[i]) ** 2 + (y9[i] - y_av[i]) ** 2 + (y10[i] - y_av[i]) ** 2) / 10))


# print(unc)

def power_fit(x, A, p):
    return A * x ** p


plt.errorbar(x, y_av, yerr=unc, fmt='ko', label='data')

(params, cov) = scp.curve_fit(power_fit, x, y_av, sigma=unc)

# print(params)
# print(cov)

param_err = np.sqrt(np.diagonal(cov))
# print(param_err)

A1 = params[0]
a1_err = param_err[0]
p1 = params[1]
p1_err = param_err[1]

# print(A1)
# print(A1_err)
# print(p1)
# print(p1_err)


plt.plot(x, power_fit(x, *params), 'r--')

chi_sq = np.sum(((y_av - A1 * x ** p1) / unc) ** 2)
# print(chi_sq)
chi_sq_red = chi_sq / dof


# print(chi_sq_red)

def chi_square_ols(A, p):
    # power = np.power(x,p)
    # model = np.multiply(power,A)
    # model=A*x**p
    model = A * np.power(x, p)
    return np.sum((np.power(y_av - model, 2)))


x0 = [1.00, 1.00]
args = [x, y_av]
min_chi = scp.minimize(chi_square_ols, x0=x0, args=args)

print(min_chi)



