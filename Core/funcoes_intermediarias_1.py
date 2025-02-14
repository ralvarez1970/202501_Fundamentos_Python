## R. Alvarez, Python Bootcamp, Jan 2025



matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes1 = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

############## Parte 1
##### Tasks
# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
# En ciudades, cambia “Cancún” por “Monterrey”
# En las coordenadas, cambia el valor de “latitud” por 9.9355431


print ("#################")
print ("Parte 1")
print ()

matriz[1][0] = 6
print (matriz)

cantantes1[0]["nombre"] = "Enrique Martin Morales"
print(cantantes1)

ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

print ()
print ()

############## Parte 2
##### Tasks
# Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondient

print ("#################")
print ("Parte 2")
print ()

cantantes2 = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

def iterarDiccionario (cantantes):
    for i in range (len(cantantes)):
        print (f"nombre  -  {cantantes[i]["nombre"]}, pais  -  {cantantes[i]["pais"]}")

iterarDiccionario (cantantes2)

print ()
print ()

############## Parte 3
##### Tasks
# Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista.


print ("#################")
print ("Parte 3")
print ()

def iterarDiccionario2(chave, lista):
        for i in range (len(lista)):
            print (f"{cantantes2[i][chave]}")

chave = input("Qual chave devo usar? ")

while (chave != "nombre" and chave != "pais"):
     print ("Entrada invalida. Esta funcao somente aceita as seguintes chaves: 'nombre' e 'pais'.")
     print ("Você precisa entrar outra chave para continuar")
     chave = input("Qual chave devo usar? ")

iterarDiccionario2(chave, cantantes2)
print ()
print ()

############## Parte 4
##### Tasks
# Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.

print ("#################")
print ("Parte 4")
print ()

costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

def imprimirInformacao(dicionario):
     for chave in dicionario.keys():
        print(len(dicionario[chave]), chave.upper())
        print ()
        for i in range (0, len(dicionario[chave])):
             print (dicionario[chave][i])
             print ()

imprimirInformacao(costa_rica)