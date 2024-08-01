import sys
import os


from flask_restful import Resource, request
from flask import jsonify

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)
from database.google_trends.realtime_trending_searches import get_realtime_trending_data, get_realtime_count_and_unique_count

class Realtime(Resource):
    def get(self):
        country_id = request.form('country_id')
        start = request.form('start')
        end = request.form('end')
        rank_min = request.form('rank_min')
        rank_max = request.form('rank_max')
        limit = request.form('limit')
        offset = request.form('offset')
        data_response = []
        data = get_realtime_trending_data(country_id, start, end, rank_min, rank_max, limit, offset)
        if data is None:
            return jsonify(None)
        counts = get_realtime_count_and_unique_count(country_id, start, end, rank_min, rank_max, limit)
        for record in data:
            search_id, rank, search, timestamp, country_name = record
            data_response.append((
                search_id,
                rank,
                search,
                str(timestamp),
                country_name
            ))
        response = {
            'data': data_response,
            'total_count': counts[0],
            'unique_count': counts[1]
        }
        return jsonify(response)


