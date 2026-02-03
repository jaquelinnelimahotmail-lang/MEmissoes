from typing import List
from models.usuario import Usuario

class UsuarioControl:

    def __init__(self) -> None:
        self.__lista_usuarios:List[Usuario] = []

    def add_usuario(self, usuario:Usuario) -> None:
        self.__lista_usuarios.append(usuario)
        print("usuario adicionado com sucesso")

    def validar_acesso(self, user:str, senha:str) -> bool:
        validacao = False
        for user in self.__lista_usuarios:
            if user.usuario == user and user.senha_1 == senha:
                validacao = True
                break
        return validacao

    def acessar_usuario(self, indice:int) -> Usuario:
        usuario = self.__lista_usuarios[indice]
        return usuario

    def alterar_usuario(self, indice:int, usuario:Usuario) -> None:
        self.__lista_usuarios[indice] = usuario
        print("usuario alterado com sucesso")

    def excluir_usuario(self, indice:int) -> None:
        del self.__lista_usuarios[indice]
        print("usuario excluido com sucesso")

    @property
    def lista_usuarios(self) -> List[Usuario]:
        return self.__lista_usuarios

    @lista_usuarios.setter
    def lista_usuarios(self, lista:List[Usuario]) -> None:
        pass
