import mysql.connector
class Alumnos():
    
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='ue0647dj82tqfwn4', 
                password='pb9ouxzef5hl5zqp',
                host='q57yawiwmnaw13d2.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port=3306,
                database='r41eax92x64eqwz5'
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

    def view(self, id_alumno):
        try:
            self.connect()
            query = ("SELECT * FROM alumnos where id_alumno = %s;")
            values = (id_alumno,)
            self.cursor.execute(query, values)
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

    def insert(self,matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil):
        try:
            self.connect()
            query = ("INSERT INTO alumnos (matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil) values (%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self,id_alumno,matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil):
        try:
            self.connect()
            query = ("UPDATE alumnos SET matricula=%s,nombre=%s,apellido_paterno=%s,apellido_materno=%s,edad=%s,fecha_nacimiento=%s,sexo=%s,estado_civil=%s WHERE id_alumno=%s;")
            values = (matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil,id_alumno)
            self.cursor.execute(query, values)
            self.cnx.commit() #Almacenar cambios en la base de datos
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def delete(self, id_alumno):
        try:
            self.connect()
            query = ("DELETE FROM alumnos WHERE id_alumno = %s;")
            values = (id_alumno,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

object = Alumnos()
#object.connect()
#object.insert("1718198721","Nayla Melanie","Meneses","Vite",19,"2000/10/05","Femenino","Soltera")
#object.insert("1718198721","Diana Marlen","Meneses","Alegria",19,"2000/03/12","Femenino","Soltera")
#object.insert("1718198721","Dania Jimena","Meneses","Alegria",18,"2002/11/01","Femenino","Soltera")
#object.update(4,"1718198721","NAYLA MELANIE","MENESES","VITE",19,"2000/10/05","Femenino","Soltera")
#object.delete(4)

for row in object.select():
    print(row)