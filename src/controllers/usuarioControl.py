from typing import List
from models.usuario import Usuario

class UsuarioControl:

    def __init__(self):
        self.__lista_usuarios:List[Usuario] = []

    def add_usuario(self, usuario:Usuario):
        self.__lista_usuarios.append(usuario)
        print("usuario adicionado com sucesso")

    def consultar_usuario(self, usuario:str, senha:str):
        flag = False
        for usuario in self.__lista_usuarios:
            if usuario.user == usuario and usuario.senha_1 == senha:
                flag = True
                break
        return flag

    def acessar_usuario(self, indice:int):
        usuario = self.__lista_usuarios[indice]
        return usuario

    def alterar_usuario(self, indice:int, usuario:Usuario):
        self.__lista_usuarios[indice] = usuario
        print("usuario alterado com sucesso")

    def excluir_usuario(self, indice:int):
        del self.__lista_usuarios[indice]
        print("usuario excluido com sucesso")

    @property
    def lista_usuarios(self):
        return self.__lista_usuarios

    @lista_usuarios.setter
    def lista_usuarios(self, lista:List[Usuario]):
        pass
