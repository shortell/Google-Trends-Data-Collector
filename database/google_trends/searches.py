from database.postgres_utils import exec_commit, exec_get_all, exec_get_one

def add_search(search):
    """
    Adds a search query to the 'google_trends.searches' table in the database.

    Parameters:
        search (str): The search query to add.

    Returns:
        bool: True if the search query was successfully added, False otherwise.

    Notes:
        - This function constructs an SQL query to insert a new search query into the 'searches' table.
        - The 'search' parameter is the search query to be added.
        - If the insertion is successful, True is returned.
        - If an exception occurs during execution (e.g., duplicate entry), False is returned.
    """
    query = """
    INSERT INTO google_trends.searches (search)
    VALUES (%s);
    """
    try:
        exec_commit(query, (search,))
        return True
    except Exception as _:
        return False


def get_search_id(search):
    """
    Retrieves the ID of a search query from the 'google_trends.searches' table in the database.

    Parameters:
        search (str): The search query for which to retrieve the ID.

    Returns:
        int or None: The ID of the search query if found, otherwise None.

    Notes:
        - This function constructs an SQL query to select the ID of a search query from the 'searches' table.
        - The 'search' parameter is the search query for which to retrieve the ID.
        - If the search query is found, its corresponding ID is returned.
        - If the search query is not found, None is returned.
    """
    query = """
    SELECT id FROM google_trends.searches
    WHERE search = %s;
    """
    result = exec_get_one(query, (search,))
    if result is not None:
        return result[0]
    return result


def get_search_by_id(search_id):
    """
    Retrieves a search query by its ID from the 'google_trends.searches' table in the database.

    Parameters:
        search_id (int): The ID of the search query to retrieve.

    Returns:
        tuple or None: A tuple containing the search query data (id, search) if found, otherwise None.

    Notes:
        - This function constructs an SQL query to select a search query by its ID from the 'searches' table.
        - The 'search_id' parameter is the ID of the search query to retrieve.
        - If the search query with the given ID is found, a tuple containing its data (id, search) is returned.
        - If no search query is found with the given ID, None is returned.
    """
    query = """
    SELECT * FROM google_trends.searches
    WHERE id = %s;
    """
    return exec_get_one(query, (search_id,))


def get_all_searches(limit=50, offset=0):
    """
    Retrieves all search queries from the 'google_trends.searches' table in the database.

    Parameters:
        limit (int): The maximum number of results to retrieve. Defaults to 50.
        offset (int): The number of results to skip before starting to return rows. Defaults to 0.

    Returns:
        list of tuples: A list of tuples containing all search query data.
            Each tuple has the format (id, search).

    Notes:
        - This function constructs an SQL query to select all search queries from the 'searches' table.
        - The 'limit' parameter controls the maximum number of results to retrieve.
        - The 'offset' parameter specifies how many results to skip before starting to return rows.
        - Each tuple in the result contains the ID and search query of a search entry.
    """
    query = """
    SELECT * FROM google_trends.searches
    LIMIT %s OFFSET %s;
    """
    return exec_get_all(query, (limit, offset))
