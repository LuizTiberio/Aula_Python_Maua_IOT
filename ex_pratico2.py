# -*- coding: cp1252 -*-
import math

def distancia( x1,y1,x2,y2):
    aux = (x2-x1)**2+(y2-y1)**2
    dist= math.sqrt(aux)
    return dist

x=[]
y=[]
aux=0
DistanciaMaxima=0
aux2=0

while True:
    a=raw_input("Por favor, digite o X ou tecle ENTER para sair:  ")
    if a=="":
      break
    else:
     b=raw_input("Por favor, digite o Y:  ")
     x.append(float(a ))
     y.append(float(b ))
     aux+=1

for i in range(len(x)):
    for j in range(len(y)):
        aux2=distancia( x[j],y[j],x[i],y[i])
        if (aux2>DistanciaMaxima):
                    DistanciaMaxima=aux2
                
         
print(" A maior distância entre os pontos é: "+ str(DistanciaMaxima)
      )
