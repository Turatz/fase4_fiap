from modulos.modulo_base import ModuloBase

class Comunicacao(ModuloBase):

    def __init__(self):
        super().__init__(
            nome="Comunicacao",
            consumo_energetico=30,
            prioridade_operacional=4,
            capacidade_armazenamento=0,
            necessidade_comunicacao="alta"
        )