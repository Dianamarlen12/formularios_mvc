import web

render = web.template.render("mvc/views/alumnos/", base="template)

class Insert():

    def GET(self):
        try:
            return render.insert() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self):
        try:
            form = web.input()
            print(form)
        except Exception as e:
            return "Error "