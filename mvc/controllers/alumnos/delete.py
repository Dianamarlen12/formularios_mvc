import web

import mvc.models.personas as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class Delete():

    def GET(self, id_alumno):
        try:
            result = model_personas.view(id_persona)[0]
            return render.delete(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)


    def POST(self, id_alumno):
        try:
            form = web.input()
            id_alumno = form.id_alumno # hidden
            result = model_personas.delete(id_alumno)
            web.seeother('/list')
        except Exception as e:
            print(e)
            return "Error"