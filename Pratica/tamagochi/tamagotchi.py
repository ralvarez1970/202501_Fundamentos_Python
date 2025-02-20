## R. Alvarez, 2025
## Python bootcamp


class Tamagotchi:

    kill = False
    tamagotchi_counter = 0

    def __init__(self, owner, nome, cor, saude=20, felicidade=20, energia=20):
        self.owner = owner
        self.name = nome
        self.cor = cor
        self.saude = saude
        self.felicidade = felicidade
        self.energia = energia
        Tamagotchi.tamagotchi_counter += 1

    def jogar (self):
        Tamagotchi.kill = False
        self.felicidade += 10
        if (self.saude > 5):
            self.saude -= 5
        else:
            print (f"****** ATENÇÃO ****** | Seu tamagotchi {self.name} morreu!!!")
            Tamagotchi.kill = True
        return self

    def comer (self):
        print ()
        print (f"Alimentando o Tagagochi {self.name}")
        self.felicidade += 5
        self.saude -= 10
        return self

    def curar (self):
        print ()
        print (f"Cuidando e curando o Tagagochi {self.name}")
        self.felicidade -= 5
        self.saude += 20
        return self
    
    def reportar (self):
        print ()
        print ("***********************")
        print (f"Tamagochi: {self.name}| Owner: {self.owner.name}")
        print (f"Saúde: {self.saude}")
        print (f"Felicidade: {self.felicidade}")
        print (f"Tamagotchis criados: {Tamagotchi.tamagotchi_counter}")
        print ("***********************")
        return self