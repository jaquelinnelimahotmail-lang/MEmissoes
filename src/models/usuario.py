class Usuario:

    def __init__(self) -> None:
        self.__nome: str = ''
        self.__sobrenome: str = ''
        self.__usuario: str = ''
        self.__email: str = ''
        self.__senha_1: str = ''
        self.__senha_2: str = ''
        self.error: str = ''

    # NOME
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if nome != '':
            self.__nome = nome
            self.error = ''
        else:
            self.error = 'O campo "Nome" é obrigatório'

    # SOBRENOME
    @property
    def sobrenome(self) -> str:
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome: str) -> None:
        if sobrenome != '':
            self.__sobrenome = sobrenome
            self.error = ''
        else:
            self.error = 'O campo "Sobrenome" é obrigatório'

    # USUÁRIO
    @property
    def usuario(self) -> str:
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario: str) -> None:
        if usuario != '':
            self.__usuario = usuario
            self.error = ''
        else:
            self.error = 'O campo "Usuário" é obrigatório'

    # EMAIL
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if email != '':
            self.__email = email
            self.error = ''
        else:
            self.error = 'O campo "E-mail" é obrigatório'

    # SENHA 1
    @property
    def senha_1(self) -> str:
        return self.__senha_1

    @senha_1.setter
    def senha_1(self, senha_1: str) -> None:
        if senha_1 != '':
            if 5 <= len(senha_1) <= 8:
                self.__senha_1 = senha_1
                self.error = ''
            else:
                self.error = 'A senha deve possuir entre 5 e 8 caracteres'
        else:
            self.error = 'O campo "Senha" é obrigatório'

    # SENHA 2
    @property
    def senha_2(self) -> str:
        return self.__senha_2

    @senha_2.setter
    def senha_2(self, senha_2: str) -> None:
        if senha_2 != '':
            if senha_2 == self.__senha_1:
                self.__senha_2 = senha_2
                self.error = ''
            else:
                self.error = 'As senhas fornecidas não são iguais'
        else:
            self.error = 'A confirmação de senha é obrigatória'
