# -*- coding: cp1252 -*-
a=float(input("Por favor, digite o valor de A: "))
b=float(input("Por favor, digite o valor de B: "))
c=float(input("Por favor, digite o valor de C: "))

vet=[]
vet.append(a)
vet.append(b)
vet.append(c)
vet.sort()
if (vet[2]**2==vet[1]**2+vet[0]**2):
    area= (vet[1]*vet[0])/2
    print(" Trata-se de um tri�ngulo ret�ngulo!")
    print("Sua �rea � igual a: " + str(area))
else:
    print(" N�o � um tri�ngulo ret�ngulo! os valores lidos foram:  A={0}, B={1}, C={2}".format(a,b,c))      
