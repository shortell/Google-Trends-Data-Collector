def calculate_average_rank(data: list):
    length = len(data)
    if length == 0:
        return -1
    if length == 1:
        return data[0][1]
    all_ranks = []
    for _, rank in data:
        all_ranks.append(rank)

    avg_rank = sum(all_ranks) / len(all_ranks)
    return avg_rank
