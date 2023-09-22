from Pessoa import Pessoa

# Exemplo de herança
class Medico(Pessoa):

    # Ou seja, Medico possui tudo que uma Pessoa comum têm
    def __init__(self):
        super().__init__()
        self.__especializacao = ""
        self.__num_registro = ""

    # GETTERS
    @property
    def especializacao(self):
        return self.__especializacao
    
    # SETTERS
    @especializacao.setter
    def especializacao(self, especializacao):
        self.especializacao = especializacao


    @property
    def numRegistro(self):
        return self.__num_registro
    

    @numRegistro.setter
    def numRegistro(self, numRegistro):
        self.numRegistro = numRegistro



    def cadastrarMedico(self, nome, idade, dia, mes, ano, cpf, especializacao, num_registro):
        self.__nome = nome
        self.data_nascimento.dia = dia
        self.data_nascimento.mes = mes
        self.data_nascimento.ano = ano
        self.__idade = idade
        self.__cpf = cpf
        self.__especializacao = especializacao
        self.__num_registro = num_registro

        return {
            "nome": self.__nome,
            "idade": self.__idade,
            "data_nascimento": self.data_nascimento.formarDataNascimento(),
            "cpf": self.__cpf,
            "especializacao": self.__especializacao,
            "num_registro": self.__num_registro
            
        }



        

    

    