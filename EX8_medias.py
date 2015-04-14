# -*- coding: cp1252 -*-
import sys
notas = []
nota=0;

while nota>=0:
    while True:
   
        try:
           nota = float(raw_input('insira a nota\n'))
           notas.append(nota)
           break;
        except:
            print " Voce nao inseriu um número válido"
            '''sys.exit(-1)'''
notas.remove(-1)
media = sum(notas)/len(notas)    
print "a media é ", media
print "A maior nota é", max(notas)
