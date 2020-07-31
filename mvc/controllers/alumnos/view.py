import web

import mvc.models.personas as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class View():

    def GET(self, id_alumno):
        try:
            result = model_alumnos.view(id_alumno)[0]
            return render.view(result) # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)