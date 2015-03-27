import math

def distancia( p1,p2):
    aux = (p2[0]-p1[0])**2+(p2[1]-p1[1])**2
    dist= math.sqrt(aux)
    return dist


p1=[]
p2=[]
p1.append(float( input("Por favor, digite o x do ponto 1:  ")))
p1.append(float( input("Por favor, digite o y do ponto 1:  ")))
p2.append(float( input("Por favor, digite o x do ponto 2:  ")))
p2.append(float( input("Por favor, digite o y do ponto 2:  ")))
print(distancia(p1,p2))
