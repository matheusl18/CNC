import numpy as np
import csv

def sistemaAumentado(x,y,dim):
  m = len(x)
  A = np.empty((dim,dim))
  b = np.empty((dim))
  soma = []
  for i in range(0,dim+2):
    aux = 0
    for k in range(0,m):
      aux = aux + x[k]**i
    soma.append(aux)

  for i in range(0,dim):
    for j in range(i,dim):
      A[i,j] = soma[i+j]
      if (i != j):
        A[j,i] = A[i,j]
  
  b = []
  for i in range(0,dim):
    aux = 0
    for k in range(0,m):
      aux = aux + y[k]*(x[k]**(i))
    b.append(aux)
  
  return A,b
      

x = []
y = []
with open('cnc02.csv') as f:
    r = csv.reader(f)
    for line in r:
        x.append(float(line[0]))
        y.append(float(line[1]))
A,b = sistemaAumentado(x,y,3)
print("A = ", A)
print("b = ", b)
coef = np.linalg.solve(A,b)
print("coef = ",coef)