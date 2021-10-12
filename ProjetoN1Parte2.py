import os
import time

listaUsuarios = []

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def mostrarUsuarios(usuario):
    print("-----------------------------")
    print("Nome: ", usuario["Nome"])
    print("E-mail: ", usuario["E-mail"])

def cadastrarUsuario():
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

    input("Pressione qualquer tecla para voltar para o menu principal")
    clearConsole()
    menuPrincipal()

def exibirCadastros():
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
        exibirCadastros()

    input("Pressione qualquer tecla para voltar para o menu principal")
    clearConsole()
    menuPrincipal()

def pesquisarCadastro():
    opcao = 1
    while opcao == 1:
        nome = input("Informe o nome do Usuário: ").strip()
        for usuario in listaUsuarios:
            if(usuario["Nome"] == nome):
                mostrarUsuarios(usuario)
                break
        print("1- Pesquisar novamente ")
        print("2- Voltar para o menu principal ")
        opcao = int(input())
        clearConsole()
    menuPrincipal()

def removerCadastro():
    opcao = 1
    while opcao == 1:
        email = input("Digite o E-mail do Usuário: ").strip()
        for usuario in listaUsuarios:
            if(usuario["E-mail"] == email):
                listaUsuarios.remove(usuario)
                print("Usuário removido com sucesso")
                break
            else:
                print("Usuário Inexistente")
                break
        print("1- Remover outro usuário ")
        print("2- Voltar para o menu principal ")
        opcao = int(input())
    clearConsole()
    menuPrincipal()

def alterarCadastro():
    opcao = 1
    while opcao == 1:
        email = input("Digite o E-mail do Usuário: ").strip()
        for usuario in listaUsuarios:
            if(email == usuario["E-mail"]):
                nome = input("Digite o novo nome do usuário: ").strip()
                usuario["Nome"] = nome
                print("Alteração realizada com sucesso ")
                break
            else:
                print("Usuário não encontrado")
                break
        print("1- Alterar outro usuário ")
        print("2- Voltar para o menu principal ")
        opcao = int(input())
    clearConsole()
    menuPrincipal()

def menuPrincipal():
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
        cadastrarUsuario()
    elif(n == 2):
        clearConsole()
        exibirCadastros()
    elif(n == 3):
        clearConsole()
        pesquisarCadastro()
    elif(n == 4):
        clearConsole()
        removerCadastro()
    elif(n == 5):
        clearConsole()
        alterarCadastro()
    elif(n == 6):
        print("Até logo.")
        exit()
    else:
        print("Opção Inválida!")
        time.sleep(2)
        clearConsole()
        menuPrincipal()

def main():
    menuPrincipal()

if __name__ == "__main__":
    main()