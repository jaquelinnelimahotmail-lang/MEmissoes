from typing import List
from models.emissao import Emissao

class EmissaoControl:

    def __init__(self) -> None:
        self.__lista_emissoes:List[Emissao] = []

    def add_emissao(self, emissao:Emissao) -> str:
        self.__lista_emissoes.append(emissao)
        return 'Emissao cadastrada com sucesso'
