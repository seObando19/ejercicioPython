import sqlite3

conexion = sqlite3.connect('colegio.db')

cursor = conexion.cursor()
#------------------------------LECCION 1------------------------------------------------
# Creamos el cursor
#cursor = conexion.cursor()

# Ahora crearemos una tabla de usuarios para almacenar nombres, edades y emails
    #cursor.execute("CREATE TABLE estudiante (ID INTEGER, nombre VARCHAR(100), apellido VARCHAR(100), cedula INTEGER, telefono VARCHAR(50))")

#Insertar datos
    #cursor.execute("INSERT INTO estudiante VALUES('1','Pablo','Restrepo','1490323','2274056')")
    #conexion.commit()

#Recuperar el primer registro(Devuelve en Tupla)
    #cursor.execute("SELECT * FROM estudiante")
    #print(cursor)
    #Recuperar el primer registro(Devuelve en texto)
    #usuario = cursor.fetchone()
    #print(usuario[0])
    #print(usuario[1])
    #print(usuario[2]) """

#Registrar varios estudiantes
    #estudiantes = [
    #    ('2','Marco','perez','1267934','62839430'),
    #    ('3','Alejandro','Vazquez','3782442','772994'),
    #    ('4','Antonio','Morales','1390453','36729384'),
    #    ('5','Simon','Bolivar','36782038','24629302'),
    #    ('6','Alfredo','gonzalez','734729','4792837'),
    #]
    #cursor.executemany("INSERT INTO estudiante VALUES(?,?,?,?,?)", estudiantes)

#Recuperar varios registros
    #cursor.execute("SELECT *FROM estudiante")
    #estudiantes = cursor.fetchall()
    #for estudiante in estudiantes:
    #    print("Codigo: ", estudiante[0],"Nombre: ", estudiante[1])

#------------------------------LECCION 2------------------------------------------------
#Primary key
    #cursor.execute('''
    #                  CREATE TABLE estudiante
    #                   (
    #                       ID INTEGER PRIMARY KEY,
    #                       nombre VARCHAR(100),
    #                       apellido VARCHAR(100),
    #                       cedula INTEGER,
    #                       telefono VARCHAR(50)
    #                    )
                        
    #                   ''')
    #estudiantes = [
    #        (1,'Pablo','Restrepo','1490323','2274056'),
    #        (2,'Marco','perez','1267934','62839430'),
    #        (3,'Alejandro','Vazquez','3782442','772994'),
    #        (4,'Antonio','Morales','1390453','36729384'),
    #        (5,'Simon','Bolivar','36782038','24629302'),
    #        (6,'Alfredo','gonzalez','734729','4792837'),
    #    ]
    #
    #cursor.executemany("INSERT INTO estudiante VALUES(?,?,?,?,?)", estudiantes)

#Campo Autoincremental

# Guardamos los cambios haciendo un commit
conexion.commit()
conexion.close()