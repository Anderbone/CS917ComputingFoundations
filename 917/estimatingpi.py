### ALL CODE YOU SUBMIT SHOULD BE IN THIS FILE
### DO NO IMPORT AND USE ANY OTHER PACKAGES.


### Import the uniform and gauss (for normally distributed
### numbers) methods from the random pacakage
from random import uniform, gauss
"""
Name: Jiyu yan
ID: 1851015
"""

### Representation of a dart, with X and Y coordinates.
class Dart:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __str__(self):
        return "({0:.3f}..,{1:.3f}..)".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

### Euclidean distance of a given Dart object to the origin (0,0)
def distanceToOrigin(dart):
    return (dart.x**2 + dart.y**2) ** 0.5

### Generate and throw a dart in a uniform square from (-1,-1) to (1,1)
def throwUniformDart():
    return Dart(uniform(-1,1),uniform(-1,1))

### Generate and throw a dart normally distributed about the origin (std=0.6)
def throwNormalDart():
    mu = 0
    sigma = 0.6
    return Dart(gauss(mu,sigma),gauss(mu,sigma))

# Estimate pai by throwing 1000 darts uniformly
def pred_uniform():
    num_less = 0
    for i in range(1000):
        dart = throwUniformDart()
        if distanceToOrigin(dart) < 1:
            num_less += 1
    pred = 4 * num_less / 1000
    # print(pred)
    return pred

# Estimate pai by throwing 1000 darts normally
def pred_normal():
    num_less = 0
    for i in range(1000):
        dart = throwNormalDart()
        if distanceToOrigin(dart) < 1:
            num_less += 1
    pred = 4 * num_less / 1000
    return pred

# Compute the confident interval. n is the number of estimate.
def confident(n):
    ans = mean_sig(n)
    mean = ans[0]
    sig = ans[1]
    left = mean - 1.96 * sig/(n ** 0.5)
    right = mean + 1.96 * sig/(n ** 0.5)
    print("95 % confidence interval in {} estimates:[{:.3f}, {:.3f}]".format(n, left, right))

# Compute the mean and standard deviation of uniformly thrown from n estimates.
def mean_sig(n):
    all = []
    sum = 0
    for i in range(n):
        pred = pred_uniform()
        all.append(pred)
        sum += pred
    mean = sum / n
    # print(mean)
    temp_sum = 0
    for i in all:
        temp_sum += (i - mean) ** 2
    sig = (temp_sum / (n ** 0.5)) ** 0.5
    return mean, sig

# Compute the mean and standard deviation of normally thrown from n estimates.
def mean_sig2(n):
    all = []
    sum = 0
    for i in range(n):
        pred = pred_normal()
        all.append(pred)
        sum += pred
    mean = sum / n
    # print(mean)
    temp_sum = 0
    for i in all:
        temp_sum += (i - mean) ** 2
    sig = (temp_sum / (n ** 0.5)) ** 0.5
    return mean, sig


# Compute t-test from n estimates
def diff(n):
    ans1 = mean_sig(n)
    ans2 = mean_sig2(n)
    nom = abs(ans1[0] - ans2[0])
    dnom = (ans1[1] **2 /n + ans2[1]**2/n) ** 0.5
    t = nom/dnom
    print("t={:.3f} in {} estimates".format(t, n))
    return t


if __name__ == "__main__":

    pred = pred_uniform()
    print('estimate pai is {:.3f}'.format(pred))
    confident(5)
    confident(10)
    confident(100)
    confident(1000)
    diff(5)
    diff(10)
    diff(100)
    diff(1000)

