from Entities.Desarrollador import Desarrollador
from Entities.Videojuegos import Videojuego
from menu import Competencia
from Exceptions.FaltanIntegrantes import FaltanIntegrantes

if __name__ == "__main__":
    # Carga de datos del team 1
    # Persona1 = Desarrollador(53612131, "Tomas", "Munoz","Uruguay", "18/10/2003", 2, "Diseñador")
    # Persona2 = Desarrollador(53612132, "Tomas", "Munoz","Uruguay", "18/10/2003", 2, "Diseñador")
    # Persona3 = Desarrollador(53612133, "Tomas", "Munoz","Uruguay", "18/10/2003", 2, "Productor")
    # Persona4 = Desarrollador(53612134, "Tomas", "Munoz","Uruguay", "18/10/2003", 2, "Programador")
    # Persona5 = Desarrollador(53612135, "Tomas", "Munoz","Uruguay", "18/10/2003", 2, "Programador")
    # Persona6 = Desarrollador(53612136, "Tomas", "Munoz","Uruguay", "18/10/2003", 2, "Programador")
    # Persona7 = Desarrollador(53612137, "Tomas", "Munoz","Uruguay", "18/10/2003", 2, "Tester")
    # Persona8 = Desarrollador(53612138, "Tomas", "Munoz","Uruguay", "18/10/2003", 2, "Tester")
    # Team1 = Videojuego("Lospibes", "Acción")
    # Team1.desarrolladores_asociados.extend([Persona1, Persona2, Persona3, Persona4, Persona5, Persona6, Persona7, Persona8])

    # # Carga de datos del team 2
    # Persona9 = Desarrollador(43612131, "Tomas", "Munoz", "Argentina", "18/10/2003", 10, "Diseñador")
    # Persona10 = Desarrollador(43612132, "Pedrito", "Munoz", "Uruguay", "18/10/2003", 9, "Diseñador")
    # Persona11 = Desarrollador(43612133, "Pedrolo", "Munoz", "Uruguay", "18/10/2003", 8, "Productor")
    # Persona12 = Desarrollador(43612134, "Pepe", "Ortiz", "Uruguay", "18/10/2003", 5, "Programador")
    # Persona13 = Desarrollador(43612135, "Tomas", "Munoz","Uruguay", "18/10/2003", 4, "Programador")
    # Persona14 = Desarrollador(43612136, "Tomas", "Munoz","Uruguay", "18/10/2003", 4, "Programador")
    # Persona15 = Desarrollador(43612137, "Tomas", "Munoz","Uruguay", "18/10/2003", 4, "Tester")
    # Persona16 = Desarrollador(43612138, "Tomas", "Munoz","Uruguay", "18/10/2003", 4, "Tester")
    # Team2 = Videojuego("Los pibardos", "Acción")
    # Team2.desarrolladores_asociados.extend([Persona9, Persona10, Persona11, Persona12, Persona13, Persona14, Persona15, Persona16])
    
    # carga de datos de Competencia
    competencia = Competencia()
    # competencia.desarrolladores.extend([Persona1, Persona2, Persona3, Persona4, Persona5, Persona6, Persona7, Persona8, Persona9, Persona10, Persona11, Persona12, Persona13, Persona14, Persona15, Persona16])
    # competencia.videojuegos.extend([Team1, Team2])
    
    competencia.Menu_principal()

    print("hola")