from Entities.Desarrollador import Desarrollador
from Entities.Videojuegos import Videojuego
from Competencia import Competencia
from Exceptions.FaltanIntegrantes import FaltanIntegrantes

if __name__ == "__main__":
    # Carga de datos del team 1
    Persona1 = Desarrollador(10000001, "Ricardo", "Jurado","Uruguay", "18/10/2003", 2, "Diseñador")
    Persona2 = Desarrollador(10000002, "Joseba", "Giraldo","Uruguay", "18/10/2003", 2, "Diseñador")
    Persona3 = Desarrollador(10000003, "Maider", "Ramos","Uruguay", "18/10/2003", 2, "Productor")
    Persona4 = Desarrollador(10000004, "Piedad", "Zhu","Uruguay", "18/10/2003", 2, "Programador")
    Persona5 = Desarrollador(10000005, "Adoracion", "Zaragoza","Uruguay", "18/10/2003", 2, "Programador")
    Persona6 = Desarrollador(10000006, "Mara", "Hurtado","Uruguay", "18/10/2003", 2, "Programador")
    Persona7 = Desarrollador(10000007, "Leonardo", "Palau","Uruguay", "18/10/2003", 2, "Tester")
    Persona8 = Desarrollador(10000008, "Samira", "Peral","Uruguay", "18/10/2003", 2, "Tester")
    Team1 = Videojuego("Lospibes", "Acción")
    Team1.desarrolladores_asociados.extend([Persona1, Persona2, Persona3, Persona4, Persona5, Persona6, Persona7, Persona8])

    # # Carga de datos del team 2
    Persona9  = Desarrollador(10000009, "Joan", "Carranza", "Argentina", "18/10/2003", 10, "Diseñador")
    Persona10 = Desarrollador(10000010, "Anastasio", "Giron", "Uruguay", "18/10/2003", 9, "Diseñador")
    Persona11 = Desarrollador(10000011, "Yeray", "Vallejo", "Uruguay", "18/10/2003", 8, "Productor")
    Persona12 = Desarrollador(10000012, "Francisco", "Zamora", "Uruguay", "18/10/2003", 5, "Programador")
    Persona13 = Desarrollador(10000013, "Celso", "Arenas","Uruguay", "18/10/2003", 4, "Programador")
    Persona14 = Desarrollador(10000014, "Igor", "Rivero","Uruguay", "18/10/2003", 4, "Programador")
    Persona15 = Desarrollador(10000015, "Juana", "Pereira","Uruguay", "18/10/2003", 4, "Tester")
    Persona16 = Desarrollador(10000016, "Camilo", "Tellez","Uruguay", "18/10/2003", 4, "Tester")
    # Team2 = Videojuego("Los pibardos", "Acción")
    # Team2.desarrolladores_asociados.extend([Persona9, Persona10, Persona11, Persona12, Persona13, Persona14, Persona15, Persona16])
    
    # carga de datos de Competencia
    competencia = Competencia()
    competencia.desarrolladores.extend([Persona1, Persona2, Persona3, Persona4, Persona5, Persona6, Persona7, Persona8, Persona9, Persona10, Persona11, Persona12, Persona13, Persona14, Persona15, Persona16])
    competencia.videojuegos.extend([Team1])
    
    competencia.Menu_principal()