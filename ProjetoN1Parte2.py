import os
import time


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def mostrarUsuarios(usuario):
    print("-----------------------------")
    print("Nome: ", usuario["Nome"])
    print("E-mail: ", usuario["E-mail"])

def cadastrarUsuario(listaUsuarios):
    i = int(input("Quantos usuários deseja cadastrar? "))
    clearConsole()
    for x in range(1,i + 1):
        print("Cadastro do usuário {}º ".format(x))
        nome = input("Informe o nome: ").strip()
        email = input("Informe o E-mail: ").strip()
        aluno = {"Nome": nome, "E-mail": email}
        listaUsuarios.append(aluno)
        clearConsole()
        print("Usuário cadastrado com sucesso!")

    print("\n")
    input("Pressione qualquer tecla para voltar para o menu principal")
    clearConsole()
    menuPrincipal(listaUsuarios)

def exibirCadastros(listaUsuarios):
    print("1 - Exibir por ordem de cadastro")
    print("2 - Exibir por ordem alfabética")
    n = int(input())
    clearConsole()
    if(n == 1):
        for usuario in listaUsuarios:
            mostrarUsuarios(usuario)
    elif(n == 2):
        novaLista = sorted(listaUsuarios, key=lambda d: d["Nome"])
        for usuario in novaLista:
            mostrarUsuarios(usuario)
    else:
        print("Opção Inválida!")
        time.sleep(2)
        clearConsole()
        exibirCadastros(listaUsuarios)

    print("\n")
    input("Pressione qualquer tecla para voltar para o menu principal")
    clearConsole()
    menuPrincipal(listaUsuarios)

def pesquisarCadastro(listaUsuarios):
    opcao = 1
    while opcao == 1:
        nome = input("Informe o nome do Usuário: ").strip()
        for usuario in listaUsuarios:
            if(usuario["Nome"] == nome):
                mostrarUsuarios(usuario)
                break
        print("\n")
        print("1- Pesquisar novamente ")
        print("2- Voltar para o menu principal ")
        opcao = int(input())
        clearConsole()
    menuPrincipal(listaUsuarios)

def removerCadastro(listaUsuarios):
    opcao = 1
    while opcao == 1:
        email = input("Digite o E-mail do Usuário: ").strip()
        listLength = len(listaUsuarios)
        for usuario in listaUsuarios:
            if(usuario["E-mail"] == email):
                listaUsuarios.remove(usuario)
                print("Usuário removido com sucesso")
                break
        if(listLength == len(listaUsuarios)):
            print("Usuário inexistente")
        
        print("\n")
        print("1- Remover outro usuário ")
        print("2- Voltar para o menu principal ")
        opcao = int(input())
        clearConsole()
    menuPrincipal(listaUsuarios)

def alterarCadastro(listaUsuarios):
    opcao = 1
    while opcao == 1:
        email = input("Digite o E-mail do usuário que deseja alterar: ").strip()
        for usuario in listaUsuarios:
            if(email == usuario["E-mail"]):
                nome = input("Digite o novo nome do usuário: ").strip()
                usuario["Nome"] = nome
                print("Alteração realizada com sucesso ")
                break
            
        print("\n")
        print("1- Alterar outro usuário ")
        print("2- Voltar para o menu principal ")
        opcao = int(input())
    clearConsole()
    menuPrincipal(listaUsuarios)

def menuPrincipal(listaUsuarios):
    print("----------MENU----------")
    print("1 - Cadastrar Usuário")
    print("2 - Exibir Cadastros")
    print("3 - Pesquisar Cadastro")
    print("4 - Remover Cadrastro")
    print("5 - Alterar Cadastro")
    print("6 - Encerrar")
    n = int(input())
    if(n == 1):
        clearConsole()
        cadastrarUsuario(listaUsuarios)
    elif(n == 2):
        clearConsole()
        exibirCadastros(listaUsuarios)
    elif(n == 3):
        clearConsole()
        pesquisarCadastro(listaUsuarios)
    elif(n == 4):
        clearConsole()
        removerCadastro(listaUsuarios)
    elif(n == 5):
        clearConsole()
        alterarCadastro(listaUsuarios)
    elif(n == 6):
        print("Até logo.")
        exit()
    else:
        print("Opção Inválida!")
        time.sleep(2)
        clearConsole()
        menuPrincipal()

def main():
    listaUsuarios = []
    menuPrincipal(listaUsuarios)

if __name__ == "__main__":
    main()