from Entities.Desarolladores import Desarolladores
from Entities.Videojuegos import Videojuego
from menu import Competencia
from Exceptions.FaltanIntegrantes import FaltanIntegrantes


persona1=Desarolladores(53612131,"Tomas","Munoz","Uruguay","18/10/2003",2,"Diseñador")
persona2=Desarolladores(53612132,"Tomas","Munoz","Uruguay","18/10/2003",2,"Diseñador")
persona3=Desarolladores(53612133,"Tomas","Munoz","Uruguay","18/10/2003",2,"Productor")
persona4=Desarolladores(53612134,"Tomas","Munoz","Uruguay","18/10/2003",2,"Programador")
persona5=Desarolladores(53612135,"Tomas","Munoz","Uruguay","18/10/2003",2,"Programador")
persona6=Desarolladores(53612136,"Tomas","Munoz","Uruguay","18/10/2003",2,"Programador")
persona7=Desarolladores(53612137,"Tomas","Munoz","Uruguay","18/10/2003",2,"Tester")
persona8=Desarolladores(53612138,"Tomas","Munoz","Uruguay","18/10/2003",2,"Tester")

team1=Videojuego("Lospibes","Acción")
team1.desarolladores_asociados.extend([persona1,persona2,persona3,persona4,persona5,persona6,persona7,persona8])

Persona1=Desarolladores(43612131,"Tomas","Munoz","Argentina","18/10/2003",10,"Diseñador")
Persona2=Desarolladores(43612132,"Pedrito","Munoz","Uruguay","18/10/2003",9,"Diseñador")
Persona3=Desarolladores(43612133,"Pedrolo","Munoz","Uruguay","18/10/2003",8,"Productor")
Persona4=Desarolladores(43612134,"Pepe","Ortiz","Uruguay","18/10/2003",5,"Programador")
Persona5=Desarolladores(43612135,"Tomas","Munoz","Uruguay","18/10/2003",4,"Programador")
Persona6=Desarolladores(43612136,"Tomas","Munoz","Uruguay","18/10/2003",4,"Programador")
Persona7=Desarolladores(43612137,"Tomas","Munoz","Uruguay","18/10/2003",4,"Tester")
Persona8=Desarolladores(43612138,"Tomas","Munoz","Uruguay","18/10/2003",4,"Tester")

Team1=Videojuego("Los pibardos","Acción")
Team1.desarolladores_asociados.extend([Persona1,Persona2,Persona3,Persona4,Persona5,Persona6,Persona7,Persona8])


if __name__=="__main__":
    competencia=Competencia()
    competencia.desarolladores.extend([persona1,persona2,persona3,persona4,persona5,persona6,persona7,persona8])
    competencia.desarolladores.extend([Persona1,Persona2,Persona3,Persona4,Persona5,Persona6,Persona7,Persona8])
    
    competencia.videojuegos.extend([team1,Team1])
    competencia=competencia.Menu_principal()
    
    