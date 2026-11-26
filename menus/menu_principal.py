from menus.menu_modulo import menu_gerenciar_modulos
from menus.menu_modos import menu_modos

def menu_principal(gerenciador, gerenciador_modos):
    print("\n===== SIGIC =====")
    print("1. Gerenciar módulos")
    print("2. Consultar infraestrutura")
    print("3. Gerenciar energia")
    print("4. Visualizar rede energética")
    print("5. Gerenciar modos de operação")
    print("0. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite uma opção numérica válida.")
        
    match opcao:
        case 1:
            menu_gerenciar_modulos(gerenciador)
        case 2:
           ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            menu_modos(gerenciador_modos)
        case 0:
            return False
        case _:
            print("Opção inválida.")
    return True

