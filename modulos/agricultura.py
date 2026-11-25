from modulos.modulo_base import ModuloBase

class Agricultura(ModuloBase):

    def __init__(self):
        super().__init__(
            nome="Agricultura",
            consumo_energetico=80,
            prioridade_operacional=4,
            capacidade_armazenamento=0,
            necessidade_comunicacao="media"
        )