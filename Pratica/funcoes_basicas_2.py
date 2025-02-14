################################
################################################################ Funcao 1

print ()
print ("###############")
print ("Funcao 1")
print ("###############")
print ()

def multiplica2x (numero):
    for i in range (2, numero+1):
        print (i * 2)

valor = int(input ("Entre o valor desejado: "))
print (valor)
multiplica2x (valor)
print ()

################################
################################################################ Funcao 2

print ()
print ("###############")
print ("Funcao 2")
print ("###############")
print ()

def soma_e_resta (n1, n2):
    print (n1 + n2)
    return (n1-n2)

valor1 = int(input ("Entre o valor desejado do primeiro numero: "))
valor2 = int(input ("Entre o valor desejado do segundo numero: "))
print (soma_e_resta(valor1, valor2))
print ()


################################
################################################################ Funcao 3
print ()
print ("###############")
print ("Funcao 3")
print ("###############")
print ()


def entra_numeros (tam): # Esta es una funcion de uso genral, la utilizo en distintos ejercicios abajo.
    numerais = []
    for i in range (0, tam):
        numero = int(input (f"Entre o valor desejado do {i+1}o numero: "))
        numerais.append(numero)
    return (numerais)

def soma_menos_length (lista_numeros):
    soma = 0
    for i in range (0, len(lista_numeros)):
        soma = soma + int(lista_numeros[i])
    tamanho = len (lista_numeros)
    print ("Soma =", soma)
    print ("Tamanho =", tamanho)
    return (soma-tamanho)

tam = int(input("Entre quantos nuumeros tera a serie: "))
lista=entra_numeros(tam)
print("Resultado: " + str(soma_menos_length(lista)))
print ()


################################
################################################################ Funcao 4
print ()
print ("###############")
print ("Funcao 4")
print ("###############")
print ()

def valor_multiplicado_segundo (lista_numeros):
    if (len(lista_numeros)<2):
        print ("Tamanho inválido, menor que dois elementos")
        return ([])
    else:
        multiplicador = lista_numeros[1]
        for i in range (0, len(lista_numeros)):
            lista_numeros[i] = lista_numeros[i] * multiplicador
        tamanho = len (lista_numeros)
        print ("Multiplicador =", multiplicador)
        print ("Tamanho =", tamanho)
    return (lista_numeros)


tam = int(input("Entre quantos nuumeros tera a serie: "))
lista = entra_numeros(tam)
print ("Nova lista: ", valor_multiplicado_segundo(lista))
print ()


################################################################
############ Funcao 5
print ()
print ("###############")
print ("Funcao 5")
print ("###############")
print ()

def valor_multiplicado_tamanho (tam, val):
    lista = []
    for i in range (0, tam):
            lista.append(tam*val)
    return (lista)


tamanho = int(input ("Entre o tamanho da lista: "))
valor = int(input ("Entre o valor: "))

print ("List criada: ", valor_multiplicado_tamanho(tamanho, valor))
print ()