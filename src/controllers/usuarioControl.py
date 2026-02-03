from typing import List
from models.usuario import Usuario


class UsuarioControl:

    def __init__(self) -> None:
        self.__lista_usuarios: List[Usuario] = []

    def add_usuario(self, usuario: Usuario) -> None:
        self.__lista_usuarios.append(usuario)
        print("Usuário adicionado com sucesso")

    def validar_acesso(self, login: str, senha: str) -> bool:
        for usuario in self.__lista_usuarios:
            if usuario.usuario == login and usuario.senha_1 == senha:
                return True
        return False

    def acessar_usuario(self, indice: int) -> Usuario:
        return self.__lista_usuarios[indice]

    def alterar_usuario(self, indice: int, usuario: Usuario) -> None:
        self.__lista_usuarios[indice] = usuario
        print("Usuário alterado com sucesso")

    def excluir_usuario(self, indice: int) -> None:
        del self.__lista_usuarios[indice]
        print("Usuário excluído com sucesso")

    @property
    def lista_usuarios(self) -> List[Usuario]:
        return self.__lista_usuarios

    @lista_usuarios.setter
    def lista_usuarios(self, lista: List[Usuario]) -> None:
        pass
