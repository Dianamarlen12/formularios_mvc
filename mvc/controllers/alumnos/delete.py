import web

render = web.template.render("mvc/views/almunos/", base="template)

class Delete():

    def GET(self):
        try:
            return render.delete() # renderizando formulario.html
        except Exception as e:
            return "Error " + str(e.args)
        