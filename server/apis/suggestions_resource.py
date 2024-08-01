import sys
import os


from flask_restful import Resource, request
from flask import jsonify

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)
from utils.data_searching import suggestion_search


class Suggestion(Resource):
    def post(self):
        data = request.get_json()
        searches = data.get('searches')
        category_words = data.get('category_words')
        response = suggestion_search(searches, category_words)
        return jsonify(response)