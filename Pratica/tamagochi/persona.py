## R. Alvarez, 2025
## Python bootcamp

from tamagotchi import Tamagotchi


class Persona:

    last_position = 0

    def __init__(self, nome, sobrenome, colecao=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.colecao = colecao if colecao is not None else []
        self.contador = 0

    def criar_tamagochi (self):
        print ()
        nome = input (f"Que nome terá o seu tamagotchi #{self.contador+1}? ").strip()
        cor = input ("Qual será a sua cor? ").strip()
        tamagotchi = Tamagotchi(self, nome, cor)
        self.colecao.append(tamagotchi)
        self.contador += 1

    def jogar_com_tamagotchi (self):
        tamagotchi = self.escolher_tamagotchi("jogar")
        Tamagotchi.jogar(tamagotchi)
        return self

    def dar_comida_tamagotchi (self):
        tamagotchi = self.escolher_tamagotchi("alimentar")
        Tamagotchi.comer(tamagotchi)
        return self

    def curar_tamagotchi (self):
        tamagotchi = self.escolher_tamagotchi("curar")
        Tamagotchi.curar(tamagotchi)
        return self
    
# A cada rodada, o usuario pode escolher qual acao realizar (jogar, alimentar, curar ou sair)

    def escolher_acao (self):
        end = False
        while end == False:
            print ()
            print (f"O que você gostaria de fazer?")
            print ("[1] Jogar com tamagotchi")
            print ("[2] Alimentar tamagotchi")
            print ("[3] Cuidar e curar tamagotchi")
            print ("[4] SAIR")
            escolha = 0
            entrada_digit = False
            while escolha < 1 or escolha > 4 or entrada_digit == False:
                entrada = input("Entre a sua opcao: ")
                if (entrada.isdigit()):
                    entrada_digit = True
                    escolha = int(entrada)
                if escolha == 1:
                    posicao = self.jogar_com_tamagotchi()
                    if Tamagotchi.kill == True:
                        del self.colecao[int(Persona.last_position)]
                elif escolha == 2:
                    self.dar_comida_tamagotchi()
                elif escolha == 3:
                    self.curar_tamagotchi()
                elif escolha == 4:
                    print ("******** END OF GAME ********")
                    print ()
                    end = True
        return self
    
# A cada rodada, o usuario pode escolher qual tamagotchi acionar

    def escolher_tamagotchi (self, acao):
        i = 1
        opcao = 0
        print ()
        print (f"Escolha em sua colecao! um tamagotchi para {acao} ------")
        print ("---------------------------------------------------------")
        for item in self.colecao:
            print (f"Tamagochi [{i}] | Nome: {item.name}")
            i += 1
        while (opcao < 1 or opcao > len(self.colecao)):
            opcao = int(input ("Entre o numero do tamagochi escolhido: "))
        tamagotchi = self.colecao[opcao-1]
        Persona.last_position = opcao-1
        return (tamagotchi)