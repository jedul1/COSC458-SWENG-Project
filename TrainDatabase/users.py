from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
#import ast


app = Flask(__name__)
api = Api(app)

user_path = "trainusers.csv"



DISCOUNT_MILEAGE_LIMIT = 400

user_data = pd.read_csv(user_path)
trainusers = user_data.to_dict()

class User(Resource):
  def __init__(self, name, id):
    self.name = name
    self.id = id
    self.Miles = 0
  
  def createUser(self):

    user_data = {
      'name': [self.name], 
      'id': [self.id], 
      'Miles': [self.Miles]
    }
    new_data = pd.DataFrame(user_data)
    new_data.to_csv(user_path, mode = 'a', index=False, header=False)

  
    

  def getMiles(self):
    user_data = pd.read_csv(user_path)
    user_data = user_data.to_dict()
    name = self.name
    name_dict = user_data['name']
    miles_dict = user_data['Miles']
    for key in (name_dict):
      if name_dict[key] == name:
        return miles_dict[key]
        
  def getUserId(self):
    user_data = pd.read_csv(user_path)
    user_data = user_data.to_dict()
    name = self.name
    name_dict = user_data['name']
    id_dict = user_data['id']
    for key in (name_dict):
      if name_dict[key] == name:
        return id_dict[key]
      
    

  def isEligibleForDiscount(self):
    global DISCOUNT_MILEAGE_LIMIT
    miles_traveled = self.getMiles()
    if miles_traveled >= DISCOUNT_MILEAGE_LIMIT:
      return True
    else:
      return False

  
  def updateMiles(self, new_miles):
    user_data = pd.read_csv(user_path)
    user_data = user_data.to_dict()
    name = self.name
    current_miles = ""
    name_dict = user_data['name']
    miles_dict = user_data['Miles']
    for key in (name_dict):
      if name_dict[key] == name:
        current_miles = miles_dict[key]
        new_miles = new_miles + current_miles
        miles_dict[key] = new_miles
  
    user_data = pd.DataFrame(user_data)
    user_data.to_csv(user_path, mode = 'w', index=False, header=True)
    

  
  

api.add_resource(User,"/users")

if __name__ == "__main__":
  app.run()


