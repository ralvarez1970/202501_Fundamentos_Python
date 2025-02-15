## R. Alvarez, Python Bootcamp, Jan 2025
## Exercicio <core> "Tarjet Credito"


class CartaoCredito:

# Estas sao variaveis gerais da classe, usadas para contar cartoes e criar uma lista com a qual seja possivel iteragir

    contador_cartoes = 0
    lista_cartoes =[]

# Este construtor cria 'automaticamente' o nome do cartao de forma serial, com base no numero de cartoes emitidos
# Ele tambem adiciona (append) o cartao criado a lista geral de cartoes

    def __init__(self, nome="", saldo_pagar=0, limite_credito=1000, taxa_juros=0.02):
        self.nome = f"cartao_{CartaoCredito.contador_cartoes+1}"
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
            print (f"Compra aprovada para {self.nome}. Valor = {valor}")
        else:
            print (f"Compra negada para {self.nome}. Valor = {valor}. Motivo: limite insuficiente")
        return self

    def pagar_cartao(self, valor):
        self.saldo_pagar -= valor 
        return self

    def mostrar_informacao_cartao(self):
        print(f"Saldo a pagar {self.nome}: {self.saldo_pagar}")
        return self

    def cobrar_juros(self):
        self.saldo_pagar = round(self.saldo_pagar * (1+self.taxa_juros), 2)
        return self
    
# Este <class method> usa a lista geral de cartoes e iterage para imprimir as informacoes (valores do parametros) de cada cartao

    @classmethod
    def Imprime_Cartoes(cls):
        for cartao in CartaoCredito.lista_cartoes:
            print ()
            print ("*****************************************")
            print ("Cartao:", cartao.nome)
            print ("Saldo a pagar:", cartao.saldo_pagar)
            print ("Limite:", cartao.limite_credito)
            print ("Limite disponivel:", round(float(cartao.limite_credito) - cartao.saldo_pagar, 2))
            print ("*****************************************")

# Criaca das tres instancias --> tres cartoes

cartao_1 = CartaoCredito()
cartao_2 = CartaoCredito()
cartao_3 = CartaoCredito()

# Os comandos abaixo executam as transacoes com os cartoes
# Inclui prints das transacoes de compras tentadas/realizadas

print ()
print (f"Transacoes do {cartao_1.nome}")
print ("*****************************************")
cartao_1.fazer_compra(150).fazer_compra(320).pagar_cartao(270).cobrar_juros().mostrar_informacao_cartao()
print ()

print ()
print (f"Transacoes do {cartao_2.nome}")
print ("*****************************************")
cartao_2.fazer_compra(700).fazer_compra(50).fazer_compra(200).pagar_cartao(100).pagar_cartao(500).cobrar_juros().mostrar_informacao_cartao()

print ()
print (f"Transacoes do {cartao_3.nome}")
print ("*****************************************")
cartao_3.fazer_compra(150).fazer_compra(320).fazer_compra(320).fazer_compra(320).fazer_compra(320).cobrar_juros().mostrar_informacao_cartao()

# O comando abaixo cahama o <class method> para imprimir as informacoes (parametors) de cada instancia

CartaoCredito.Imprime_Cartoes()