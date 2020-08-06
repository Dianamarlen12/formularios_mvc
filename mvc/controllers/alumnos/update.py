import web

import mvc.models.personas as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class Update():

    def GET(self, id_alumno):
        try:
            result = model_alumnos.view(id_alumno)[0]
            print(result)
            return render.update(result) # renderizando formulario.html
        except Exception as e:
            return "Error "

    def POST(self,id_alumno):
        try:
            form = web.input()
            print(form)
            id_alumno = form.id_alumno
            matricula = form.matricula
            nombre = form.nombre
            apellido_paterno = form.apellido_paterno
            apellido_materno = form.apellido_materno
            edad = form.edad
            fecha_nacimiento = form.fecha_nacimiento
            sexo = form.sexo
            estado_civil = form.estado_civil
            result = model_alumnos.update(id_alumno,matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"    