# 1. Imprime "Hola, mundo"

print( "Hola, mundo" )

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Donald"

print("Hola", nombre) # con una coma

print("Hola " + nombre) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 177

print("Hola", numero, "!" ) # con una coma

print("Hola " + str(numero) + " !") # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "hamburgers"

comida2 = "hot dogs"

print("Me encanta comer {} y {}!".format(comida1, comida2)) # con .format()

print(f"Me encanta comer {comida1} y {comida2}!") # con una cadena f