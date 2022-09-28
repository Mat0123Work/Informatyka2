## funkcje
##  0   1  2  3  4
x = [1 ,2 ,3, 4]

def dodaj(a, b):
    return a + b

#x[0] -> 1
#x[1] -> 2

#x[0] + x[1] + ....

##c++ for(int i = 0; i<len(x); i++)

sum = 0
for number in range(0, len(x), 1):
    sum = dodaj(sum, x[number])

def ex():
    example = 42
    return x[0] + example

print(sum)















## -------- Z4.1

def isPowerOfThree(number):
    while(number % 3 == 0):
        number /= 3
    return number == 1

def zad4_1():
    counter = 0
    with open("przyklad.txt", mode='r', encoding='utf-8') as openedFile:
        for line in openedFile.readlines():
            if(isPowerOfThree(int(line))):
                counter+=1
    return counter

print(zad4_1())



## -------- Z4.2


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def silnia(n):
    if n==0 or n==1:
        return 1
    elif n>=2:
        return n*silnia(n-1)


##n*silnia(n-1) -> ...

#result = 1
#result *= 2
#result *= 3
#...
#5

## iteracja
#factorial(n) -> wynik

### Rekurencja:

#silnia(n) -> silnia(n-1)-> silnia(n-2) -> ... -> silnia(1)


#12\r\n
#15\r\n
#14\r\n
#12121

#01001010101011





def zad4_2():
    result = []
    with open("przyklad.txt", mode='r', encoding='utf-8') as openedFile:
        for line in openedFile.readlines():
            line = line.strip("\r\n")
            sum = 0
            for digit in line:
                sum += factorial(int(digit))
            if(sum == int(line)):
                result.append(line)
    return result

print(zad4_2())





    
