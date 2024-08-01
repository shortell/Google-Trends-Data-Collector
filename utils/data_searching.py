import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from utils.data_analysis import calculate_average_rank
from utils.data_collection import store_suggestions
from database.google_trends.suggestions import get_suggestions_by_search_id
from database.google_trends.countries import get_country_by_id
from database.google_trends.today_searches import get_today_data, get_today_search_rank_overtime
from database.google_trends.realtime_trending_searches import get_realtime_trending_data, get_realtime_search_rank_overtime
from database.google_trends.trending_searches import get_trending_data, get_trending_search_rank_overtime


def get_all_data(country_id, start, end, rank_min, rank_max, limit, offset):
    country = get_country_by_id(country_id)
    country_name = country[1]
    # Fetch counts and unique counts

    # Fetch data
    trending_data = get_trending_data(
        country_id, start, end, rank_min, rank_max, limit, offset)
    realtime_data = get_realtime_trending_data(
        country_id, start, end, rank_min, rank_max, limit, offset)
    today_data = get_today_data(
        country_id, start, end, rank_min, rank_max, limit, offset)

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

    # Prepare the result dictionary
    result = {
        "country": country_name,
        "trending_data": trending_response,
        "realtime_data": realtime_response,
        "today_data": today_response,
        "unique_searches": unique_searches
    }

    return result


def check_if_word_contains_word(checked_word: str, containing_word: str):
    return (checked_word.lower() in containing_word.lower())


def suggestion_search(searches: dict, cat_word: str):
    found_searches = []
    for search_id, search in searches.items():
        suggestions = get_suggestions_by_search_id(search_id)
        if len(suggestions) == 0:
            store_suggestions(search_id, search)
            suggestions = get_suggestions_by_search_id(search_id)

        if check_if_word_contains_word(cat_word, search):
            record = (search_id, search, cat_word)
            found_searches.append(record)
            continue  # move to the next search

        for sug_word in suggestions:
            if check_if_word_contains_word(cat_word, sug_word[0]):
                print(cat_word, sug_word[0])
                    
                    

                record = (search_id, search, sug_word[0])
                # print(record)
                found_searches.append(record)
                # print(sug_word)
                break  # Exit the suggestions loop and move to the next search

    return found_searches


def find_search(country_id, start, end, rank_min, rank_max, limit, offset, cat_word):
    result = get_all_data(country_id, start, end,
                          rank_min, rank_max, limit, offset)

    unique_searches = result['unique_searches']

    # print(unique_searches)

    found_searches = suggestion_search(unique_searches, cat_word)
    if len(found_searches) == None:
        return None
    searches_avg_rank = []
    for record in found_searches:
        search_id, search, _ = record
        realtime_rank_ot = get_realtime_search_rank_overtime(
            country_id, search_id, start, end)
        trending_rank_ot = get_trending_search_rank_overtime(
            country_id, search_id, start, end)
        today_rank_ot = get_today_search_rank_overtime(
            country_id, search_id, start, end)
        all_averages = []
        realtime_avg_rank = calculate_average_rank(realtime_rank_ot)
        if realtime_avg_rank != -1:
            all_averages.append(realtime_avg_rank)
        trending_avg_rank = calculate_average_rank(trending_rank_ot)
        if trending_avg_rank != -1:
            all_averages.append(trending_avg_rank)
        today_avg_rank = calculate_average_rank(today_rank_ot)
        if today_avg_rank != -1:
            all_averages.append(today_avg_rank)

        overall_avg = sum(all_averages) / len(all_averages)

        new_record = (search_id, search, overall_avg)
        searches_avg_rank.append(new_record)

    return searches_avg_rank

