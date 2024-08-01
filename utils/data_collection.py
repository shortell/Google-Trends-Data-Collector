import json
from database.google_trends.searches import add_search, get_search_id
from database.google_trends.trending_searches import add_trending_search
from database.google_trends.realtime_trending_searches import add_realtime_trending_search
from database.google_trends.today_searches import add_today_search
from database.google_trends.countries import get_countries
from database.google_trends.suggestions import add_suggestion
from input.google_trends_fetcher import fetch_trending_searches, fetch_realtime_trending_searches, fetch_today_searches, fetch_suggestions
from utils.datetime_utils import create_datetime
from utils.data_formatter import format_realtime_trending_searches_email, format_trending_searches_email, format_today_searches_email


def store_trending_searches(country_id, camel_case_name):
    """
    Fetches trending searches data for a given country and stores it in the database.

    Parameters:
        country_id (str): The identifier for the country.
        camel_case_name (str): The name of the country in camel case.

    Returns:
        dict or None: A dictionary containing the trending searches data if successful,
                      otherwise None if the response is invalid or empty.
    """
    response = fetch_trending_searches(camel_case_name)
    if response is None:
        return None
    json_data = json.loads(response.to_json())
    trending_searches = json_data["0"]
    for rank, search in trending_searches.items():
        add_search(search)
        search_id = get_search_id(search)
        timestamp = create_datetime()
        add_trending_search(rank, search_id, timestamp, country_id)
    return trending_searches


def store_realtime_trending_searches(country_id, two_letter_code):
    """
    Fetches realtime trending searches data for a given country and stores it in the database.

    Parameters:
        country_id (str): The identifier for the country.
        two_letter_code (str): The two-letter country code.

    Returns:
        dict or None: A dictionary containing the realtime trending searches data if successful,
                      otherwise None if the response is invalid or empty.
    """
    response = fetch_realtime_trending_searches(two_letter_code)
    if response is None:
        return None
    json_data = json.loads(response.to_json())
    realtime_trending_searches = json_data['entityNames']
    for rank, search_list in realtime_trending_searches.items():
        for search in search_list:
            add_search(search)
            search_id = get_search_id(search)
            timestamp = create_datetime()
            add_realtime_trending_search(
                rank, search_id, timestamp, country_id)
    return realtime_trending_searches


def store_today_searches(country_id, two_letter_code):
    """
    Fetches today's search data for a given country and stores it in the database.

    Parameters:
        country_id (str): The identifier for the country.
        two_letter_code (str): The two-letter country code.

    Returns:
        dict or None: A dictionary containing today's search data if successful,
                      otherwise None if the response is invalid or empty.
    """
    response = fetch_today_searches(two_letter_code)
    if response is None:
        return None
    json_data = json.loads(response.to_json())
    today_searches = json_data['query']
    for rank, search in today_searches.items():
        add_search(search)
        search_id = get_search_id(search)
        timestamp = create_datetime()
        add_today_search(rank, search_id, timestamp, country_id)
    return today_searches


def store_all_searches():
    """
    Fetches and stores trending, realtime, and today's search data for all countries in the database.

    Returns:
        list: A list of tuples containing the result and body of formatted emails for each country.
    """
    countries = get_countries()
    responses = []
    for country in countries:
        id, _, two_letter_code, camel_case_name = country
        trending_result = store_trending_searches(id, camel_case_name)
        realtime_result = store_realtime_trending_searches(id, two_letter_code)
        today_result = store_today_searches(id, two_letter_code)
        result, body = format_trending_searches_email(trending_result)
        responses.append((result, body))
        result, body = format_realtime_trending_searches_email(realtime_result)
        responses.append((result, body))
        result, body = format_today_searches_email(today_result)
        responses.append((result, body))
    return responses


def store_suggestions(search_id, search):
    response = fetch_suggestions(search)
    if response is None:
        return None
    suggestions = []
    for record in response:
        title = record['title']
        suggestion_type = record['type']
        if title != search:
            add_suggestion(title, search_id)
            suggestions.append(title)
        elif (suggestion_type != search) and (suggestion_type != "Topic"):
            add_suggestion(suggestion_type, search_id)
            suggestions.append(suggestion_type)
    if len(suggestions) == 0:
        add_suggestion("Topic", search_id)
    return suggestions

