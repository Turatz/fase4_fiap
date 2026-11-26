from modulos.gerenciador_modulos import GerenciadorModulos
from modulos.gerenciador_modos import GerenciadorModos
from menus.menu_principal import menu_principal

gerenciador = GerenciadorModulos()
gerenciador_modos = GerenciadorModos()

while True:
    continuar = menu_principal(gerenciador, gerenciador_modos)

    if not continuar:
        print("Encerrando o SIGIC...")
        break