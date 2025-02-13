## R. Alvarez, Python Bootcamp, Jan 2025


## Exercicio 1

print ("Exercicio 1")
print ("###########")
for i in range (1, 101):
    print(i)
print ("###############################################################")
print()


## Exercicio 2

print ("Exercicio 2")
print ("###########")
for i in range (1, 501):
    if (i % 2 == 0):
        print(i)
print ("###############################################################")
print()


## Exercicio 3

print ("Exercicio 3")
print ("###########")
for i in range (1, 101):
    if (i % 10 == 0):
        print("baby")
    elif (i % 5 == 0):
        print("ice ice")
    else:
        print(i)
print ("###############################################################")
print ()


## Exercicio 4
print ("Exercicio 4")
print ("###########")
soma = 0
for i in range (1, 5000001):
    soma = soma + i
print ("Soma = " + str(soma))
print ("###############################################################")
print ()


## Exercicio 5
print ("Exercicio 5")
print ("###########")
for i in range (2024, 0, -3):
    print (i)
print ("###############################################################")
print ()


## Exercicio 6
print ("Exercicio 6")
print ("###########")
numInicial = 34
numFinal = 1056
multiplo = 3
for i in range (numInicial, numFinal):
    if (i % multiplo == 0):
        print (i)
print ("###############################################################")
print ()


