def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    count = { }

    for value in samples:
        if value in count:
            count[value]+=1
        else:
            count[value] = 1
    empirical = [ ]
    for value,frequency in count.items():
        empirical.append((value,frequency/len(samples)))
    return empirical