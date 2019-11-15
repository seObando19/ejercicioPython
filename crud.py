import sqlite3


def crearTabla():
    conexion = sqlite3.connect('colegio.db')
    cursor=conexion.cursor
    sql ='''
            CREATE TABLE estudiantes(
                id INTEGER PRIMARY KEY,
                nombre VARCHAR(100),
                apellido VARCHAR(100),
                cedula VARCHAR(20),
                telefono VARCHAR(100)

            )
            '''
            cursor.execute(sql)
            conexion.commit
            conexion.close()

def addUser(id,nombre,apellido,cedula,telefono):
    conexion = sqlite3.connect('colegio.db')
    cursor=conexion.cursor
    sql ='''
            INSERT INTO estudiantes(
                id,nombre,apellido,cedula,telefono) VALUES(?,?,?,?,?)
            '''
            cursor.execute(sql(id,nombre,apellido,cedula,telefono))
            conexion.commit
            conexion.close()

def obtenerEstudiante():
	conn = sqlite3.connect('basededatos.sqlite')

	cursor = conn.cursor()

	sql = '''
	    SELECT cedula, nombre, telefono
	    FROM student
	'''

	cursor.execute(sql)
	resultado = cursor.fetchall()

	conn.commit()
	conn.close()

	return resultado
def actualizarEstudiante(cedula,nombre,telefono):
	conn = sqlite3.connect('basededatos.sqlite')

	cursor = conn.cursor()

	sql = '''
	    UPDATE student
	    SET nombre = ?, telefono = ?
	    WHERE cedula = ?
	'''

	cursor.execute(sql,(nombre,telefono,cedula))

	conn.commit()
	conn.close()


def eliminarEstudiante(cedula):
	conn = sqlite3.connect('basededatos.sqlite')

	cursor = conn.cursor()

	sql = '''
	    DELETE
	    FROM student
	    WHERE cedula = {}
	''' .format(cedula)

	cursor.execute(sql)
	resultado = cursor.fetchall()

	conn.commit()
	conn.close()

	return resultado