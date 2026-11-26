from menus.menu_edicao import editar_modulo

def menu_gerenciar_modulos(gerenciador):

    while True:
        print("\n===== GERENCIAMENTO DE MÓDULOS =====")
        print("1. Editar módulo")
        print("2. Listar módulos")
        print("0. Voltar")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite uma opção numérica válida.")
            continue

        match opcao:
            case 1:
               editar_modulo(gerenciador)

            case 2:
                modulos = gerenciador.listar_modulos()

                print("\n===== MÓDULOS DA COLÔNIA =====")

                nomes_atributos = {
                    "nome": "Nome",
                    "consumo_energetico": "Consumo energético",
                    "prioridade_operacional": "Prioridade operacional",
                    "capacidade_armazenamento": "Capacidade de armazenamento",
                    "necessidade_comunicacao": "Necessidade de comunicação",
                    "status_operacional": "Status operacional"
                }

                for identificador, modulo in modulos.items():
                    print(f"\n--- {modulo.nome.upper()} ---")
                    print(f"Identificador: {identificador}")

                    dados = modulo.consultar_dados()

                    for atributo, valor in dados.items():
                        nome_exibicao = nomes_atributos[atributo]
                        print(f"{nome_exibicao}: {valor}")
            case 0:
                break
            case _:
                print("Opção inválida.")
