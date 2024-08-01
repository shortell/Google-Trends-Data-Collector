CREATE SCHEMA IF NOT EXISTS google_trends;

CREATE TABLE IF NOT EXISTS google_trends.searches (
    id SERIAL PRIMARY KEY,
    search TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS google_trends.countries (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    two_letter_code TEXT NOT NULL UNIQUE,
    camel_case_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS google_trends.trending_searches(
    id SERIAL PRIMARY KEY,
    rank INTEGER NOT NULL,
    search_id INTEGER NOT NULL REFERENCES google_trends.searches(id),
    timestamp TIMESTAMP NOT NULL,
    country_id INTEGER NOT NULL REFERENCES google_trends.countries(id),
    CONSTRAINT unique_trending_search_timestamp_country UNIQUE (search_id, timestamp, country_id)
);

CREATE TABLE IF NOT EXISTS google_trends.realtime_trending_searches(
    id SERIAL PRIMARY KEY,
    rank INTEGER NOT NULL,
    search_id INTEGER NOT NULL REFERENCES google_trends.searches(id),
    timestamp TIMESTAMP NOT NULL,
    country_id INTEGER NOT NULL REFERENCES google_trends.countries(id),
    CONSTRAINT unique_realtime_trending_search_timestamp_country UNIQUE (search_id, timestamp, country_id)
);

CREATE TABLE IF NOT EXISTS google_trends.today_searches(
    id SERIAL PRIMARY KEY,
    rank INTEGER NOT NULL,
    search_id INTEGER NOT NULL REFERENCES google_trends.searches(id),
    timestamp TIMESTAMP NOT NULL,
    country_id INTEGER NOT NULL REFERENCES google_trends.countries(id),
    CONSTRAINT unique_today_search_timestamp_country UNIQUE (search_id, timestamp, country_id)
);

CREATE TABLE IF NOT EXISTS google_trends.suggestions(
    id SERIAL PRIMARY KEY,
    related_term TEXT NOT NULL,
    search_id INTEGER NOT NULL REFERENCES google_trends.searches(id),
    CONSTRAINT unique_term_search_id UNIQUE (related_term, search_id)
);