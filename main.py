import numpy as np
import math

n = int(input("Enter number of elements: "))

x = []
y = []

sumx = 0
sumy = 0
sumxy = 0
sumxx = 0
sumyy = 0

xnumber = 1
ynumber = 1

for i in range(n):
    xvalue = int(input("Enter {}x coordinate: ".format(xnumber)))
    x.append(xvalue)
    xnumber += 1
    #print(x)

for i in range(n):
    yvalue = int(input("Enter {}y coordinate: ".format(ynumber)))
    y.append(yvalue)
    ynumber += 1
    #print(y)

for i in range(0, len(x)):
    sumx += x[i]

for i in range(0, len(y)):
    sumy += y[i]

#print(f"Total for x, {sumx}")
#print(f"Total for y, {sumy}")

x_array = np.array(x)
y_array = np.array(y)

xy_array = x_array * y_array
xy = xy_array.tolist()

xx_array = x_array * x_array
xx = xx_array.tolist()

yy_array = y_array * y_array
yy = yy_array.tolist()

for i in range(0, len(xy)):
    sumxy += xy[i]

for i in range(0, len(xx)):
    sumxx += xx[i]

for i in range(0, len(yy)):
    sumyy += yy[i]

#print(sumx, sumy, sumxy, sumxx, sumyy)

first = n*sumxy - sumx*sumy
second = n*sumxx - sumx*sumx
third = n*sumyy - sumy*sumy

r = first / math.sqrt(second * third)
print(f"Pearson correlation coefficient {r}")
