import sys
import os


from flask_restful import Resource
from flask import jsonify

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)
from database.google_trends.countries import get_countries

class Countries(Resource):

    def get(self):
        response =  get_countries()
        return jsonify(response)