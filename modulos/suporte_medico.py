from modulos.modulo_base import ModuloBase

class SuporteMedico(ModuloBase):

    def __init__(self):
        super().__init__(
            nome="Suporte medico",
            consumo_energetico=60,
            prioridade_operacional=3,
            capacidade_armazenamento=0,
            necessidade_comunicacao="media"
        )