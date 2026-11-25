from modulos.habitacao import Habitacao
from modulos.agricultura import Agricultura
from modulos.laboratorio import Laboratorio
from modulos.comunicacao import Comunicacao
from modulos.suporte_medico import SuporteMedico
from modulos.producao_oxigenio import ProducaoOxigenio


class GerenciadorModulos:

    def __init__(self):
        self.modulos = {
            "habitacao": Habitacao(),
            "agricultura": Agricultura(),
            "laboratorio": Laboratorio(),
            "comunicacao": Comunicacao(),
            "suporte_medico": SuporteMedico(),
            "producao_oxigenio": ProducaoOxigenio()
        }

    def listar_modulos(self):
        return self.modulos

    def buscar_modulo(self, identificador):
        return self.modulos.get(identificador)
