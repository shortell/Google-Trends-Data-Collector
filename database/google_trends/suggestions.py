from database.postgres_utils import exec_commit, exec_get_all

def add_suggestion(related_term, search_id):
    """
    Adds a suggestion to the 'google_trends.suggestions' table in the database.

    Parameters:
        related_term (str): The related term or suggestion to add.
        search_id (int): The ID of the search query associated with the suggestion.

    Returns:
        bool: True if the suggestion was successfully added, False otherwise.

    Notes:
        - This function constructs an SQL query to insert a new suggestion into the 'suggestions' table.
        - The 'related_term' parameter is the suggestion or related term to be added.
        - The 'search_id' parameter is the ID of the search query associated with the suggestion.
        - If the insertion is successful, True is returned.
        - If an exception occurs during execution (e.g., data format error), False is returned.
    """
    query = """
    INSERT INTO google_trends.suggestions (related_term, search_id)
    VALUES (%s, %s);
    """
    try:
        exec_commit(query, (related_term, search_id))
        return True
    except Exception as _:
        return False


def get_suggestions_by_search_id(search_id):
    """
    Retrieves suggestions related to a search query by its ID from the 'google_trends.suggestions' table in the database.

    Parameters:
        search_id (int): The ID of the search query to retrieve related suggestions for.

    Returns:
        list of tuples: A list of tuples containing suggestions related to the given search ID.
            Each tuple has the format (related_term,).

    Notes:
        - This function constructs an SQL query to select suggestions related to a search query by its ID
          from the 'suggestions' table.
        - The 'search_id' parameter is the ID of the search query to retrieve related suggestions for.
        - Each tuple in the result contains a related term or suggestion.
    """
    query = """
    SELECT related_term FROM google_trends.suggestions
    WHERE google_trends.suggestions.search_id = %s;
    """
    return exec_get_all(query, (search_id,))


def get_all_suggestions(limit=500):
    query = """
    SELECT * FROM google_trends.suggestions
    LIMIT %s;
    """
    return exec_get_all(query, (limit,))



