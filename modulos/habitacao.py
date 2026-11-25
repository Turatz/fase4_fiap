from modulos.modulo_base import ModuloBase

class Habitacao(ModuloBase):

    def __init__(self):
        super().__init__(
            nome="Habitação",
            consumo_energetico=60,
            prioridade_operacional=3,
            capacidade_armazenamento=0,
            necessidade_comunicacao="media"
        )