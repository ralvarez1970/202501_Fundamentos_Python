
class Usuario:

    def __init__(self, nome, sobrenome, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.saldo_pagar = 0

    def fazer_compra(self, valor):
        self.saldo_pagar += valor 
        return self

    def pagar_cartao(self, valor):
        self.saldo_pagar -= valor 
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario : {self.nome}, Saldo a pagar : {self.saldo_pagar}")

    def transferir_divida(self, outro_usuario, valor):
        self.saldo_pagar -= valor 
        outro_usuario.saldo_pagar += valor
        return self


joao = Usuario("Joao", "das Couves", "joao@gmail.com")
maria = Usuario("Maria", "Moraes", "maria@gmail.com")
pedro = Usuario("Pedro", "Moreira", "pedro@nada.com")


joao.fazer_compra(100).fazer_compra(300).pagar_cartao(200)
joao.mostrar_saldo_usuario()

maria.fazer_compra(600).pagar_cartao(200).pagar_cartao(175)
maria.mostrar_saldo_usuario()

pedro.fazer_compra(120).fazer_compra(125).fazer_compra(355).pagar_cartao(95).pagar_cartao(290).pagar_cartao(25).pagar_cartao(190)
pedro.mostrar_saldo_usuario()