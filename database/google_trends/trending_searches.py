from database.postgres_utils import exec_commit, exec_get_all, exec_get_one


def add_trending_search(rank, search_id, timestamp, country_id):
    """
    Adds a trending search entry to the 'google_trends.trending_searches' table in the database.

    Parameters:
        rank (int): The rank of the trending search.
        search_id (int): The ID of the trending search query.
        timestamp (datetime): The timestamp of when the trending search was recorded.
        country_id (int): The ID of the country for which the trending search is recorded.

    Returns:
        bool: True if the trending search entry was successfully added, False otherwise.

    Notes:
        - This function constructs an SQL query to insert a new trending search entry into the 'trending_searches' table.
        - The 'rank', 'search_id', 'timestamp', and 'country_id' are required for insertion.
        - If the insertion is successful, True is returned.
        - If an exception occurs during execution (e.g., data format error), False is returned.
    """
    query = """
    INSERT INTO 
        google_trends.trending_searches (rank, search_id, timestamp, country_id)
    VALUES (%s, %s, %s, %s);
    """
    try:
        exec_commit(query, (rank, search_id, timestamp, country_id))
        return True
    except Exception as _:
        return False


def get_trending_data(country_id, start, end,  rank_min, rank_max, limit, offset):
    query = """
    SELECT 
        google_trends.trending_searches.search_id,
        google_trends.trending_searches.rank,
        google_trends.searches.search,
        google_trends.trending_searches.timestamp
    FROM 
        google_trends.trending_searches
    JOIN 
        google_trends.searches ON google_trends.trending_searches.search_id = google_trends.searches.id
    WHERE 
        google_trends.trending_searches.country_id = %s
    AND 
        google_trends.trending_searches.timestamp BETWEEN %s AND %s
    AND
        google_trends.trending_searches.rank BETWEEN %s and %s
    ORDER BY 
        trending_searches.timestamp ASC, trending_searches.rank ASC
    LIMIT %s OFFSET %s;
    """
    return exec_get_all(query, (country_id, start, end, rank_min, rank_max, limit, offset))


def get_trending_count_and_unique_count(country_id, start, end, rank_min, rank_max, limit):
    query = """
    SELECT 
        COUNT(google_trends.trending_searches.search_id),
        COUNT(DISTINCT google_trends.trending_searches.search_id)
    FROM 
        google_trends.trending_searches
    WHERE 
        google_trends.trending_searches.country_id = %s
    AND 
        google_trends.trending_searches.timestamp BETWEEN %s AND %s
    AND
        google_trends.trending_searches.rank BETWEEN %s and %s
    LIMIT %s;
    """
    return exec_get_one(query, (country_id, start, end, rank_min, rank_max, limit))


def get_trending_search_rank_overtime(country_id, search_id, start, end):
    query = """
    SELECT 
        timestamp,
        rank
    FROM 
        google_trends.trending_searches
    WHERE 
        google_trends.trending_searches.timestamp BETWEEN %s AND %s
    AND
        google_trends.trending_searches.search_id = %s
    AND 
        google_trends.trending_searches.country_id = %s
    ORDER BY 
        trending_searches.timestamp ASC;
    """
    return exec_get_all(query, (start, end, search_id, country_id))
