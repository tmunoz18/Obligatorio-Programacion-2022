from Entities.Desarrollador import Desarrollador
from Entities.Videojuegos import Videojuego


import datetime
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
        print("")
        print("Menú principal:")
        print("")
        print(" Seleccione la opción del menú:")
        print("     1. Alta de desarrollador")
        print("     2. Alta de videojuego")
        print("     3. Simular competencia")
        print("     4. Realizar consultas")
        print("     5. Finalizar programa")
        print("")
        try:
            seleccion = int(input(" - Ingrese seleccion aqui: "))
            if seleccion > 5 or seleccion < 1:
                raise ValueError
        except:
            print("Seleccion Invalida")
            time.sleep(2)
            self.Menu_principal()
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
        
    def Alta_desarollador(self):
        print("Alta de desarrollador")

        # Cedula
        cedula = (input(" - Ingresar Cedula: "))
        # verifico que la cedula sea un dato correcto
        try:
            if len(cedula) == 8:
                cedula = int(cedula)
            else:
                raise ValueError
        except ValueError:
            print("Cedula ingresada es inválida, intente nuevamente")
            time.sleep(2)
            self.Menu_principal()
        # verifico si ya existe un desarrollador ingresado con esta cedula
        try:
            if self.existe_desarrollador(cedula):
                raise ValueError
        except ValueError:
            print("Este desarrollador ya existe")
            time.sleep(2)
            self.Menu_principal()

        # Nombre y Apellido
        nombre = input(" - Ingresar Nombre: ")
        apellido = input(" - Ingresar Apellido: ")
        # verifico que el nombre y el apellido no sean numeros
        try:
            if nombre.isnumeric() or apellido.isnumeric():
                raise ValueError
        except ValueError:
            print("Nombre o Apellido ingresado es inválidos, intente nuevamente")
            time.sleep(2)
            self.Menu_principal()
        # fecha
        fecha, fecha_datetime = self.pedir_fecha()

        # Pais
        print(" - Seleccionar país de origen (o nacimiento):")
        print("")
        pais_de_origen = ["Uruguay", "Argentina", "Brasil", "Chile"]
        contador = 1
        for pais in pais_de_origen:
            print(f"{contador}. {pais}")
            contador += 1
        print("")
        try:
            pais = int(input(" - Ingresar Seleccion: "))
            if pais - 1 >= 0 and pais - 1 <= 3:
                pais_origen = pais_de_origen[pais-1]
            else:
                raise ValueError
        except ValueError:
            print("Pais Fuera de rango")
            time.sleep(2)
            self.Menu_principal()

        # Años de desarrollo
        años_de_desarrollo = input(" - Ingrese años de desarrollo de videojuegos: ")
        print("")

        try:
            inicio_laboral = datetime.date.today() - datetime.timedelta(days=int(años_de_desarrollo) * 365)
            if inicio_laboral < fecha_datetime:
                raise ValueError
        except ValueError:
            print("Años de desarrollo invalido")
            time.sleep(2)
            self.Menu_principal()

        # Roles
        roles = ["Diseñador", "Productor", "Programador", "Tester"]
        contador = 1
        for rol in roles:
            print(f"{contador}. {rol}")
            contador += 1
        print("")
        try:
            rol = int(input("Ingresar Seleccion: "))
            if rol - 1 >= 0 and rol - 1 <= 3:
                rol = roles[rol-1]
            else:
                raise ValueError
        except ValueError:
            print("Rol Fuera de rango")
            time.sleep(2)
            self.Menu_principal()

        # agrego el desarrollador
        self.desarrolladores.append(Desarrollador(
            cedula, nombre, apellido, pais_origen, fecha, int(años_de_desarrollo), rol))
        print("Desarollador agregado correctamente!")
        time.sleep(2)
        return self.Menu_principal()

    def existe_desarrollador(self, ci):
        existe = False
        for dev in self._desarrolladores:
            if dev.cedula == ci:
                existe = True
        return existe

    def pedir_fecha(self):
        try:
            date_input = input(" - Ingresar Fecha de nacimiento (DD/MM/AAAA): ")
            date_formating = date_input.split("/")
            date_formating = datetime.date(int(date_formating[2]), int(date_formating[1]), int(date_formating[0]))
            if datetime.date.today() < date_formating:
                raise ValueError
        except:
            print("Fecha de Nacimiento inválido, intente nuevamente")
            time.sleep(2)
            self.Menu_principal()
        return date_input, date_formating

    def Alta_videojuego(self):
        # nombre de juego
        print("Alta de videojuego (ingresar 0 para salir):")
        nombre = input(" - Ingrese nombre del videjuego: ")
        if len(self.videojuegos) != 0:
            try:
                for videjuego in self.videojuegos:
                    if videjuego.nombre == nombre:
                        raise ValueError
            except:
                print("{} ya esta registrado".format(nombre))
                time.sleep(2)
                self.Menu_principal()
        # categoria de juego
        categoria = input(" - Ingrese categorías del videojuego (1: Acción, 2: Aventura, 3: Estrategia, 4: Puzzle): ")
        categorias = ["Acción", "Aventura", " Estrategia", "Puzzle"]
        categorias_juego = []

        try:
            categoria = set(categoria.split(','))
            categoria = [int(x) for x in categoria]
            for i in categoria:
                if i-1 <= 3 and i-1 >= 0:
                    categorias_juego.append(categorias[i-1])
                else:
                    raise ValueError
        except ValueError:
            print("categorias {} invalidas".format(categoria))
            time.sleep(2)
            self.Menu_principal()

        # integrates de juego
        integrantes = []
        cantidad_de_integrantes = None
        # compruebo que el dato ingresado por el usuario es valido
        try:
            cantidad_de_integrantes = int(input(' - Ingresar cantidad de integrantes (minimo 8): '))
            if cantidad_de_integrantes < 8:
                raise ValueError
        except ValueError:
            if cantidad_de_integrantes is None:
                print("Valor invalido")
                time.sleep(2)
                self.Menu_principal()
            else:
                print("Minimo de integrantes 8, usted digito {}".format(cantidad_de_integrantes))
                time.sleep(2)
                self.Menu_principal()

        # pregunto la cedula de los integrantes
        for i in range(cantidad_de_integrantes):
            cedula_desarrollador = int(input(" - Ingrese cédula de desarrollador(" + str(i+1) + " de " + str(cantidad_de_integrantes) + "): "))
            # compruebo que el desarrollador exista, y no este duplicado
            try:
                if not self.existe_desarrollador(int(cedula_desarrollador)) or cedula_desarrollador in integrantes:
                    raise ValueError
            except ValueError:
                print("cedula {} es invalida o ya fue cargada anteriormente".format(cedula_desarrollador))
                time.sleep(2)
                self.Menu_principal()
            if len(self.videojuegos) != 0:
                try:
                    for otro_videjuego in self.videojuegos:
                        for dev_otro_videjuego in otro_videjuego.desarrolladores_asociados:
                            if dev_otro_videjuego.cedula == int(cedula_desarrollador):
                                raise ValueError
                except:
                    print("desarrollador {} esta asociado a otro juego".format(cedula_desarrollador))
                    time.sleep(2)
                    self.Menu_principal()
            integrantes.append(cedula_desarrollador)

        # creo el objeto videojuego
        videojuego = Videojuego(nombre, categorias_juego)

        # busco y agrego el objeto desarrollador mediante la cedula
        for ci_desarrollador in integrantes:
            for desarollador in self.desarrolladores:
                if int(ci_desarrollador) == desarollador.cedula:
                    videojuego.desarrolladores_asociados.append(desarollador)

        # compruebo el minimo de tecnicos
        try:
            if not videojuego.cumple_minimo():
                raise ValueError
        except ValueError:
            print("el juego {} no cumple con el minimo de composicion".format(videojuego.nombre))
            time.sleep(2)
            self.Menu_principal()

        # agrego el videjuego a la comptenecia
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
        
        try:
            categoria = int(input(" - Ingrese categoría del videojuego para la competencia: "))
            if categoria < 1 or 4 < categoria:
                raise ValueError
        except:
            print("Seleaccion Invalida")
            time.sleep(2)
            self.Menu_principal()
        
        for videojuego in self.videojuegos:
            videojuego.calc_puntaje()

        categoria1 = categorias[categoria-1]

        competidores = [
            videojuego for videojuego in self.videojuegos if categoria1 in videojuego.categoria]

        podio = []
        for videojuego in competidores:
            value = videojuego.puntaje
            nombre = videojuego.nombre
            cant_trabajadores = len(videojuego.desarrolladores_asociados)
            podio.extend([[value, nombre, cant_trabajadores]])

        podio = sorted(podio, key=lambda posicion_1: (posicion_1[0], posicion_1[2], posicion_1[1]) , reverse=True)
        contador = 1
        if len(podio) != 0:
            for ganadores in podio[:3]:
                print(f' {contador} {ganadores[1]} Puntaje {ganadores[0]} Trabajadores {ganadores[2]} ')
                contador += 1
        else:
            print(f'No hay videjuegos para la categoria {categoria1}')
        time.sleep(2)
        self.Menu_principal()

    def determinar_10_mejores(self):
        podio = []
        for desarrollador in self.desarrolladores:
            value = desarrollador.cantidad_de_años_de_desarollo
            nombre = desarrollador
            podio.extend([[value, nombre]])

        podio = sorted(podio, key=lambda posicion_1: posicion_1[0], reverse=True)
        podio = [persona[1] for persona in podio]

        cont = 1
        for integrante in podio[:10]:
            print(f'posicion nº {cont} \n{integrante.__dict__}\n')
            cont += 1
        time.sleep(2)
        self.Menu_principal()

    def determinar_5_mejores(self):
        listita = [programador for programador in self.desarrolladores if programador.rol == "Programador"]
        podio = []

        for desarollador in listita:
            value = desarollador.cantidad_de_años_de_desarollo
            nombre = desarollador
            podio.extend([[value, nombre]])

        podio = sorted(podio, key=lambda posicion_1: posicion_1[0], reverse=True)
        podio = [persona[1] for persona in podio]

        cont = 1
        for integrante in podio[:5]:
            print(f'posicion nº {cont} \n{integrante.__dict__}\n')
            cont += 1
        time.sleep(2)
        self.Menu_principal()

    def determinar_los_7_desarrolladores_de_edad_mas_avanzada(self):
        podio = []
        for desarollador in self.desarrolladores:
            date_format = desarollador.fecha_de_nacimiento.split("/")
            date_format = int(date_format[2] + date_format[1] + date_format[0])
            nombre = desarollador
            podio.extend([[date_format, nombre]])
        
        podio = sorted(podio, key=lambda posicion_1: posicion_1[0])
        podio = [persona[1] for persona in podio]
        cont = 1
        for integrante in podio[:7]:
            print(f'posicion nº {cont} \n{integrante.__dict__}\n')
            cont += 1
        time.sleep(2)
        self.Menu_principal()

    def determinar_el_videojuego_con_mas_desarrolladores_uruguayos(self):
        podio = []

        for videojuego in self.videojuegos:
            value = len([desarollador for desarollador in videojuego.desarrolladores_asociados if desarollador.pais_de_origen == "Uruguay"])
            nombre = videojuego
            podio.extend([[value, nombre]])

        podio = sorted(podio, key=lambda posicion_1: posicion_1[0], reverse=True)
        podio = [persona[1] for persona in podio]
        
        print(podio[0])
        time.sleep(2)
        self.Menu_principal()
        
        
    def Realizar_consulta(self):
        print("Realizar Consulta")
        print("1. Determine los 10 mejores desarrolladores registrados (basados en años de desarrollo)")
        print("2. Determine los 5 mejores desarrolladores con el rol de Programador (basados en años de desarrollo)")
        print("3. Determine los 7 desarrolladores registrados con edad más avanzada")
        print("4. Determine el videojuego con más desarrolladores que provienen de Uruguay")
        print("")
        try:
            seleccion = int(input("Ingresar seleccion: "))
            if seleccion > 4 or seleccion < 1:
                raise ValueError
        except ValueError:
            print("seleccion invalida")
            time.sleep(2)
            self.Menu_principal()
        if seleccion == 1:
            self.determinar_10_mejores()
        elif seleccion == 2:
            self.determinar_5_mejores()
        elif seleccion == 3:
            self.determinar_los_7_desarrolladores_de_edad_mas_avanzada()
        elif seleccion == 4:
            self.determinar_el_videojuego_con_mas_desarrolladores_uruguayos()
        

    def Finalizar_programa(self):
        print("Finalizar programa...")
        time.sleep(2)
        exit()


# with open("data.txt","wb") as f:
