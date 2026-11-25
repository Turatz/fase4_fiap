class ModuloBase:

    def __init__(
        self,
        nome,
        consumo_energetico,
        prioridade_operacional,
        capacidade_armazenamento=0,
        necessidade_comunicacao="baixa"
    ):
        
        if consumo_energetico < 0:
            raise ValueError("O consumo energético não pode ser negativo.")

        if prioridade_operacional < 1 or prioridade_operacional > 5:
            raise ValueError("A prioridade deve estar entre 1 e 5.")

        if capacidade_armazenamento < 0:
            raise ValueError("A capacidade de armazenamento não pode ser negativa.")
        
        if necessidade_comunicacao not in ["baixa", "media", "alta"]:
            raise ValueError("A comunicação deve ser baixa, media ou alta.")

        self.nome = nome
        self.consumo_energetico = consumo_energetico
        self.prioridade_operacional = prioridade_operacional
        self.capacidade_armazenamento = capacidade_armazenamento
        self.necessidade_comunicacao = necessidade_comunicacao
        self.status_operacional = "ativo"

    
    def alterar_consumo(self, novo_consumo):
        if novo_consumo < 0:
            raise ValueError("O consumo energético não pode ser negativo.")

        self.consumo_energetico = novo_consumo

    def alterar_prioridade(self, nova_prioridade):
        if nova_prioridade < 1 or nova_prioridade > 5:
            raise ValueError("A prioridade deve estar entre 1 e 5.")

        self.prioridade_operacional = nova_prioridade

    def alterar_comunicacao(self, nova_necessidade):
        if nova_necessidade not in ["baixa", "media", "alta"]:
            raise ValueError("A comunicação deve ser baixa, media ou alta.")

        self.necessidade_comunicacao = nova_necessidade

    def ativar(self):
        self.status_operacional = "ativo"

    def desativar(self):
        self.status_operacional = "inativo"

    def consultar_status(self):
        return self.status_operacional

    def consultar_dados(self):
        return {
            "nome": self.nome,
            "consumo_energetico": self.consumo_energetico,
            "prioridade_operacional": self.prioridade_operacional,
            "capacidade_armazenamento": self.capacidade_armazenamento,
            "necessidade_comunicacao": self.necessidade_comunicacao,
            "status_operacional": self.status_operacional
        }

    
    def alterar_capacidade_armazenamento(self, nova_capacidade):
        if nova_capacidade < 0:
            raise ValueError("A capacidade não pode ser negativa.")

        self.capacidade_armazenamento = nova_capacidade

