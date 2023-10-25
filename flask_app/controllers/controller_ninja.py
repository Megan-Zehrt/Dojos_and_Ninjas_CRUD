from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.model_ninja import Ninja
from flask_app.models.model_dojo import Dojo

#Create ninja
@app.route("/ninjas")
def new_ninja():
   dojos= Dojo.get_all()
   print(dojos)
   return render_template("Ninja.html", dojos=dojos)

@app.route("/create_ninja", methods=['POST'])
def create_ninja():
   data = {
      'first_name': request.form['first_name'],
      'last_name': request.form['last_name'],
      'age': request.form['age'],
      'dojo_id': request.form['dojos']
   }
   id = Ninja.create_one(data)
   return redirect("/dojos")


