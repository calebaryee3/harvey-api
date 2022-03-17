from unicodedata import name
from flask import Flask
#import json

from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import random
app = Flask(__name__)
api = Api(app)
data=json.load(open('Harvey.json'))
@app.route("/")
def main():
    return "<h1> Harvey Specter quotes API </h1>"

class Harvey(Resource):
    # methods go here
     def get(self,number=None): 
         
         #data = data.to_dict()  
         if number != None:
             getRandomQuoteFromArray = random.sample(data,number)
             return {'data': getRandomQuoteFromArray},200
         else:
             return {'data': random.choice(data)}, 200  # return data and 200 OK code
             

api.add_resource(Harvey,'/harvey' ,'/harvey/<int:number>')  # '/users' is our entry point
#api.add_resource(Harvey, '/harvey')

        
        
if __name__ == '__main__':
    app.run(debug=True)
    
    

