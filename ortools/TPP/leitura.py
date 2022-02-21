# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:47:49 2021

@author: M.Pereira
"""
import sys
import pandas as pd
import numpy as np

def leitura(nome=None):
    arquivo = open(nome)
    for i in range(3):
        arquivo.readline()
        
    texto = arquivo.readline().split()
    
    num_cities = int(texto[2])
    
    distance = (np.zeros((num_cities,num_cities))).tolist()
    
    for i in range(3):
        arquivo.readline()
    
    x_vector = np.zeros(num_cities)
    y_vector = np.zeros(num_cities)
    for i in range(num_cities):
        texto = arquivo.readline().split()
        x_vector[i] = texto[1]
        y_vector[i] = texto[2]
        
    for i in range(num_cities):
        for j in range(num_cities):
            distance[i][j] = np.sqrt((x_vector[j]-x_vector[i])**2 + (y_vector[j]-y_vector[i])**2)


    arquivo.readline()
   
    num_deman = int(arquivo.readline())
 
    demanda = (np.zeros(num_deman)).tolist()
    
    for i in range(num_deman):
        texto = arquivo.readline().split()
        demanda[i] =int(texto[1])
    
    arquivo.readline()
    arquivo.readline()
    custo = (np.zeros((num_cities,num_deman))).tolist()
    prod = (np.zeros((num_cities,num_deman))).tolist()
    
    for i in range(1,num_cities):
        texto = arquivo.readline().split()
 
        for j in range(2,len(texto),3):

            custo[i][int(texto[j])-1] =int(texto[j+1])
            prod[i][int(texto[j])-1] =int(texto[j+2])
            
            
    return num_cities,num_deman,distance,demanda,custo,prod
