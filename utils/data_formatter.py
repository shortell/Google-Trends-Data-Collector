def format_trending_searches_email(trending_searches):
    if trending_searches is None:
        return False, 'TRENDING SEARCHES\nN/A'
    body = "TRENDING SEARCHES\n"
    for rank, search_term in trending_searches.items():
        body += f"{rank}. {search_term}\n"
    return True, body


def format_realtime_trending_searches_email(realtime_trending_searches):
    if realtime_trending_searches is None:
        return False, 'Realtime Trending Searches\nN/A'
    body = "Realtime Trending Searches\n"
    for rank, search_list in realtime_trending_searches.items():
        for search_term in search_list:
            body += f"\t{rank}. {search_term}\n"
    return True, body


def format_today_searches_email(today_searches):
    if today_searches is None:
        return False, 'Today Searches\nN/A'
    body = "Today Searches\n"
    for rank, search_term in today_searches.items():
        body += f"{rank}. {search_term}\n"
    return True, body
