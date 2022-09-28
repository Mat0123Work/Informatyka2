plik = open('liczby.txt') 
dane = plik.read().split()
print(dane)

liczby = []

for i in range(0,len(dane)):
    liczby.append(int(dane[i]))
print(liczby)

'''
for dana in dane:
    liczby.append(int(dana))
print(liczby)
'''

import math
liczby = [int(x) for x in dane]


#potegi_3 = [3**x for x in range(11)]

potegi_3 = []
for i in range(0, 11):
    potegi_3.append(3**i)

print(potegi_3)


ile_poteg = 0
for liczba in liczby:
    if liczba in potegi_3:
        ile_poteg+=1
print(ile_poteg)


#Z4.2
def silnia(n):
    if n==0 or n==1:
        return 1
    elif n>=2:
        return n*silnia(n-1)
 
print(silnia(6))

def zad4_2():
    counter = []
    for i in range(0, len(dane)):
        sum = 0
        for digit in dane[i]:
            sum += silnia(int(digit))
        if sum == int(dane[i]):
            counter.append(dane[i])
    return counter


 
def liczba_elo(liczba):
    liczba_tekst = str(liczba)
    suma = 0
    for cyfra in liczba_tekst:
        suma += silnia(int(cyfra))
    if liczba==suma:
        return liczba
    else:
        return None
 
for liczba in liczby:
    if liczba_elo(liczba)!=None:
        print(liczba)
