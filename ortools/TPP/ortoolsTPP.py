# -*- coding: utf-8 -*-
from ortools.linear_solver import pywraplp as otpl
from ortools.init import pywrapinit
import sys
import numpy as np
from leitura import leitura



n,m,c,demanda,custo,produto = leitura('CapEuclideo.5.5.tpp')

#resolvedor
solver = otpl.Solver.CreateSolver('CBC')


#cria variáveis do modelo
x = (np.zeros((n,n))).tolist()
y = (np.zeros(n)).tolist()
z = (np.zeros((n,m))).tolist()

u = (np.zeros(n)).tolist()

#inicializa variáveis
for i in range(n):
    
    for j in range(n):
        x[i][j] = solver.IntVar(0,1,'x[%i][%i]'%(i,j))
    
    y[i] = solver.IntVar(0,1,'y[%i]'%(i))
    

for k in range(m):
    maxq = 0
    
    for j in range(n):
        if maxq < produto[j][k]:
            maxq = produto[j][k]
    
    for i in range(n):
        z[i][k] = solver.IntVar(0,maxq,'z[%i][%i]'%(i,k))
        
        
        
u[0] = solver.IntVar(1,1,'u[0]')

for i in range(1,n):
    u[i] = solver.IntVar(2,n,'u[%i]'%(i))



#restrições de vizinho

for i in range(n):
    soma_x = []
    for j in range(n):
        soma_x.append(x[i][j])
    solver.Add(sum(soma_x) == y[i])

for j in range(n):
    soma_x = []
    for i in range(n):
        soma_x.append(x[i][j])
    solver.Add(sum(soma_x) == y[j])
    
for i in range(n):
    solver.Add(x[i][i]==0)
    
solver.Add(y[0] == 1)   

#Restrição de demanda

for k in range(m):
    soma_pro =[]
    for j in range(n):
        soma_pro.append(z[j][k])        
    
    solver.Add(sum(soma_pro) == demanda[k])
  
for j in range(n):
    for k in range(m):
        solver.Add(z[j][k] <= produto[j][k]*y[j])
 

#restrição de quebra de ciclo MTZ
for i in range(1,n):
    for j in range(1,n):
        if i !=j:        
            solver.Add(u[i] - u[j] - n*x[j][i] - (n-2)*x[i][j] >= -n+1)
        else:
            solver.Add(u[i] - u[j] == 0)

#função objetivo   
obj = []

for i in range(n):
    for j in range(n):
        obj.append(c[i][j]*x[i][j])

for j in range(1,n):
    for k in range(m):
        obj.append(custo[j][k]*z[j][k])
    



solver.Minimize(sum(obj))

status = solver.Solve()


print('Objective value =', solver.Objective().Value())

for j in range(n):
    print(y[j].name(), ' = ', y[j].solution_value())
print()

for i in range(n):
    for j in range(n):
        print(x[i][j].name(), ' = ', x[i][j].solution_value())
print()
for j in range(n):
    for k in range(m):
        print(z[j][k].name(), ' = ', z[j][k].solution_value())
        

print()
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())

    
    
    
    
    
    
    
    


