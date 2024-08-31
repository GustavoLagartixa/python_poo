import pickle
import traceback

from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def menu_candidato():
    print("1-Inserir candidato")
    print("2-Listar Candidatos")
    print("3-Sair")
    opc = int(input("Digite a opcao [1,2,3]? "))
    while opc not in (1, 2, 3):
        opc = int(input("Digite a opcao [1,2,3]? "))
    return opc

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def inserir_candidato(candidatos):
    numero = int(input("Digite o Numero: "))

    if numero in candidatos:
        raise Exception("Numero já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo2:
        pickle.dump(candidatos, arquivo2)

    print('Candidato gravado com sucesso!')
    print(candidato)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova secao: ")
        zona = input("Digite a nova zona: ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

def listar_candidatos(candidatos):
    for candidato in candidatos.values():
        print(candidato)

if __name__ == "__main__":

    eleitores = {} #dicionário a chave será o titulo
    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    candidatos = {}  # dicionário a chave será o numero
    try:
        print("Carregando arquivo de candidatos ...")

        with open(FILE_CANDIDATOS, 'rb') as arquivo2:
            candidatos = pickle.load(arquivo2)
    except FileNotFoundError as fnfe2:
        print(fnfe2)
        print("Arquivo nao encontrado, nenhum candidato carregado!")

    op_user = 0
    while op_user not in (1,2):
        op_user = int(input("1 - Eleitor ou 2 - Candidato\n"))
        if op_user == 1:
            opcao = 1
            while opcao in (1, 2, 3):
                try:
                    opcao = menu_eleitor()

                    if opcao == 1:
                        inserir_eleitor(eleitores)
                    elif opcao == 2:
                        atualizar_eleitor(eleitores)
                    elif opcao == 3:
                        print("Saindo!")
                        break
                except Exception as e:
                    # traceback.print_exc()
                    print(e)

        elif op_user == 2:
            opcao = 2
            while opcao in (1, 2, 3):
                try:
                    opcao = menu_candidato()

                    if opcao == 1:
                        inserir_candidato(candidatos)
                    elif opcao == 2:
                        listar_candidatos(candidatos)
                    elif opcao == 3:
                        print("Saindo!")
                        break
                except Exception as e:
                    # traceback.print_exc()
                    print(e)
