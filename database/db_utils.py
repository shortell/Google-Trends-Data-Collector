from database.postgres_utils import exec_sql_file, exec_commit


def create_schema():
    """
    Creates the schema schema by executing an SQL file.
    """
    try:
        exec_sql_file('queries/schema.sql')
        return True
    except Exception as e:
        print("SCHEMA NOT CREATED")
        print(e)
        return False


def drop_schema():
    """
    Drops existing tables from the google_trends schema if they exist.
    """

    query = """
    DROP TABLE IF EXISTS google_trends.categories CASCADE;
    DROP TABLE IF EXISTS google_trends.countries CASCADE;
    DROP TABLE IF EXISTS google_trends.today_searches CASCADE;
    DROP TABLE IF EXISTS google_trends.realtime_trending_searches CASCADE;
    DROP TABLE IF EXISTS google_trends.trending_searches CASCADE;
    DROP TABLE IF EXISTS google_trends.searches CASCADE;
    DROP TABLE IF EXISTS google_trends.suggestions CASCADE;
    DROP SCHEMA IF EXISTS google_trends CASCADE;
    """
    try:
        exec_commit(query)
    except Exception as e:
        print("COULD NOT DROP SCHEMA")
        print(e)
        return False


def seed_database():
    try:
        exec_sql_file('queries/seed.sql')
    except Exception as _:
        pass