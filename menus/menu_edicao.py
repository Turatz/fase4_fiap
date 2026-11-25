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
                ...
            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 0:
                break
            case _:
                print("Opção inválida.")


def editar_modulo(gerenciador):

    modulos = gerenciador.listar_modulos()

    print("\n===== SELECIONE O MÓDULO =====")

    identificadores = list(modulos.keys())

    for indice, identificador in enumerate(identificadores, start=1):
        print(f"{indice}. {modulos[identificador].nome}")

    print("0. Voltar")

    opcao = int(input("Escolha um módulo: "))

    if opcao == 0:
        return

    if opcao < 1 or opcao > len(identificadores):
        print("Opção inválida.")
        return

    identificador = identificadores[opcao - 1]
    modulo = modulos[identificador]

    menu_edicao(modulo)
