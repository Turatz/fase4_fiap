from modulos.modulo_base import ModuloBase

class Producao_Oxigenio(ModuloBase):

    def __init__(self):
        super().__init__(
            nome="Producao de oxigenio",
            consumo_energetico=80,
            prioridade_operacional=5,
            capacidade_armazenamento=0,
            necessidade_comunicacao="alta"
        )