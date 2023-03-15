from abc import ABC, abstractclassmethod


class Pessoa(ABC):
    @abstractclassmethod
    def relacao_com_fatec(self):
        pass

class Aluno(Pessoa):
    def relacao_com_fatec(self):
        return "Aluno"

class Professor(Pessoa):
    def relacao_com_fatec(self):
        return "Professor"

class Coordenador(Pessoa):
    def relacao_com_fatec(self):
        return "Coordenador"
    
class Diretor(Pessoa):
    def relacao_com_fatec(self):
        return "Diretor"

class Administrativo(Pessoa):
    def relacao_com_fatec(self):
        return "Administrativo"
    
class Vestibulando(Pessoa):
    def relacao_com_fatec(self):
        return "Vestibulando"

class PessoaFactory:
 
    
    def criar_pessoa(relacao):
        if relacao == "Aluno":
            return Aluno()
        elif relacao == "Professor":
            return Professor()
        elif relacao == "Coordenador":
            return Coordenador()
        elif relacao == "Diretor":
            return Diretor()
        elif relacao == "Administrativo":
            return Administrativo()
        elif relacao == "Vestibulando":
            return Vestibulando()
        else:
            return None
          
    def menu():
        print('\n*------------------------*')
        print ('| 1 -- Aluno             |' )
        print ('| 2 -- Professor         |' )
        print ('| 3 -- Coordenador       |' )
        print ('| 4 -- Diretor           |' )
        print ('| 5 -- Administrativo    |' )
        print ('| 6 -- Vestibulando      |' )
        print('*------------------------*')
  
        option = input('\nEscolha sua relação com a FATEC: ')
      
        if option == "1":
            relacao = "Aluno"
        elif option == "2":
            relacao = "Professor"
        elif option == "3":
            relacao = "Coordenador"
        elif option == "4":
            relacao = "Diretor"
        elif option == "5":
            relacao = "Administrativo"
        elif option == "6":
            relacao = "Vestibulando"
        else:
            print("\n\n Opção invalida!")
            return None
        return relacao

sair = "C"
while(sair != "S"):
  nome = input("Bem-vindo ao sistema! Digite o seu nome: ")
  relacao = PessoaFactory.menu()
  pessoa = PessoaFactory.criar_pessoa(relacao)
  
  if pessoa:
      print("\n\nOlá, " + nome + "! você tem relação com a instituição como " + pessoa.relacao_com_fatec())
      import fatecWay

  else:
      print("\n\n" + nome + " não tem nenhuma relação com a instituição, acompanhar até a secretaria")
  sair = input("\nDigite S para sair, ou qualquer outro caractere para continuar.")