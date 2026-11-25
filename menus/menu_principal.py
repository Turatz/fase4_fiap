from menus.menu_modulo import menu_gerenciar_modulos

def menu_principal(gerenciador):
    print("\n===== SIGIC =====")
    print("1. Gerenciar módulos")
    print("2. Consultar infraestrutura")
    print("3. Gerenciar energia")
    print("4. Visualizar rede energética")

    print("0. Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            menu_gerenciar_modulos(gerenciador)
        case 2:
           ...
        case 3:
            ...
        case 4:
            ...
        case 0:
            return False
        case _:
            print("Opção inválida.")
    return True

