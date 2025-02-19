## R. Alvarez, Python Bootcamp, Jan 2025
## Exercicio <core> "Tarjeta Credito com Usuarios"
## Class --> Usuarios
## Este é o "main", todas as classes e funções são chamadas a oartir daqui


# Importa a classe <CartaoCredito>

from cartao import CartaoCredito

# Define a classe <Usuarios>
# A lista de cartoes de cada usuario e armazenada em <self.cartoes>

class Usuarios:

# Construtor: cria usuarios 
# # Ele tambem inicializa a lista de cartoes de cada usuario

    def __init__(self, nome, sobrenome, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.saldo_pagar = 0
        self.cartoes = [] # Inicializa lista de cartoes do usuario criado
        self.cartao_a_usar = 0

# Este metodo cria cartoes, chamando a classe <CartaoCredito> 
# # Ele tambem atualiza a lista de cartoes de cada usuario usando <append> e guardando resultado em <self.cartoes>

    def criar_cartao (self, nome="", saldo=0, limite=20000, taxa=0.015): 
        novo_cartao = CartaoCredito(self, nome, saldo, limite, taxa)
        self.cartoes.append (novo_cartao) # Adiciona cartao a lista de cartoes do usuario
        print (f"Cartao criado para {self.nome} {self.sobrenome}: ", novo_cartao.nome) 
        return self

# Este metodo lista os cartoes do usuario

    def listar_cartoes_usuario (self):
        print (f"O usuario {self.nome} tem os seguintes cartoes: ")
        i = 0
        for cartoes in self.cartoes:
            print (f"{self.cartoes[i].nome}")
            i += 1
        return self

# Este metodo iterage com a lista de cartoes do usuario e mostra: (i) soldo de cada cartao e (ii) saldo todal

    def mostrar_saldo_usuario (self):
        i = 0
        saldo = 0
        print ()
        input (f"**** Aperte enter para imprimir os saldos dos cartoes de {self.nome} {self.sobrenome} ****")
        print ()
        print ("*****************************************")
        print (f"Saldo do usuario {self.nome} {self.sobrenome}")
        for cartao in self.cartoes:
            print (f"Saldo do cartao {cartao.nome}: {cartao.saldo_pagar}")
            saldo = saldo + (cartao.saldo_pagar)
        print(f"Usuario : {self.nome} | Saldo total a pagar : {saldo}")
        print ("*****************************************")
        return self

# Este metodo permite que o usuario selecione o cartao a utilizar em transacoes de compra a pagamento
# Optei por armazenar o valor de salecionado em cada instancia para poder (i) retornar <self> e (ii) encadear metodos

    def selecionar_cartao (self): 
        print ()
        i = 0
        selecao_valida = False
        escolha = 0
        tentativas = 0
        entrada_digito = False
        print ("******************************")
        print (f"Cartoes disponiveis para {self.nome}")
        for cartao in self.cartoes:
            print (f"[{i+1}] {self.cartoes[i].nome}")
            i += 1
        while selecao_valida == False:
            if escolha > 0 and escolha <= len(self.cartoes) and entrada_digito == True:
                selecionado = escolha - 1
                selecao_valida = True
            else:
                if (tentativas > 0):
                    print ("Selecao invalida!")
                entrada = input ("Selecione o cartão a utilizar: ")    
                if (entrada.isdigit()):
                    entrada_digito = True
                    escolha = int(entrada)
                tentativas += 1 
        print ()
        self.cartao_a_usar = selecionado
        return self
            


# Inicio do codihgo a ser executado 

print ()

# Cria instancias (usuarios: Joao, Maria e Pedro) e um cartoes (instancias de <CartaoCredito>) para cada um dos usuarios

joao = Usuarios("Joao", "das Couves", "joao@gmail.com")
joao.criar_cartao()

maria = Usuarios("Maria", "Moraes", "maria@gmail.com")
maria.criar_cartao()

pedro = Usuarios("Pedro", "Moreira", "pedro@nada.com")
pedro.criar_cartao()

# Cria cartoes adicionais (instancias de <CartaoCredito>)

print ()
maria.criar_cartao()
pedro.criar_cartao()
pedro.criar_cartao()
maria.criar_cartao()

# Lista os cartoes emitidos para cada usuario

print ()
joao.listar_cartoes_usuario()
print ()
maria.listar_cartoes_usuario()
print ()
pedro.listar_cartoes_usuario()

print ()

# Executa transacoes - Joao

cartao = joao.selecionar_cartao().cartoes[joao.cartao_a_usar].fazer_compra(100).fazer_compra(600).mostrar_informacao_cartao()

# Executa transacoes - Maria

maria.selecionar_cartao().cartoes[maria.cartao_a_usar].fazer_compra(1000).fazer_compra(1500).pagar_cartao(2000).mostrar_informacao_cartao().fazer_compra(333).mostrar_informacao_cartao()
maria.selecionar_cartao().cartoes[maria.cartao_a_usar].fazer_compra(750).fazer_compra(5000).fazer_compra(1200).mostrar_informacao_cartao()

# Executa transacoes - Pedro

pedro.selecionar_cartao().cartoes[pedro.cartao_a_usar].fazer_compra(800).fazer_compra(1200).pagar_cartao(1800).fazer_compra(22000).mostrar_informacao_cartao()

# Mostra os saldos de todos os usuarios

joao.mostrar_saldo_usuario ()
maria.mostrar_saldo_usuario ()
pedro.mostrar_saldo_usuario ()

# Imprime a lista de todos os cartões, usuarios e respectivos saldos

CartaoCredito.Imprime_Cartoes()