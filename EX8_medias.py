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
            print " Voce nao inseriu um n�mero v�lido"
            '''sys.exit(-1)'''
notas.remove(-1)
media = sum(notas)/len(notas)    
print "a media � ", media
print "A maior nota �", max(notas)

#Nota: 1.1
#Comentario: Valia 1.0 mas dei +0.1 pelo uso de adicionais nao explicadas em aula
