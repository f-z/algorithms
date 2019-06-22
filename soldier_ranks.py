def solution(ranks):
    """
    Getting counts of soldiers in a certain rank n reporting to at least one soldier in rank n + 1 (where n + 1 exists)
    and returning their total sum across all ranks
    """
    counts = {}
    for i in range(len(ranks)):
        if ranks[i] in counts:
            counts[ranks[i]] += 1
        else:
            counts[ranks[i]] = 1

    sum = 0

    for key, value in counts.items():
        if (key + 1) in counts:
            sum += value

    return sum
