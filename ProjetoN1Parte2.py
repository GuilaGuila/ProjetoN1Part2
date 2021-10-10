listaUsuarios = []

def cadastrarUsuario():
    i = int(input("Quantos usuários deseja cadastrar? "))
    for x in range(1,i + 1):
        print("Cadastro do usuário {}º ".format(x))
        nome = input("Informe o nome: ")
        email = input("Informe o E-mail: ")
        aluno = {"Nome": nome, "E-mail": email}
        listaUsuarios.append(aluno)
        print("Usuário cadastrado com sucesso!")

    input("Pressione qualquer tecla para voltar para o menu principal.")
    menuPrincipal()

def exibirCadastros():
    print("1 - Exibir por ordem de cadastro")
    print("2 - Exibir por ordem alfabética")
    n = int(input())
    if(n == 1):
        for usuario in listaUsuarios:
            print("-----------------------------")
            print("Nome: ", usuario["Nome"])
            print("E-mail: ", usuario["E-mail"])
    elif(n == 2):
        novaLista = sorted(listaUsuarios, key=lambda d: d["Nome"])
        for usuario in novaLista:
            print("-----------------------------")
            print("Nome: ", usuario["Nome"])
            print("E-mail: ", usuario["E-mail"])

    input("Pressione qualquer tecla para voltar para o menu principal.")
    menuPrincipal()

def pesquisarCadastro():
    opcao = 1
    while opcao == 1:
        nome = input("Informe o nome do Usuário: ")
        for usuario in listaUsuarios:
            if(usuario["Nome"] == nome):
                print("-----------------------------")
                print("Nome: ", usuario["Nome"])
                print("E-mail: ", usuario["E-mail"])
                break
            else:
                print("Usuário Inexistente")
                break
        print("1- Pesquisar novamente ")
        print("2- Voltar para o menu principal ")
        opcao = int(input())
    menuPrincipal()

def removerCadastro():
    opcao = 1
    while opcao == 1:
        mail = input("Digite o E-mail do Usuário: ")
        for email in listaUsuarios:
            if(email["E-mail"] == mail):
                listaUsuarios.remove(email)
                print("Usuário removido com sucesso")
                break
            else:
                print("Usuário Inexistente")
                break
        print("1- Remover outro usuário ")
        print("2- Voltar para o menu principal ")
        opcao = int(input())
    menuPrincipal()

def alterarCadastro():
    print("5")



def menuPrincipal():
    print("1 - Cadastrar Usuário")
    print("2 - Exibir Cadastros")
    print("3 - Pesquisar Cadastro")
    print("4 - Remover Cadrastro")
    print("5 - Alterar Cadastro")
    print("6 - Encerrar")
    n = int(input())
    if(n == 1):
        cadastrarUsuario()
    elif(n == 2):
        exibirCadastros()
    elif(n == 3):
        pesquisarCadastro()
    elif(n == 4):
        removerCadastro()
    elif(n == 5):
        alterarCadastro()
    elif(n == 6):
        exit()
    else:
        print("Opção Inválida!")



def main():
    menuPrincipal()

if __name__ == "__main__":
    main()


