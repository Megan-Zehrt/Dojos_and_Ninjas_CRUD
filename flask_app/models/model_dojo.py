#import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the user table from our database
from flask_app import DATABASE

class Dojo:
   def __init__(self, data:dict):
      self.id = data['id']
      self.name = data['name']
      self.created_at = data['created_at']
      self.updated_at = data['updated_at']

      #Add additional columns from database here

   def info(self):
      returnStr = f"Name = {self.name}"
      return returnStr

#CREATE
   @classmethod
   def create_one(cls, data:dict):
      query = "INSERT INTO dojos (name) VALUES (%(name)s)"
      print("this is the model file")
      result = connectToMySQL(DATABASE).query_db(query, data)
      print(data)
      return result
       
   # now we use the class methods to query our database

#READ
   @classmethod
   def get_all(cls) -> list:
      query = "SELECT * FROM dojos;"
      #make sure to call the connectToMySQL function with the schema you are targeting

      results = connectToMySQL(DATABASE).query_db(query)
      #create an empty list to append our instances of dojos
      if not results:
         return []

      instance_list = []
      # iterate over the db results anad create instances of dojos with cls.
      for dictionary in results:
         instance_list.append(cls(dictionary))
      return instance_list

   @classmethod
   def get_one(cls, data):
      query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
      results = connectToMySQL(DATABASE).query_db(query, data)
      person = cls(results[0])
      return person

   @classmethod
   def get_ninjas(cls, data):
      # query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id;"
      query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
      results = connectToMySQL(DATABASE).query_db(query, data)
      ninjas = []
      for ninja in results:
         ninjas.append(cls(ninja))
      return ninjas
