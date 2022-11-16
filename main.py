from Entities.Desarrollador import Desarrollador
from Entities.Videojuegos import Videojuego
from Entities.Competencia import Competencia

if __name__ == "__main__":
    # Carga de datos del team 1
    Persona1 = Desarrollador(10000001, "Ricardo", "Jurado","Uruguay", "01/01/2003", 2, "Diseñador")
    Persona2 = Desarrollador(10000002, "Joseba", "Giraldo","Uruguay", "02/01/2003", 2, "Diseñador")
    Persona3 = Desarrollador(10000003, "Maider", "Ramos","Uruguay", "03/01/2003", 2, "Productor")
    Persona4 = Desarrollador(10000004, "Piedad", "Zhu","Uruguay", "04/01/2003", 2, "Programador")
    Persona5 = Desarrollador(10000005, "Adoracion", "Zaragoza", "Uruguay", "05/10/2003", 2, "Programador")
    Persona6 = Desarrollador(10000006, "Mara", "Hurtado","Uruguay", "06/01/2003", 2, "Programador")
    Persona7 = Desarrollador(10000007, "Leonardo", "Palau","Uruguay", "07/01/2003", 2, "Tester")
    Persona8 = Desarrollador(10000008, "Samira", "Peral","Uruguay", "08/01/2003", 2, "Tester")
    Team1 = Videojuego("God of Wars IV", ["Acción"])
    Team1.desarrolladores_asociados.extend([Persona1, Persona2, Persona3, Persona4, Persona5, Persona6, Persona7, Persona8])

    # # Carga de datos del team 2
    Persona9  = Desarrollador(10000009, "Joan", "Carranza", "Argentina", "01/02/2003", 10, "Diseñador")
    Persona10 = Desarrollador(10000010, "Anastasio", "Giron", "Uruguay", "02/02/2003", 9, "Diseñador")
    Persona11 = Desarrollador(10000011, "Yeray", "Vallejo", "Uruguay", "03/02/2003", 8, "Productor")
    Persona12 = Desarrollador(10000012, "Francisco", "Zamora", "Uruguay", "04/02/2003", 5, "Programador")
    Persona13 = Desarrollador(10000013, "Celso", "Arenas","Uruguay", "05/02/2003", 4, "Programador")
    Persona14 = Desarrollador(10000014, "Igor", "Rivero","Uruguay", "06/02/2003", 4, "Programador")
    Persona15 = Desarrollador(10000015, "Juana", "Pereira","Uruguay", "07/02/2003", 4, "Tester")
    Persona16 = Desarrollador(10000016, "Camilo", "Tellez","Uruguay", "08/02/2003", 4, "Tester")
    Team2 = Videojuego("Grand Theft Auto V", ["Acción", "Aventura"])
    Team2.desarrolladores_asociados.extend([Persona9, Persona10, Persona11, Persona12, Persona13, Persona14, Persona15, Persona16])
    
    # Carga de datos del team 3
    Persona17 = Desarrollador(10000017, "Joan", "Carranza", "Argentina", "01/01/2002", 10, "Diseñador")
    Persona18 = Desarrollador(10000018, "Anastasio", "Giron", "Uruguay", "02/01/2002", 9, "Diseñador")
    Persona19 = Desarrollador(10000019, "Yeray", "Vallejo", "Uruguay", "03/01/2002", 8, "Productor")
    Persona20 = Desarrollador(10000020, "Francisco", "Zamora", "Uruguay", "04/01/2002", 5, "Programador")
    Persona21 = Desarrollador(10000021, "Celso", "Arenas","Uruguay", "01/02/2002", 4, "Programador")
    Persona22 = Desarrollador(10000022, "Igor", "Rivero","Uruguay", "02/02/2002", 4, "Programador")
    Persona23 = Desarrollador(10000023, "Juana", "Pereira","Uruguay", "03/02/2002", 4, "Tester")
    Persona24 = Desarrollador(10000024, "Camilo", "Tellez","Uruguay", "04/02/2002", 4, "Tester")
    Team3 = Videojuego("Grand Theft Auto IV", ["Acción", "Aventura"])
    Team3.desarrolladores_asociados.extend([Persona17, Persona18, Persona19, Persona20, Persona21, Persona22, Persona23, Persona24])
    
    # carga de datos de Competencia
    competencia = Competencia()
    competencia.desarrolladores.extend([Persona1, Persona2, Persona3, Persona4, Persona5, Persona6, Persona7, Persona8, Persona9, Persona10, Persona11, Persona12, Persona13, Persona14, Persona15, Persona16, Persona17, Persona18, Persona19, Persona20, Persona21, Persona22, Persona23, Persona24])
    competencia.videojuegos.extend([Team3, Team2])
    
    competencia.Menu_principal()