from Entities.Desarrollador import Desarrollador
from Entities.Videojuegos import Videojuego


from datetime import datetime
import time


class Competencia:
    def __init__(self) -> None:
        self._videojuegos = []
        self._desarrolladores = []

    @property
    def videojuegos(self):
        return self._videojuegos

    @property
    def desarrolladores(self):
        return self._desarrolladores

    def Menu_principal(self):

        print("Menú principal:")
        print("")
        print(" Seleccione la opción del menú:")
        print("     1. Alta de desarrollador")
        print("     2. Alta de videojuego")
        print("     3. Simular competencia")
        print("     4. Realizar consultas")
        print("     5. Finalizar programa")
        print("")

        seleccion = int(input(" - Ingrese seleccion aqui: "))
        if seleccion == 1:
            return self.Alta_desarollador()
        elif seleccion == 2:
            return self.Alta_videojuego()
        elif seleccion == 3:
            return self.Simular_Competencia()
        elif seleccion == 4:
            return self.Realizar_consulta()
        elif seleccion == 5:
            return self.Finalizar_programa()
        else:
            raise ValueError

    def Alta_desarollador(self):
        print("Alta de desarrollador")
        
        # Cedula
        cedula = (input(" - Ingresar Cedula: "))
        try:
            if len(cedula) == 8:
                cedula = int(cedula)
            else:
                raise ValueError
        except ValueError:
            print("Uno o más datos ingresados son inválidos, intente nuevamente")
            time.sleep(2)
            self.Menu_principal()
        
        # Nombre y Apellido
        nombre = input(" - Ingresar Nombre: ")
        apellido = input(" - Ingresar Apellido: ")
        
        # fecha
        fecha = self.pedir_fecha()
        
        # Pais
        print(" - Seleccionar país de origen (o nacimiento):")
        print("")
        pais_de_origen = ["Uruguay", "Argentina", "Brasil", "Chile"]
        contador = 1
        for pais in pais_de_origen:
            print(f"{contador}. {pais}")
            contador += 1
        print("")
        pais = int(input(" - Ingresar Seleccion: "))
        pais_origen = pais_de_origen[pais]
        
        # Años de desarrollo
        años_de_desarrollo = input(
            " - Ingrese años de desarrollo de videojuegos:")
        print("")
        
        # Roles
        roles = ["Diseñador", "Productor", "Programador", "Tester"]
        contador = 1
        for rol in roles:
            print(f"{contador}. {rol}")
            contador += 1
        print("")
        rol = int(input("Ingresar Seleccion: "))

        # agrego el desarrollador
        self.desarrolladores.append(Desarrollador(cedula, nombre, apellido, pais_origen, fecha, años_de_desarrollo, rol))
        print("Desarollador agregado correctamente!")
        time.sleep(2)
        return self.Menu_principal()

    def pedir_fecha(self):
        try:
            date_input = input(
                " - Ingresar Fecha de nacimiento (DD/MM/AAAA): ")
            date_formating = date_input.split("/")
            date_formating = datetime(int(date_formating[2]), int(
            date_formating[1]), int(date_formating[0]))

            if datetime.now() < date_formating:
                raise ValueError
        except:
            print("Uno o más datos ingresados son inválidos, intente nuevamente")
            time.sleep(2)
            self.Menu_principal()
        return date_input

    def Alta_videojuego(self):
        print("Alta de videojuego (ingresar 0 para salir):")

        nombre = input(" - Ingrese nombre del videjuego:")

        categoria = input(
            " - Ingrese categorías del videojuego (1: Acción, 2: Aventura, 3: Estrategia, 4: Puzzle):")
        categorias = ["Acción", "Aventura", " Estrategia", "Puzzle"]
        categorias_juego = []
        categoria = categoria.split(',')
        categoria = [int(x) for x in categoria]
        for i in categoria:
            categorias_juego.append(categorias[i-1])

        integrantes = []
        cantidad_de_integrantes = int(
            input(' - Ingresar cantidad de integrantes:'))
        for i in range(cantidad_de_integrantes):
            cedula_desarollador = input(
                " - Ingrese cédula de desarrollador: (realizar este paso la cantidad de veces necesarias)")
            integrantes.append(cedula_desarollador)

        videojuego = Videojuego(nombre, categorias_juego)
        for desarollador in integrantes:
            for desarollador1 in self.desarolloadores:
                if desarollador == desarollador1:
                    videojuego.desarrolladores_asociados.append()

        videojuego.comprobar_minimo()

        self.videojuegos.append(videojuego)
        print("Videojuego agregado satisfactoriamente!")
        time.sleep(2)
        return self.Menu_principal()

    def Simular_Competencia(self):
        print("Simular Competencia:")

        categorias = ["Acción", "Aventura", "Estrategia", "Puzzle"]

        indice = 1
        for i in categorias:
            print(f' {indice}. {i}')
            indice += 1
        print("")
        categoria = int(
            input(" - Ingrese categoría del videojuego para la competencia:"))

        for videojuego in self.videojuegos:
            videojuego.competencia()

        categoria1 = categorias[categoria-1]

        competidores = [
            videojuego for videojuego in self.videojuegos if videojuego == categoria1]

        podio = []
        for videojuego in competidores:
            value = videojuego.valor
            nombre = videojuego.nombre
            podio.extend([[value, nombre]])

        podio = sorted(
            podio, key=lambda posicion_1: posicion_1[0], reverse=True)

        contador = 1
        for ganadores in podio:
            print(f' {contador} {ganadores[1]}')
            if contador == 4:
                break
            else:
                contador += 1

    def determinar_10_mejores(self):
        podio = []
        for desarollador in self.desarrolladores:
            value = desarollador.cantidad_de_años_de_desarollo
            nombre = desarollador
            podio.extend([[value, nombre]])

        podio = sorted(
            podio, key=lambda posicion_1: posicion_1[0], reverse=True)
        podio1 = [persona[1] for persona in podio]

        podio = {"Primer Lugar": podio1[0],
                 "Segundo Lugar": podio1[1],
                 "Tercer Lugar": podio1[2],
                 "Cuarto Lugar": podio1[3],
                 "Quinto Lugar": podio1[4],
                 "Sexto Lugar": podio1[5],
                 "Septimo Lugar": podio1[6],
                 "Octavo Lugar": podio1[7],
                 "Noveno Lugar": podio1[8],
                 "Decimo Lugar": podio1[9]}

        print(podio)

    def determinar_5_mejores(self):
        listita = [
            programador for programador in self.desarrolladores if programador.rol == "Programador"]
        podio = []

        for desarollador in listita:
            value = desarollador.cantidad_de_años_de_desarollo
            nombre = desarollador
            podio.extend([[value, nombre]])

        podio = sorted(
            podio, key=lambda posicion_1: posicion_1[0], reverse=True)
        podio1 = [persona[1] for persona in podio]

        podio = {"Primer Lugar": podio1[0],
                 "Segundo Lugar": podio1[1],
                 "Tercer Lugar": podio1[2],
                 "Cuarto Lugar": podio1[3],
                 "Quinto Lugar": podio1[4]}

        print(podio)

    def determinar_los_7_desarrolladores_de_edad_mas_avanzada(self):
        pass

    def determinar_mejores_deasarolladores_Uruguayos(self):
        podio = []

        for videojuego in self.videojuegos:
            value = len(
                [desarollador for desarollador in videojuego.desarrolladores_asociados if desarollador.pais_de_origen == "Uruguay"])
            nombre = videojuego
            podio.extend([[value, nombre]])

        podio = sorted(
            podio, key=lambda posicion_1: posicion_1[0], reverse=True)
        podio1 = [persona[1] for persona in podio]

        podio = podio1[0].__dict__

        print(podio)

    def Realizar_consulta(self):
        print("Realizar Consulta")
        print("1. Determine los 10 mejores desarrolladores registrados (basados en años de desarrollo)")
        print("2. Determine los 5 mejores desarrolladores con el rol de Programador basados en años de desarrollo")
        print("3. Determine los 7 desarrolladores registrados con edad más avanzada")
        print("4. Determine el videojuego con más desarrolladores que provienen de Uruguay")
        print("")
        seleccion = int(input("Ingresar seleccion:"))

        if seleccion == 1:
            self.determinar_10_mejores()
            time.sleep(2)
            self.Menu_principal()
        elif seleccion == 2:
            self.determinar_5_mejores()
            time.sleep(2)
            self.Menu_principal()
        elif seleccion == 4:
            self.determinar_mejores_deasarolladores_Uruguayos()
            time.sleep(2)
            self.Menu_principal
        elif seleccion == 5:
            self.Finalizar_programa()

    def Finalizar_programa(self):
        print("Finalizar programa...")
        time.sleep(2)
        exit()


# with open("data.txt","wb") as f: