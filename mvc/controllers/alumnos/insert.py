import web

import mvc.models.personas as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando formulario.html
        except Exception as e:
            return "Error " 

    def POST(self):
        try:
            form = web.input()
            print(form)
            matricula = form.matricula
            nombre = form.nombre
            apellido_paterno = form.apellido_paterno
            apellido_materno = form.apellido_materno
            edad = form.edad
            fecha_nacimiento = form.fecha_nacimiento
            sexo = form.sexo
            estado_civil = form.estado_civil
            model_alumnos.insert(matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil)
            #return render.insert()
            web.seeother('/list')
        except Exception as e:
            print(e)
            return render.insert()
    