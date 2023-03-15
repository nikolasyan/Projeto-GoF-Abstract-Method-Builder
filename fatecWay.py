from abc import ABC, abstractmethod
class Pedido:
    def __init__(self):
        self.carnes = []
        self.paes = []
        self.queijos = []
        self.vegetais = []
        self.molhos = []

    def add_carne(self, carne):
        self.carnes.append(carne)

    def add_pao(self, pao):
        self.paes.append(pao)

    def add_queijo(self, queijo):
        self.queijos.append(queijo)

    def add_vegetal(self, vegetal):
        self.vegetais.append(vegetal)

    def add_molho(self, molho):
        self.molhos.append(molho)

    def __str__(self):
        return f"Resumo do pedido: {', '.join(self.carnes)} no pão {', '.join(self.paes)} com queijo {', '.join(self.queijos)}, {', '.join(self.vegetais)}, acompanhado com os molhos {', '.join(self.molhos)}."


class PedidoBuilder:
    def __init__(self):
        self.pedido = Pedido()

    def add_carne(self, carne):
        self.pedido.add_carne(carne)
        return self

    def add_pao(self, pao):
        self.pedido.add_pao(pao)
        return self

    def add_queijo(self, queijo):
        self.pedido.add_queijo(queijo)
        return self

    def add_vegetal(self, vegetal):
        self.pedido.add_vegetal(vegetal)
        return self

    def add_molho(self, molho):
        self.pedido.add_molho(molho)
        return self

    def build(self):
        return self.pedido
class Opcao:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome



def atendimento():
    builder = PedidoBuilder()

    print("Bem-vindo à lanchonete FATEC Way! Monte o seu lanche: \n")
    print("-----------------------------------------------------------")
    print("Opções de carne:")
    print("1 - Carne")
    print("2 - Frango")
    print("3 - Linguiça")
    print("4 - Vegetariano")
    print("-----------------------------------------------------------")

    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 1:
        builder.add_carne("Carne")
    elif opcao == 2:
        builder.add_carne("Frango")
    elif opcao == 3:
        builder.add_carne("Linguiça")
    elif opcao == 4:
        builder.add_carne("Vegetariano")
    print("-----------------------------------------------------------")
    print("Opções de pão:")
    print("1 - Parmesão e Orégano")
    print("2 - 9 Grãos")
    print("3 - Italiano")
    print("-----------------------------------------------------------")
    
    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 1:
        builder.add_pao("Parmesão e Orégano")
    elif opcao == 2:
        builder.add_pao("9 Grãos")
    elif opcao == 3:
        builder.add_pao("Italiano")

    print("-----------------------------------------------------------")
    print("Opções de queijo:")
    print("1 - Cheddar")
    print("2 - Suíço")
    print("3 - Muçarela")
    print("-----------------------------------------------------------")

    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 1:
        builder.add_queijo("Cheddar")
    elif opcao == 2:
        builder.add_queijo("Suíço")
    elif opcao == 3:
        builder.add_queijo("Muçarela")

    print("-----------------------------------------------------------")
    print("Opções de vegetais:")
    print("1 - Azeitona")
    print("2 - Alface")
    print("3 - Tomate")
    print("-----------------------------------------------------------")


    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 1:
        builder.add_vegetal("Azeitona")
    elif opcao == 2:
        builder.add_vegetal("Alface")
    elif opcao == 3:
        builder.add_vegetal("Tomate")

    print("-----------------------------------------------------------")
    print("Opções de molhos:")
    print("1 - Barbecue")
    print("2 - Chipotle")
    print("3 - Supreme")
    print("-----------------------------------------------------------")

    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 1:
        builder.add_molho("Barbecue")
    elif opcao == 2:
        builder.add_molho("Chipotle")
    elif opcao == 3:
        builder.add_molho("Supreme")

    pedido = builder.build()

    print("Seu pedido: \n")
    print(pedido)

    print("\nObrigado pela preferência! Volte sempre!")

  
while True:
  opcao = input("Digite 'S' para iniciar o atendimento ou 'Q' para sair: ")
  if opcao == "S":
    atendimento()
  elif opcao == "Q":
    break
  else:
    print("Opção inválida.")

