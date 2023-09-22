# Classe Principal
from Medico import Medico
medic = Medico()

def menu():
 
    dados = []

    while(True):
        print("-- Bem vindo ao sistema de cadastro médico orientado a objetos --")
        print("Selecione sua opção: ")
        print("[1] Cadastrar médico")
        print("[2] Visualizar os médicos cadastrados no hospital")
        print("[0] Sair do programa")
        opc = int(input("Selecione a opção que deseja: "))
        
        if(opc == 1):
            #cadastrar os médicos´
            nome = input("Insira o nome: ")
            idade = input("Insira a idade: ")
            print("\n-- Data de nascimento --")
            dia = input("Insira o dia: ")
            mes = input("Insira o mês: ")
            ano = input("Insira o ano: ")
            cpf = input("Insira o CPF: ")
            especializacao = input("Insira a especialização do médico: ")
            num_registro = input("O número de registro do médico: ")

            # Cadastro do médico
            dados.append(medic.cadastrarMedico(nome, idade, dia, mes, ano, cpf, especializacao, num_registro))
            print("Dados inseridos com sucesso")
            
        elif(opc == 2):
            print(dados)

        elif(opc == 0):
            print("Obrigado por utilizar o programa!")
            break
        else: 
            print("Por favor digite uma opção válida!")
            continue




menu()