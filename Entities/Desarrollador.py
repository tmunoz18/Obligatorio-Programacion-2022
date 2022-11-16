# cedular len 8
# pais de origen [Argentina, Brasil, Chile, Uruguay]
# fecha de nacimiento > cantidad de años de desarrollo en videojuegos
# rol [Diseñador, productor, programador, tester]

class Desarrollador:
    def __init__(self, cedula: int, nombre: str, apellido: str, pais_de_origen: str, fecha_de_nacimiento: str, cantidad_de_años_de_desarollo: int, rol: str) -> None:

        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._pais_de_origen = pais_de_origen
        self._fecha_de_nacimiento = fecha_de_nacimiento
        self._cantidad_de_años_de_desarollo = cantidad_de_años_de_desarollo
        self._rol = rol

    @property
    def cedula(self):
        return self._cedula
    

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def pais_de_origen(self):
        return self._pais_de_origen

    @property
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento

    @property
    def rol(self):
        return self._rol
    
    @property
    def cantidad_de_años_de_desarollo(self):
        return self._cantidad_de_años_de_desarollo
    
    @cantidad_de_años_de_desarollo.setter
    def cantidad_de_años_de_desarollo(self, x):
        self._cantidad_de_años_de_desarollo = x

    def __str__(self) -> str:
        return "['_cedula': {}, '_nombre': {}, '_apellido': {}, '_pais_de_origen': {}, '_fecha_de_nacimiento': {}, '_cantidad_de_años_de_desarollo': {}, '_rol': {}]".format(self.cedula, self.nombre, self.apellido, self.pais_de_origen, self.fecha_de_nacimiento, self.cantidad_de_años_de_desarollo, self.rol)