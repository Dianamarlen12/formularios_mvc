import web

render = web.template.render("mvc/views/alumnos/", base="template)

class List():

    def GET(self):
        try:
            return render.list() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)