

### Funcao 1
### Resultado previsto: 5
### Resultado --> ok

print ("Exercicio Funcao 1")
print ("###########")

def cantidad_de_vocales():

   return 5

print(cantidad_de_vocales())

print ("###############################################################")
print()



### Funcao 2
### Resultado previsto: Erro -- funcao vazia
### Resultado --> ok

print ("Exercicio Funcao 2")
print ("###########")

def cantidad_de_glaciares_argentina():

   return 16968

print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())


print ("###############################################################")
print()


### Funcao 3
### Resultado previsto: Erro -- funcao com dois valores retorno
### Resultado --> retorna 1810 e sai da funcao


print ("Exercicio Funcao 3")
print ("###########")


def anio_independencia_chile():

   return 1810

   return 1851

print(anio_independencia_chile())


print ("###############################################################")
print()


### Funcao 4
### Resultado previsto: 32
### Resultado --> ok

print ("Exercicio Funcao 4")
print ("###########")


def cantidad_de_departamentos_colombia():

   return(32)

   print(33)

print(cantidad_de_departamentos_colombia())


print ("###############################################################")
print ()


## Funcao 5
### Resultado previsto: 2438 // 0
### Resultado --> 2438 // none --> a funcao nao retorna nada

print ("Exercicio Funcao 5")
print ("###########")


def altura_machu_picchu():

   print(2438)

x = altura_machu_picchu()

print(x)

print ("###############################################################")
print ()


## Funcao 6
### Resultado previsto: 157
### Resultado --> 15 // 7 + Erro - unsuported operand

print ("Exercicio Funcao 6")
print ("###########")

def suma(a, b):

   print(a+b)

print(suma(10, 5) + suma(4, 3))

print ("###############################################################")
print ()


## Funcao 7
### Resultado previsto: 715
### Resultado --> ok

print ("Exercicio Funcao 7")
print ("###########")

def concatenar(a, b):

   return str(b) + str(a)

print(concatenar(7, 15))

print ("###############################################################")
print ()


## Funcao 8
### Resultado previsto: 560 // 46
### Resultado --> ok

print ("Exercicio Funcao 8")
print ("###########")

def paises_latinoamerica_o_lenguas_indigenas():

   a = 560

   print(a)

   if a < 180:

       return 33

   else:

       return 46

   return 21

print(paises_latinoamerica_o_lenguas_indigenas())

print ("###############################################################")
print ()


## Funcao 10
### Resultado previsto: 7
### Resultado --> ok

print ("Exercicio Funcao 10")
print ("###########")

def sumatoria(a, b):

   return a + b

   return 157

print(sumatoria(3, 4))

print ("###############################################################")
print ()


## Funcao 11
### Resultado previsto: 150 // 150 // 350 // 150 --> variavel na funcao e "interna"
### Resultado --> ok

print ("Exercicio Funcao 11")
print ("###########")

a = 150

print(a)

def funcion():

   a = 350

   print(a)

print(a)

funcion()

print(a)

print ("###############################################################")
print ()




## Funcao 13
### Resultado previsto: 150 // 150 // 350 // 350
### Resultado --> ok

print ("Exercicio Funcao 13")
print ("###########")

a = 150

print(a)

def funcion():

   a = 350

   print(a)

   return a

print(a)

a = funcion()

print(a)

print ("###############################################################")
print ()


## Funcao 14
### Resultado previsto: 3 // 1 // 2
### Resultado --> ok

print ("Exercicio Funcao 14")
print ("###########")

def funcion1():

   print(3)

   funcion2()

   print(2)

def funcion2():

   print(1)

funcion1()

print ("###############################################################")
print ()


## Funcao 15
### Resultado previsto: 3 // 1 // 0 // 4
### Resultado --> ok

print ("Exercicio Funcao 15")
print ("###########")

def funcion1():

   print(3)

   a = funcion2()

   print(a)

   return 4

def funcion2():

   print(1)

   return 0

b = funcion1()

print(b)

print ("###############################################################")
print ()