class Usuario:

    def __init__(self):
        self.__nome = ''
        self.__egmail = ''
        self.__senha_1 = ''
        self.__senha_2 = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if nome != '':
            self.__nome = nome
        else:
            print("o campo nome é obrigatorio")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if email != '':
            self.__email = email
        else:
            print("o campo email é obrigatório")

    @property
    def senha_1(self):
        return self.__senha_1

    @senha_1.setter
    def senha_1(self, senha_1):
        if senha_1 != '':
            if len(senha_1) >= 5 and len (senha_1) <= 8:
                self.__senha_1 = senha_1
            else:
                print("a senha deve possuir entre 5 a 8 caracteres")
        else:
            print("o campo senha é obrigatório")

    @property
    def senha_2(self):
        return self.__senha_2

    @senha_2.setter
    def senha_2(self, senha_2):
        if senha_2 != '':
            if senha_2 == self.senha_1:
                self.__senha_2 = senha_2
            else:
                print("senhas fornecidas nao sao iguais")
        else:
            print("o campo confirmar senha é obrigatório")
