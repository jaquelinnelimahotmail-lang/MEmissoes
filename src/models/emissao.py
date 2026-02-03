class Emissao:

    def __init__(self) -> None:
        self.__local: str = ''
        self.__latitude: str = ''
        self.__longitude: str = ''
        self.__tipo_gas: str = ''
        self.__valor: str = ''
        self.__unidade: str = ''
        self.__limite: float = 0.0
        self.error: str = ''

    # LOCAL
    @property
    def local(self) -> str:
        return self.__local

    @local.setter
    def local(self, local: str) -> None:
        if local != '':
            self.__local = local
            self.error = ''
        else:
            self.error = 'O campo "Local" é obrigatório'

    # LATITUDE
    @property
    def latitude(self) -> str:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: str) -> None:
        if latitude != '':
            self.__latitude = latitude
            self.error = ''
        else:
            self.error = 'O campo "Latitude" é obrigatório'

    # LONGITUDE
    @property
    def longitude(self) -> str:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: str) -> None:
        if longitude != '':
            self.__longitude = longitude
            self.error = ''
        else:
            self.error = 'O campo "Longitude" é obrigatório'

    # TIPO DE GÁS
    @property
    def tipo_gas(self) -> str:
        return self.__tipo_gas

    @tipo_gas.setter
    def tipo_gas(self, tipo_gas: str) -> None:
        if tipo_gas != '':
            self.__tipo_gas = tipo_gas
            self.error = ''
        else:
            self.error = 'O campo "Tipo de Gás" é obrigatório'

    # VALOR
    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str) -> None:
        if valor != '':
            self.__valor = valor
            self.error = ''
        else:
            self.error = 'O campo "Valor" é obrigatório'

    # UNIDADE
    @property
    def unidade(self) -> str:
        return self.__unidade

    @unidade.setter
    def unidade(self, unidade: str) -> None:
        if unidade != '':
            self.__unidade = unidade
            self.error = ''
        else:
            self.error = 'O campo "Unidade" é obrigatório'

    # LIMITE
    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, limite: float) -> None:
        if limite >= 0:
            self.__limite = limite
            self.error = ''
        else:
            self.error = 'O campo "Limite" deve ser maior ou igual a zero'
