from pytrends.request import TrendReq

# Initialize pytrends object
pytrends = TrendReq(hl='en-US', tz=720, timeout=(4, 10))


def build_payload(kw_list, cat=0, timeframe='now 1-d', geo='US', gprop=''):
    """
    Build the payload for Google Trends API request.

    Parameters:
    - kw_list (list): List of keywords to be included in the request.
    - cat (int): Category to narrow down the search (default is 0 for 'All categories').
    - timeframe (str): Time range for the data (default is 'now 1-d' for the past 1 day).
    - geo (str): Geographical location for the search (default is 'US' for the United States).
    - gprop (str): Google property to filter the search results (default is an empty string).

    Returns:
    None
    """
    try:
        pytrends.build_payload(
            kw_list,
            cat=cat,
            timeframe=timeframe,
            geo=geo,
            gprop=gprop
        )
        return True
    except Exception as _:
        return False


def fetch_interest_over_time():
    """
    WORKING REGULARLY
    Retrieve the interest over time data using pytrends library.

    Returns:
    DataFrame: A pandas DataFrame containing the interest over time data.
    """
    try:
        return pytrends.interest_over_time()
    except Exception as _:
        return None


def fetch_multirange_interest_ot():
    """
    ONLY RECEIVES 429 CALL LIMIT REACHED
    Retrieve multi-range interest over time data using pytrends library.

    Returns:
    DataFrame: A pandas DataFrame containing the multi-range interest over time data.
    """
    try:
        return pytrends.multirange_interest_over_time()
    except Exception as _:
        return None


def fetch_interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False):
    """
    ONLY RECEIVES 429 CALL LIMIT REACHED
    Retrieve interest by region data using pytrends library.

    Parameters:
    - resolution (str): Geographic resolution for the region data (default is 'COUNTRY').
    - inc_low_vol (bool): Include low volume regions in the data (default is True).
    - inc_geo_code (bool): Include geographical codes in the data (default is False).

    Returns:
    DataFrame: A pandas DataFrame containing the interest by region data.
    """
    try:
        return pytrends.interest_by_region(resolution=resolution, inc_low_vol=inc_low_vol, inc_geo_code=inc_geo_code)
    except Exception as _:
        return None


def fetch_related_topics():
    """
    ONLY RECEIVES 429 CALL LIMIT REACHED
    Retrieve related topics data using pytrends library.

    Returns:
    pandas.DataFrames
    """
    try:
        return pytrends.related_topics()
    except Exception as _:
        return None


def fetch_related_queries():
    """
    ONLY RECEIVES 429 CALL LIMIT REACHED
    Retrieve related queries data using pytrends library.

    Returns:
    pandas.DataFrames
    """
    try:
        return pytrends.related_queries()
    except Exception as _:
        return None


def fetch_trending_searches(pn='united_states'):
    """
    WORKING REGULARLY
    Retrieve trending searches data using pytrends library.

    Parameters:
    - pn (str): Two-letter country code for the desired region (default is 'united_states').

    Returns:
    pandas.DataFrames
    """
    try:
        return pytrends.trending_searches(pn=pn)
    except Exception as _:
        return None


def fetch_today_searches(pn='US'):
    """
    WORKING REGULARLY
    Retrieve trending searches data using pytrends library.

    Parameters:
    - pn (str): Two-letter country code for the desired region (default is 'united_states').

    Returns:
    pandas.DataFrames
    """
    try:
        return pytrends.today_searches(pn=pn)
    except Exception as _:
        return None


def fetch_realtime_trending_searches(pn='US', cat='all', count=300):
    """
    WORKING REGULARLY
    Retrieve realtime trending searches data using the pytrends library.

    Parameters:
    - pn (str): Two-letter country code for the desired region (default is 'US').
    - cat (str): Category to filter trending searches (default is 'all').
    - count (int): Number of trending searches to retrieve (default is 20).

    Returns:
    pandas.DataFrame: DataFrame containing realtime trending searches data.
    """
    try:
        return pytrends.realtime_trending_searches(pn=pn, cat=cat, count=count)
    except Exception as _:
        return None


def fetch_top_charts(date, hl='en-US', tz=300, geo='GLOBAL'):
    """
    WORKING REGULARLY
    Retrieve top charts data using pytrends library.

    Parameters:
    - date (int): A four-digit year specifying the desired date for the top charts data.
    - hl (str): Language parameter (default is 'en-US').
    - tz (int): Timezone offset in minutes (default is 300).
    - geo (str): Geographical location for the top charts data (default is 'GLOBAL').

    Returns:
    DataFrame: A pandas DataFrame containing the top charts data.
    """
    try:
        return pytrends.top_charts(date, hl=hl, tz=tz, geo=geo)
    except Exception as _:
        return None


def fetch_suggestions(keyword):
    """
    WORKING REGULARLY
    Retrieve keyword suggestions using pytrends library.

    Parameters:
    - keyword (str): The base keyword for which suggestions are requested.

    Returns:
    dict: A dictionary
    """
    try:
        return pytrends.suggestions(keyword)
    except Exception as _:
        return None


def fetch_categories():
    """
    WORKING REGULARLY
    Retrieve Google Trends categories using pytrends library.

    Returns:
    dict: A dictionary containing Google Trends categories and their associated codes.
    """
    try:
        return pytrends.categories()
    except Exception as _:
        return None


# NotImplementedError: This method has been removed for incorrectness. It will be removed completely in v5.
# If you'd like similar functionality, please try implementing it yourself and consider submitting a pull request to add it to pytrends.
def fetch_historical_interest(kw_list, start_date_hour, end_date_hour, cat=0, geo='US', gprop='', sleep=60):
    """
    Retrieve historical interest data using pytrends library.

    Parameters:
    - kw_list (list): List of keywords for which historical interest data is requested.
    - start_date_hour (list): List containing the year, month, day, and hour of the start date and time.
    - end_date_hour (list): List containing the year, month, day, and hour of the end date and time.
    - cat (int): Category to narrow down the search (default is 0 for 'All categories').
    - geo (str): Geographical location for the search (default is 'US' for the United States).
    - gprop (str): Google property to filter the search results (default is an empty string).
    - sleep (int): Time to sleep between API requests in seconds (default is 60).

    Returns:
    DataFrame: A pandas DataFrame containing the historical interest data.
    """
    try:
        return pytrends.fetch_historical_interest(kw_list=kw_list,
                                                  year_start=start_date_hour[0],
                                                  month_start=start_date_hour[1],
                                                  day_start=start_date_hour[2],
                                                  hour_start=start_date_hour[3],
                                                  year_end=end_date_hour[0],
                                                  month_end=end_date_hour[1],
                                                  day_end=end_date_hour[2],
                                                  hour_end=end_date_hour[3],
                                                  cat=cat,
                                                  geo=geo,
                                                  gprop=gprop,
                                                  sleep=sleep)
    except Exception as _:
        return None
