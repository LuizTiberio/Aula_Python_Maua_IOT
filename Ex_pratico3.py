# -*- coding: cp1252 -*-
import math

def distancia(p1,p2):
    aux = (p2[0]-p1[0])**2+(p2[1]-p1[1])**2
    dist= math.sqrt(aux)
    return dist

def angulograus(p1,p2):
  return math.atan2((p2[1]-p1[1]),(p2[0]-p1[0]))
 
    
p1=[]
p2=[]
p1.append(float( input("Por favor, digite o x do ponto 1:  ")))
p1.append(float( input("Por favor, digite o y do ponto 1:  ")))
p2.append(float( input("Por favor, digite o x do ponto 2:  ")))
p2.append(float( input("Por favor, digite o y do ponto 2:  ")))
modulo=distancia(p1,p2)
fase=angulograus(p1,p2)*(180/math.pi)
print ("modulo: "+ str(modulo))
print("fase em graus: "+ str(fase))
