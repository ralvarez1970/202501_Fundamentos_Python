## R. Alvarez, Python Bootcamp, Jan 2025
## Exercicio <core> "Tarjeta Credito com Usuarios"
## Class --> CartaoCredito

class CartaoCredito:

# Estas sao variaveis gerais da classe, usadas para contar cartoes e criar uma lista com a qual seja possivel iteragir

    contador_cartoes = 0
    lista_cartoes =[]

# Este construtor cria 'automaticamente' o nome do cartao de forma serial, com base no numero de cartoes emitidos
# Ele tambem adiciona (append) o cartao criado a lista geral de cartoes

    def __init__(self, owner, nome="", saldo_pagar=0, limite_credito=1000, taxa_juros=0.02):
        self.owner = owner
        self.nome = f"cartao_00{CartaoCredito.contador_cartoes+1}"
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.taxa_juros = taxa_juros
        CartaoCredito.contador_cartoes +=1
        CartaoCredito.lista_cartoes.append(self)

# Este metodo esta diferente do solicitado no exercicio <core>, pois inclui um <if> para autorizar/nao a transacao com base no saldo disponivel
# O metodo geral (display no terminal) o resultado de cada transacao

    def fazer_compra(self, valor):
        if (self.limite_credito>(self.saldo_pagar+valor)):
            self.saldo_pagar += valor 
            print (f"Compra aprovada para {self.nome}. Valor = R$ {valor}")
        else:
            print (f"Compra negada para {self.nome}. Valor = R$ {valor}. Motivo: limite insuficiente")
        return self

    def pagar_cartao(self, valor):
        self.saldo_pagar -= valor 
        print (f"Pagamento realizado {self.nome} | {self.owner.nome}. Valor = R$ {valor}")
        return self

    def mostrar_informacao_cartao(self):
        print(f"Saldo a pagar {self.nome} | {self.owner.nome} {self.owner.sobrenome}: R$ {self.saldo_pagar}")
        return self

    def cobrar_juros(self):
        self.saldo_pagar = round(self.saldo_pagar * (1+self.taxa_juros), 2)
        return self
        

# Este <class method> usa a lista geral de cartoes e iterage para imprimir as informacoes (valores do parametros) de cada cartao

    @classmethod
    def Imprime_Cartoes(cls):
        print ()
        input ("**** Aperte enter para imprimir os cartões e saldos ****")
        for cartao in CartaoCredito.lista_cartoes:
            print ()
            print ("*****************************************")
            print ("Cartao:", cartao.nome)
            print (f"Usuario: {cartao.owner.nome} {cartao.owner.sobrenome}")
            print ("Saldo a pagar: R$", round(float(cartao.saldo_pagar), 2))
            print ("Limite: R$", round(float(cartao.limite_credito), 2))
            print ("Limite disponivel: R$", round(float(cartao.limite_credito) - cartao.saldo_pagar, 2))
            print ("*****************************************")
            print ()


