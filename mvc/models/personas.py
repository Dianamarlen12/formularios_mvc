import mysql.connector

class Alumnos():
    
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='Mongo_db', 
                password='Agenda.2020',
                host='127.0.0.1',
                port=3309,
                database='agenda_db'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    " METODO PARA SELECCIONAR "
    def select(self):
        try:
            self.connect()
            query = ("SELECT * FROM alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                diccionario = {
                    "id_alumno":row[0],
                    "matricula":row[1],
                    "nombre":row[2],
                    "apellido_paterno":row[3],
                    "apellido_materno":row[4],
                    "edad":row[5],
                    "fecha_nacimiento":row[6],
                    "sexo":row[7],
                    "estado_civil":row[8]
                }
                result.append(diccionario)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

object = Alumnos()
object.connect()

for row in object.select():
    print(row)