class Plan:
    __codigo = 0
    __modelo = ''
    __version =''
    __valor =0
    __canticuota =60
    __cuotalicitar=10

    def __init__(self, cod, mod, vers, valor):
        self.__codigo=cod
        self.__modelo=mod
        self.__version=vers
        self.__valor=valor

    @classmethod
    def get_canticuota(cls):
        return cls.__canticuota
    @classmethod
    def get__cuotalicitas(cls):
        return cls.__cuotalicitar
    @classmethod
    def modificar_cuotalicitar(cls,ncuota):
        cls.__cuotalicitar=ncuota

    def get_codigo(self):
        return self.__codigo
    def get_modelo(self):
        return self.__modelo
    def get_version(self):
        return self.__version
    def get_valor(self):
        return self.__valor

    def valorcuota(self):
        valorc=(self.__valor/self.__canticuota)+self.__valor*0.10
        return valorc

    def actualizar_valor(self,nuevovalor):
        self.__valor=nuevovalor

