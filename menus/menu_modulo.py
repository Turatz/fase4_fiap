from menus.menu_edicao import editar_modulo

def menu_gerenciar_modulos(gerenciador):

    while True:
        print("\n===== GERENCIAMENTO DE MÓDULOS =====")
        print("1. Editar módulo")
        print("2. Listar módulos")
        print("0. Voltar")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
               editar_modulo(gerenciador)

            case 2:
                modulos = gerenciador.listar_modulos()

                print("\n===== MÓDULOS DA COLÔNIA =====")

                for identificador, modulo in modulos.items():
                    print(f"\nMódulo: {modulo.nome}")
                    print(f"Identificador: {identificador}")

                    dados = modulo.consultar_dados()

                    for atributo, valor in dados.items():
                        print(f"{atributo}: {valor}")
            case 0:
                break
            case _:
                print("Opção inválida.")
