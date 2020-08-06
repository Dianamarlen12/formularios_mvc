import web

import mvc.models.personas as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/")

class List():

    def GET(self):
        try:
            result = model_alumnos.select()
            print(result)
            return render.list(result)
        except Exception as e:
            print(e)
            return "Error" + str(e.args)