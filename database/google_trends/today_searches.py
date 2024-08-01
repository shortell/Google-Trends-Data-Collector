from database.postgres_utils import exec_commit, exec_get_all, exec_get_one


def add_today_search(rank, search_id, timestamp, country_id):
    """
    Adds a search entry to the 'google_trends.today_searches' table in the database.

    Parameters:
        rank (int): The rank of the search.
        search_id (int): The ID of the search query.
        timestamp (datetime): The timestamp of when the search was recorded.
        country_id (int): The ID of the country for which the search is recorded.

    Returns:
        bool: True if the search entry was successfully added, False otherwise.

    Notes:
        - This function constructs an SQL query to insert a new search entry into the 'today_searches' table.
        - The 'rank', 'search_id', 'timestamp', and 'country_id' are required for insertion.
        - If the insertion is successful, True is returned.
        - If an exception occurs during execution (e.g., data format error), False is returned.
    """
    query = """
    INSERT INTO 
        google_trends.today_searches (rank, search_id, timestamp, country_id)
    VALUES (%s, %s, %s, %s);
    """
    try:
        exec_commit(query, (rank, search_id, timestamp, country_id))
        return True
    except Exception as _:
        return False


def get_today_data(country_id, start, end,  rank_min, rank_max, limit, offset):
    query = """
    SELECT 
        google_trends.today_searches.search_id,
        google_trends.today_searches.rank,
        google_trends.searches.search,
        google_trends.today_searches.timestamp
    FROM 
        google_trends.today_searches
    JOIN 
        google_trends.searches ON google_trends.today_searches.search_id = google_trends.searches.id
    WHERE 
        google_trends.today_searches.country_id = %s
    AND 
        google_trends.today_searches.timestamp BETWEEN %s AND %s
    AND
        google_trends.today_searches.rank BETWEEN %s and %s
    ORDER BY 
        today_searches.timestamp ASC, today_searches.rank ASC
    LIMIT %s OFFSET %s;
    """
    return exec_get_all(query, (country_id, start, end, rank_min, rank_max, limit, offset))


def get_today_count_and_unique_count(country_id, start, end, rank_min, rank_max, limit):
    query = """
    SELECT 
        COUNT(google_trends.today_searches.search_id),
        COUNT(DISTINCT google_trends.today_searches.search_id)
    FROM 
        google_trends.today_searches
    WHERE 
        google_trends.today_searches.country_id = %s
    AND 
        google_trends.today_searches.timestamp BETWEEN %s AND %s
    AND
        google_trends.today_searches.rank BETWEEN %s and %s
    LIMIT %s;
    """
    return exec_get_one(query, (country_id, start, end, rank_min, rank_max, limit))


def get_today_search_rank_overtime(country_id, search_id, start, end):
    query = """
    SELECT 
        timestamp,
        rank
    FROM 
        google_trends.today_searches
    WHERE 
        google_trends.today_searches.timestamp BETWEEN %s AND %s
    AND
        google_trends.today_searches.search_id = %s
    AND 
        google_trends.today_searches.country_id = %s
    ORDER BY 
        today_searches.timestamp ASC;
    """
    return exec_get_all(query, (start, end, search_id, country_id))
