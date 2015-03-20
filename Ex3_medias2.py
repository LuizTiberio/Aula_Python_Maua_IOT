# -*- coding: cp1252 -*-
notas = []
nota = float(raw_input('insira a nota\n'))

while nota >= 0:
    notas.append(nota)
    nota = float(raw_input('insira a nota\n'))

media = sum(notas)/len(notas)    
print ' a media é ', media

