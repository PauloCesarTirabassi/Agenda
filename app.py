from contato import Contato

#contato1 = Contato("Neymar JR", "32 anos", "114009-1934", "neymarjr@gmail.com", "Rua Hexandro Pereira, 2022 - Sao Paulo/SP", "1194564-7456", True, "ID:32543")


def menu():
    voltarMenuPrincipal = 'sim'
    while voltarMenuPrincipal == 'sim':
        opcao = input('''
        ==============================================================
        AGENDA
        
        MENU:
        
        [1] Cadastrar Contato
        [2] Imprimir Contato(s)
        [3] Deletar Contato
        [4] Buscar Contato pelo ID ou Nome
        [5] Atualizar Contato
        [6] Sair
        
        ==============================================================
        Escolha uma opçao acima:''')
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContatoPeloId()
        elif opcao == "5":
            atualizarContato()
        elif opcao == "6":
            sair()
        voltarMenuPrincipal = input(
            "Deseja voltar ao menu principal? (Sim ou Nao): ").lower()


def atualizarContato():
    nomeDeletado = input("Digite o ID ou Nome para ser Atualizado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    idContato = input("Escolha o novo ID Contato: ")
    nome = input("Escreva o novo Nome do Contato: ")
    telefone = input("Escreva o novo Telefone do Contato: ")
    email = input("Escreva o novo Email do Contato: ")
    endereco = input("Escreva o novo Endereço do Contato: ")
    celular = input("Escreva o novo Telefone do seu Contato: ")

    try:
        agenda = open("agenda.txt", "a")
        dados = f'ID:{idContato}, Nome:{nome}, Telefone:{telefone}, Email:{email}, Endereço:{endereco}, Celular:{celular}\n'
        agenda.write(dados)
        agenda.close
        print(f'Contato gravado com sucesso!')
    except:
        print("ERRO na gravaçao do contato")
    print(f'Contato atualizado com sucesso!')
    print(f'Lista de Contato(s) atualizada: ')
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()


def cadastrarContato():
    idContato = input("Escolha o ID Contato: ")
    nome = input("Escreva o Nome do Contato: ")
    telefone = input("Escreva o Telefone do Contato: ")
    email = input("Escreva o Email do Contato: ")
    endereco = input("Escreva o Endereço do Contato: ")
    celular = input("Escreva o Telefone do seu Contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'ID:{idContato}, Nome:{nome}, Telefone:{telefone}, Email:{email}, Endereço:{endereco}, Celular:{celular}\n'
        agenda.write(dados)
        agenda.close
        print(f'Contato gravado com sucesso!')
    except:
        print("ERRO na gravaçao do contato")


def listarContato():
    print("Lista de Contatos")
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()


def deletarContato():
    print("Atual lista de Contatos")
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()
    nomeDeletado = input("Digite o ID ou Nome para ser deletado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    print(f'Lista de Contato(s) atualizada: ')
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()


def buscarContatoPeloId():
    id = input(f'Digite o ID ou o Nome a ser procurado: ').upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if id in contato.split(",")[0]:
            print(contato)
        elif id in contato.split(",")[1].upper():
            print(contato)
    agenda.close()


def sair():
    print(f'Você saiu da agenda!')
    exit()


def main():
    menu()


main()
