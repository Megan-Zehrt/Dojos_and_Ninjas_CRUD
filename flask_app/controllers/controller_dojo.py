from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

# Main Page + Create new Dojo
@app.route("/dojos")
def dojo():
    all_dojos = Dojo.get_all()
    return render_template("Dojo.html", all_dojos = all_dojos)

@app.route("/dojo", methods=["post"])
def dojo_page():
    data = {
      'name': request.form["name"]
    }
    Dojo.create_one(data)
    return redirect("/dojos")

# Show dojo
@app.route("/dojos/show")
def dojo_show():
   return render_template("Show.html")

@app.route("/dojos/<int:id>")
def dojo_show_id(id):
   data = {
      'id': id
   }
   one_dojo= Dojo.get_one(data)
   ninjas = Ninja.get_ninjas(data)
   print(one_dojo)
   return render_template("Show.html", one_dojo=one_dojo, ninjas=ninjas)

