def menu_modos(gerenciador_modos):

    while True:
        dados = gerenciador_modos.consultar_modo()

        print("\n===== GERENCIAMENTO DE MODOS =====")
        print(f"Modo atual: {dados['modo_atual'].upper()}")
        print(f"Controle: {dados['controle'].upper()}")

        print("\n1. Ativar modo normal")
        print("2. Ativar modo econômico")
        print("3. Ativar modo emergência")
        print("4. Retornar ao automático")
        print("0. Voltar")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Digite uma opção numérica.")
            continue

        match opcao:
            case 1:
                gerenciador_modos.ativar_manual("normal")
                print("Modo normal ativado manualmente.")

            case 2:
                gerenciador_modos.ativar_manual("economico")
                print("Modo econômico ativado manualmente.")

            case 3:
                gerenciador_modos.ativar_manual("emergencia")
                print("Modo emergência ativado manualmente.")

            case 4:
                gerenciador_modos.ativar_automatico()
                print("Controle automático ativado.")

            case 0:
                break

            case _:
                print("Opção inválida.")
