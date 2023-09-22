from DataNasc import DataNact


# Classe Pessoa, classe mais generica possível
# Vamos abstrair!

class Pessoa:
    # Conceito de construtor
    def __init__(self):
        # Conteição de abstração e atributos das classes
        self.__nome = ""
        self.__idade = 0
        self.irineu = ""
        self.data_nascimento = DataNact()

        # Atributos privados / conceito de encapsulamento
        self.__cpf = ""
        

    """ Como o conceito de encapsulamento impossibilita o acesso ao atributo entao
        Vamos definir getters e setters

    """

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

  
    # Definindo o get
    @property  
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    

    
