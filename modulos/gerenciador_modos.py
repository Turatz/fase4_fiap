
class GerenciadorModos:

    def __init__(self):
        self.modo_atual = "normal"
        self.controle = "automatico"

    def ativar_manual(self, novo_modo):
        modos_validos = ["normal", "economico", "emergencia"]

        if novo_modo not in modos_validos:
            raise ValueError("Modo de operação inválido.")

        self.modo_atual = novo_modo
        self.controle = "manual"

    def ativar_automatico(self):
        self.controle = "automatico"

    def atualizar_modo(self, energia_percentual):

        if not isinstance(energia_percentual, (int, float)):
            raise TypeError("A energia deve ser um valor numérico.")

        if not 0 <= energia_percentual <= 100:
            raise ValueError("A energia deve estar entre 0% e 100%.")

        if self.controle == "manual":
            return self.modo_atual

        if self.modo_atual == "normal":

            if energia_percentual <= 50:
                self.modo_atual = "economico"

        elif self.modo_atual == "economico":

            if energia_percentual > 55:
                self.modo_atual = "normal"

            elif energia_percentual < 25:
                self.modo_atual = "emergencia"

        elif self.modo_atual == "emergencia":

            if energia_percentual > 30:
                self.modo_atual = "economico"

        return self.modo_atual

    def consultar_modo(self):
        return {
            "modo_atual": self.modo_atual,
            "controle": self.controle
        }
