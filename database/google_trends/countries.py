from database.postgres_utils import exec_get_all, exec_commit, exec_get_one
import json


def get_country_data_from_file(country_name):
    """
    Retrieves country data from a JSON file based on the provided country name.

    Parameters:
        country_name (str): The name of the country for which data is to be retrieved.

    Returns:
        dict or None: A dictionary containing the country data if found, otherwise None.

    Notes:
        - This function reads country data from a JSON file located at 'data/all_countries.json'.
        - If the provided country name is found in the JSON data, the corresponding country data is returned.
        - The format of the returned country data is a dictionary.
        - If the country name is not found in the JSON data, None is returned.
    """
    with open('data/all_countries.json', 'r') as file:
        json_data = json.load(file)
        if country_name in json_data:
            return json_data[country_name]
        else:
            return None


def _add_country(name, two_letter_code, camel_case_name):
    """
    Adds a country to the 'google_trends.countries' table in the database.

    Parameters:
        name (str): The name of the country.
        two_letter_code (str): The two-letter country code.
        camel_case_name (str): The camel case name of the country.

    Returns:
        bool: True if the country was successfully added, False otherwise.

    Notes:
        - This function is intended to be used internally.
        - It constructs an SQL query to insert a new country into the 'countries' table.
        - The 'name', 'two_letter_code', and 'camel_case_name' are required for insertion.
        - If the insertion is successful, True is returned.
        - If an exception occurs during execution (e.g., duplicate entry), False is returned.
    """
    query = """
    INSERT INTO google_trends.countries(name, two_letter_code, camel_case_name)
    VALUES (%s, %s, %s);
    """
    try:
        exec_commit(query, (name, two_letter_code, camel_case_name))
        return True
    except Exception as e:
        return False


def add_country_from_file(country='United States'):
    """
    Adds a country to the 'google_trends.countries' table in the database using data from a file.

    Parameters:
        country (str): The name of the country to add. Defaults to 'United States'.

    Returns:
        bool: True if the country was successfully added, False otherwise.

    Notes:
        - This function retrieves country data from a JSON file using the get_country_data_from_file function.
        - If country data is found in the file, the two-letter country code and camel case name are extracted.
        - The country is then added to the 'countries' table in the database using the _add_country function.
        - If the addition is successful, True is returned.
        - If country data is not found or if an exception occurs during insertion, False is returned.
    """
    country_data = get_country_data_from_file(country)
    if country_data is not None:
        two_letter_code = country_data['two_letter_code']
        camel_case_name = country_data['camel_case_name']
        try:
            return _add_country(country, two_letter_code, camel_case_name)
        except Exception as _:
            pass
    return False


def get_countries():
    """
    Retrieves all countries from the 'google_trends.countries' table in the database.

    Returns:
        list of tuples: A list of tuples containing country data.
            Each tuple has the format (id, name, two_letter_code, camel_case_name).

    Notes:
        - This function constructs an SQL query to select all countries from the 'countries' table.
        - It then executes the query using exec_get_all and returns the result.
        - Each tuple in the result contains the country's ID, name, two-letter code, and camel case name.
    """
    query = """
    SELECT * FROM google_trends.countries;
    """
    return exec_get_all(query)


def get_country_by_name(name):
    """
    Retrieves country data from the 'google_trends.countries' table in the database based on the country name.

    Parameters:
        name (str): The name of the country to retrieve.

    Returns:
        tuple or None: A tuple containing country data (id, name, two_letter_code, camel_case_name) if found,
            otherwise None.

    Notes:
        - This function constructs an SQL query to select a country from the 'countries' table based on its name.
        - It then executes the query using exec_get_one with the provided country name.
        - If a country with the given name is found, a tuple containing its data is returned.
        - If no country is found or an error occurs during execution, None is returned.
    """
    query = """
    SELECT * FROM google_trends.countries
    WHERE countries.name = %s;
    """
    return exec_get_one(query, (name,))

def get_country_by_id(country_id):
    query = """
    SELECT * FROM google_trends.countries
    WHERE countries.id = %s;
    """
    return exec_get_one(query, (country_id,))

