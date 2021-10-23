# -*- coding: utf-8 -*-

'''
## 0-1 Knapsack problem

max c_1*x_1 + c_2*x_2 + . . . + c_n*x_n

subject to:
    
    a_1*x_1 + a_2*x_2 + ... + a_n*x_n <= b
    
    
    x_j in {0,1} for all j=1,...,n
    


REFERENCE : Wolsey, A. - Integer programming - Wiley-Interscience publication -
1998
'''

'''
O modelo foi implementado de forma generalizada
para utilizar qualquer instância basta adicionar a esta implementação uma função
para a leitura dos dados 
'''



from ortools.linear_solver import pywraplp as otpl
from ortools.init import pywrapinit
import gurobipy as gp
import sys
import pandas as pd
import numpy as np



## DADOS DE ENTRADA

c = [12,8,17,11,6,2,2]

a = [4,3,7,5,3,2,3]

b = 9


solver = otpl.Solver.CreateSolver('GUROBI')


x = (np.zeros(len(c))).tolist()

for i in range(len(c)):
    x[i] = solver.IntVar(0,1,'x({})'.format(i+1))

#Função objetivo

solver.Maximize(sum(c[i]*x[i] for i in range(len(c))))

#restrição

solver.Add(sum(a[i]*x[i] for i in range(len(c))) <= b)

status = solver.Solve()


if status == otpl.Solver.OPTIMAL:
    print('Objective value =', solver.Objective().Value())
    for i in range(len(c)):
        print(x[i].name(),'  ',x[i].solution_value())
    print()
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())
    print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
else:
    print('The problem does not have an optimal solution.')













