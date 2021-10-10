#Uma instituição de ensino superior precisa de um sistema para gerenciar o processo de inscrições em
#um evento técnico. O sistema deve permitir a implementação das seguintes histórias de usuário:
#H1.: Como gestor do sistema gostaria de cadastrar novos usuários pelo seu nome completo e e-mail.
#H2.: Como gestor do sistema gostaria de exibir todos os usuários cadastrados, listando-os por ordem
#de cadastro.
#H3.: Como gestor do sistema gostaria de exibir todos os usuários cadastros, listando-os por ordem
#alfabética.
#H4.: Como gestor do sistema gostaria de verificar se um usuário faz parte da lista de participantes,
#buscando-o pelo seu nome.
#H5.: Como gestor do sistema gostaria poder remover um usuário cadastrado, buscando-o por seu email.
#H6.: Como gestor do sistema gostaria de poder alterar o nome de um usuário cadastrado no sistema,
#buscando-o por seu e-mail.

#cadastrar novo usuário
#exibir usuários (ordem alfabética ou ordem de cadastro)
#pesquisar cadastro 
#remover cadastro
#alterar cadastro 

listaUsarios = []

def cadastrarUsuario():
    i = int(input("Quantos usuários deseja cadastrar?"))
    for x in range(1,i + 1):
        print("Cadastro do usuário {}º ".format(x))
        nome = input("Informe o nome: ")
        email = input("Informe o E-mail: ")
        aluno = {"Nome": nome, "E-mail": email}
        listaUsarios.append(aluno)
        print("Usuário cadastrado com sucesso!")

    input("Pressione qualquer tecla para voltar para o menu principal.")
    menuPrincipal()
    


def exibirCadastros():
    print("2")

def pesquisarCadastro():
    print("3")

def removerCadastro():
    print("4")

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


