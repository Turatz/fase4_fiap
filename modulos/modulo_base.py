class ModuloBase:

    def __init__(
        self,
        nome,
        consumo_energetico,
        prioridade_operacional,
        capacidade_armazenamento=0,
        necessidade_comunicacao="baixa"
    ):
        self.nome = nome
        self.consumo_energetico = consumo_energetico
        self.prioridade_operacional = prioridade_operacional
        self.capacidade_armazenamento = capacidade_armazenamento
        self.necessidade_comunicacao = necessidade_comunicacao
        self.status_operacional = "ativo"

    def ativar(self):
        self.status_operacional = "ativo"

    def desativar(self):
        self.status_operacional = "inativo"

    def consultar_status(self):
        return self.status_operacional
