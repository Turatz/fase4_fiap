def menu_edicao(modulo):

    while True:
        print(f"\n===== EDITAR {modulo.nome.upper()} =====")
        print("1. Consumo energético")
        print("2. Prioridade operacional")
        print("3. Necessidade de comunicação")
        print("4. Capacidade de armazenamento")
        print("0. Voltar")

        opcao = int(input("Escolha uma opção: "))

        match opcao:
            case 1:
                try:
                    novo_consumo = float(
                        input("Informe o novo consumo energético: ")
                    )

                    modulo.alterar_consumo(novo_consumo)

                    print("Consumo energético atualizado com sucesso!")

                except ValueError as erro:
                    print(f"Erro: {erro}")

            case 2:
                try:
                    nova_prioridade = int(
                        input("Informe a nova prioridade (1 a 5): ")
                    )

                    if nova_prioridade < 1 or nova_prioridade > 5:
                        print("Prioridade inválida! Informe um valor entre 1 e 5.")

                    else:
                        modulo.alterar_prioridade(nova_prioridade)
                        print("Prioridade atualizada com sucesso!")

                except ValueError:
                    print("Digite apenas números inteiros.")
                                
            case 3:
                    nova_necessidade = input(
                        "Informe a necessidade (baixa, media ou alta): "
                    ).lower().strip()

                    if nova_necessidade not in ["baixa", "media", "alta"]:
                        print("Opção inválida! Escolha baixa, media ou alta.")

                    else:
                        modulo.alterar_comunicacao(nova_necessidade)
                        print("Necessidade de comunicação atualizada com sucesso!")
            
            case 4:
                try:
                    nova_capacidade = float(
                        input("Informe a nova capacidade de armazenamento: ")
                    )

                    if nova_capacidade < 0:
                        print("Capacidade inválida! Informe um valor positivo.")

                    else:
                        modulo.alterar_capacidade_armazenamento(nova_capacidade)
                        print("Capacidade de armazenamento atualizada com sucesso!")

                except ValueError:
                    print("Digite um valor numérico válido.")
            case 0:
                input("Aperte enter para voltar")
                print("Voltando...")
                break
            case _:
                print("Opção inválida.")


def editar_modulo(gerenciador):

    modulos = gerenciador.listar_modulos()

    identificadores = list(modulos.keys())

    while True:
        print("\n===== SELECIONE O MÓDULO =====")

        for indice, identificador in enumerate(identificadores, start=1):
            print(f"{indice}. {modulos[identificador].nome}")

        print("0. Voltar")

        try:
            opcao = int(input("Escolha um módulo: "))

            if opcao == 0:
                return

            if opcao < 1 or opcao > len(identificadores):
                print("Opção inválida! Tente novamente.")
                continue

            identificador = identificadores[opcao - 1]
            modulo = modulos[identificador]

            menu_edicao(modulo)

        except ValueError:
            print("Digite apenas números inteiros.")