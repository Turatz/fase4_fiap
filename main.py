from modulos.gerenciador_modulos import GerenciadorModulos
from menus.menu_principal import menu_principal

gerenciador = GerenciadorModulos()

while True:
    continuar = menu_principal(gerenciador)

    if not continuar:
        print("Encerrando o SIGIC...")
        break
