from typing import List
from models.emissao import Emissao

class EmissaoControl:

    def __init__(self) -> None:
        self.__lista_emissoes:List[Emissao] = []

    def add_emissao(self, emissao:Emissao) -> str:
        self.__lista_emissoes.append(emissao)
        return 'Emissao cadastrada com sucesso'

    def acessar_emissao(self, indice:int) -> Emissao:
        return self.__lista_emissoes[indice]

    def alterar_emissao(self, indice:int, emissao:Emissao) -> str:
        self.__lista_emissoes[indice] = emissao
        return 'Cadastro de emissão alterado com sucesso'

    def excluir_emissao(self, indice:int) -> str:
        del self.__lista_emissoes[indice]
        return 'Cadastro de emissão excluído com sucesso'

    @property
    def lista_emissoes(self) -> List[Emissao]:
        return self.__lista_emissoes

    @lista_emissoes.setter
    def lista_emissoes(self, lista:List[Emissao]) -> None:
        pass
