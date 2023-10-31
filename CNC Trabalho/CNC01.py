import numpy as np
from numpy.linalg import inv
import csv

a = []
b = []
with open('cnc01.csv') as f:
    r = csv.reader(f)
    j = len(list(open('cnc01.csv')))
    for line in r:
        for row in line:
            if row == line[j]:
                b.append(int(row))
            else:
                a.append(int(row))
b = np.array(b)
a = np.reshape(a, (j, j))  
i = inv(a)
x = np.dot(i, b)
print(x)
