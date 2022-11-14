# categoria [accion, aventura, estrategia, puzzle]

class Videojuego:
    def __init__(self, nombre: str, categoria: str) -> None:
        self._nombre = nombre
        self._categoria = categoria
        self._desarrolladores_asociados = []
        self.valor = None
    
    def comprobar_minimo(self):
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

        if integrantes_ok:
            return ("El equipo de desarollo del juego {} cumple con el minimo necesario de integrantes".format(self.nombre))
        else:
            #raise FaltanIntegrantes("Faltan integrantes en el equipo:{}".format(self.nombre))
            raise ValueError

    def todo_sea_por_la_eficiencia(self, promedio_years, desarollador, indice):
        if promedio_years[indice] != 0:
            promedio_years[indice] += desarollador.cantidad_de_años_de_desarollo
            promedio_years[indice] /= 2

        else:
            promedio_years[indice] = desarollador.cantidad_de_años_de_desarollo

    def competencia(self):
        if self.valor == None:
            promedio_years = [0, 0, 0, 0]
            for desarollador in self.desarrolladores_asociados:
                if desarollador.rol == "Diseñador":
                    self.todo_sea_por_la_eficiencia(
                        promedio_years, desarollador, 0)
                elif desarollador.rol == "Productor":
                    self.todo_sea_por_la_eficiencia(
                        promedio_years, desarollador, 1)
                elif desarollador.rol == "Programador":
                    self.todo_sea_por_la_eficiencia(
                        promedio_years, desarollador, 2)
                elif desarollador.rol == "Tester":
                    self.todo_sea_por_la_eficiencia(
                        promedio_years, desarollador, 3)
                else:
                    raise ValueError
            valor = promedio_years[0]*0.2 + promedio_years[1] * \
                0.12+promedio_years[2]*0.5+promedio_years[3]*0.18
            self.valor = valor

        return self.valor
    
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
        return "[{}, {}, {}, {}]".format(self.nombre, self.categoria, self.__str_desarrolladores_asociados__(), self.valor)

    def __str_desarrolladores_asociados__(self):
        string = ""
        for desarrolladores_asociados in self.desarrolladores_asociados:
            string += str(desarrolladores_asociados) + " "
        return string

    def __eq__(self, otro) -> bool:
        return self.categoria == otro
