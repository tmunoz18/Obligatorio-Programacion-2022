# categoria [accion, aventura, estrategia, puzzle]

class Videojuego:
    def __init__(self, nombre: str, categoria: str) -> None:
        self._nombre = nombre
        self._categoria = categoria
        self._desarrolladores_asociados = []
        self.puntaje = None

    def cumple_minimo(self):
        diseñadores = 2
        productores = 1
        programadores = 3
        testers = 2

        integrantes_ok = True

        equipo_min = [diseñadores, productores, programadores, testers]

        for desarollador in self.desarrolladores_asociados:
            if desarollador.rol == "Diseñador":
                equipo_min[0] = equipo_min[0]-1
            elif desarollador.rol == "Productor":
                equipo_min[1] = equipo_min[1]-1
            elif desarollador.rol == "Programador":
                equipo_min[2] = equipo_min[2]-1
            elif desarollador.rol == "Tester":
                equipo_min[3] = equipo_min[3]-1

        for cantidad in equipo_min:
            if cantidad > 0:
                integrantes_ok = False

        return integrantes_ok

    def calc_promedio(self):
        avg = [0, 0, 0, 0]
        cant = [0, 0, 0, 0]
        for dev in self._desarrolladores_asociados:
            if dev.rol == "Diseñador":
                avg[0] += dev.cantidad_de_años_de_desarollo
                cant[0] += 1
            elif dev.rol == "Productor":
                avg[1] += dev.cantidad_de_años_de_desarollo
                cant[1] += 1
            elif dev.rol == "Programador":
                avg[2] += dev.cantidad_de_años_de_desarollo
                cant[2] += 1
            elif dev.rol == "Tester":
                avg[3] += dev.cantidad_de_años_de_desarollo
                cant[3] += 1
        avg[0] = avg[0] / cant[0]
        avg[1] = avg[1] / cant[1]
        avg[2] = avg[2] / cant[2]
        avg[3] = avg[3] / cant[3]
        return avg
    
    def calc_puntaje(self):
        if self.puntaje == None:
            avg_years = self.calc_promedio()
            self.puntaje = avg_years[0] * 0.2 + avg_years[1] * 0.12 + avg_years[2] * 0.5 + avg_years[3] * 0.18
        return self.puntaje

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def desarrolladores_asociados(self):
        return self._desarrolladores_asociados

    def __str__(self) -> str:
        return "[{}, {}, {}, {}]".format(self.nombre, self.categoria, self.__str_desarrolladores_asociados__(), self.puntaje)

    def __str_desarrolladores_asociados__(self):
        string = ""
        for desarrolladores_asociados in self.desarrolladores_asociados:
            string += str(desarrolladores_asociados) + " "
        return string
