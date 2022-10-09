#naive method multiplying two matrices usin nested loops

#2x2 matrix "x"
x = [[1,2],[2,3]]

#2x2 matrix "y"
y = [[2,3],[3,4]]

#matriz salida
m = [[0,0],[0,0]]

#iterar through rows of x
for i in range(len(x)):
  #iterar through colums of Y
  for j in range(len(y[0])):
    #iterar through rows of Y
    for k in range(len(y)):
      m[i][j] += x[i][k] * y[k][j]


for end in m:
  print(m)