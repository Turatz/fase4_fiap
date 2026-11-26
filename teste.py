
from modulos.gerenciador_modos import GerenciadorModos

gerenciador = GerenciadorModos()

def testar_energia(energia):
    modo = gerenciador.atualizar_modo(energia)
    print(f"Energia: {energia}% | Modo: {modo.upper()}")


print("===== TESTE DOS MODOS AUTOMÁTICOS =====")

testar_energia(80)
testar_energia(50)
testar_energia(40)
testar_energia(24)
testar_energia(28)
testar_energia(31)
testar_energia(56)


print("\n===== TESTE DO CONTROLE MANUAL =====")

gerenciador.ativar_manual("emergencia")

print("Controle manual:", gerenciador.consultar_modo())

gerenciador.atualizar_modo(90)

print("Após atualização automática:", gerenciador.consultar_modo())

gerenciador.ativar_automatico()

print("Controle automático:", gerenciador.consultar_modo())
