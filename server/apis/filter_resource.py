import sys
import os


from flask_restful import Resource, request
from flask import jsonify

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)
from database.google_trends.trending_searches import get_trending_data, get_trending_count_and_unique_count
from database.google_trends.realtime_trending_searches import get_realtime_trending_data, get_realtime_count_and_unique_count
from database.google_trends.today_searches import get_today_count_and_unique_count, get_today_data
from database.google_trends.countries import get_country_by_id

def get_all_data(country_id, start, end, rank_min, rank_max, limit, offset):
    country = get_country_by_id(country_id)
    country_name = country[1]
    # Fetch counts and unique counts
    trending_count, trending_unique_count = get_trending_count_and_unique_count(country_id, start, end, rank_min, rank_max, limit)
    realtime_count, realtime_unique_count = get_realtime_count_and_unique_count(country_id, start, end, rank_min, rank_max, limit)
    today_count, today_unique_count = get_today_count_and_unique_count(country_id, start, end, rank_min, rank_max, limit)

    # Fetch data
    trending_data = get_trending_data(country_id, start, end, rank_min, rank_max, limit, offset)
    realtime_data = get_realtime_trending_data(country_id, start, end, rank_min, rank_max, limit, offset)
    today_data = get_today_data(country_id, start, end, rank_min, rank_max, limit, offset)

    # Collect unique search IDs
    unique_searches = dict()

    trending_response = []
    realtime_response = []
    today_response = []

    for record in trending_data:
        search_id, rank, search, timestamp = record
        trending_response.append((search_id, rank, search, str(timestamp)))
        unique_searches.update({search_id: search})


    for record in realtime_data:
        search_id, rank, search, timestamp = record
        realtime_response.append((search_id, rank, search, str(timestamp)))
        unique_searches.update({search_id: search})


    for record in today_data:
        search_id, rank, search, timestamp = record
        today_response.append((search_id, rank, search, str(timestamp)))
        unique_searches.update({search_id: search})


    total_unique_count = len(unique_searches)

    total_count = trending_count + realtime_count + today_count

    # Prepare the result dictionary
    result = {
        "country": country_name,
        "trending_data": trending_response,
        "trending_count": trending_count,
        "trending_unique_count": trending_unique_count,
        "realtime_data": realtime_response,
        "realtime_count": realtime_count,
        "realtime_unique_count": realtime_unique_count,
        "today_data": today_response,
        "today_count": today_count,
        "today_unique_count": today_unique_count,
        "unique_searches": unique_searches,
        "total_count": total_count,
        "total_unique_count": total_unique_count
    }

    return result


class Filter(Resource):

    def post(self):
        data = request.get_json()
        country_id = data.get('country_id')
        start = data.get('start')
        end = data.get('end')
        rank_min = data.get('rank_min')
        rank_max = data.get('rank_max')
        limit = data.get('limit')
        offset = data.get('offset', 0)

        
        response = get_all_data(country_id, start, end, rank_min, rank_max, limit, offset)
        return jsonify(response)
