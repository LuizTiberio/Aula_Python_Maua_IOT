# -*- coding: cp1252 -*-
import math

def latitude(x,y):
    return math.atan2(y,x)

def LongAlt(x,y,z):
    count=0
    E=0.00669454185
    a=6378160
    h=0
    N=1
    P= math.sqrt(x**2+y**2)
    TangTheta= (z/P)*(1-E*(N/(N+h)))**-1
    theta=math.atan(TangTheta)
    while count<5:
        N=a/(math.sqrt(1-E*math.sin(theta)**2))
        h= (P/(math.cos(theta))-N)
        TangTheta= (z/P)*(1-E*(N/(N+h)))**-1
        count +=1
    theta=math.atan(TangTheta) 
    vetaux=[theta,h]
    return vetaux

x=float(input("Por favor, insira o X: "))
y=float(input("Por favor, insira o Y: "))
z=float(input("Por favor, insira o Z: "))
aux1=latitude(x,y)
vetor = LongAlt(x,y,z)

lati=math.degrees(aux1)
longi = math.degrees(vetor[0])
alt=vetor[1]*1000
print ("Latitude: {0}º, Longitude: {1}º, Altitude: {2}m".format(lati,longi,alt)) 
