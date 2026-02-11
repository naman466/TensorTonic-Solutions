def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    n = len(rater1)

    agree = 0
    freq1 = {}
    freq2 = {}

    for a, b in zip(rater1, rater2):
        if a == b:
            agree += 1
        freq1[a] = freq1.get(a, 0) + 1
        freq2[b] = freq2.get(b, 0) + 1

    p_o = agree / n

    # chance agreement 
    p_e = 0.0
    labels = set(freq1) | set(freq2)
    for k in labels:
        p_e += (freq1.get(k, 0) / n) * (freq2.get(k, 0) / n)

    if p_e == 1.0:  # degenerate case
        return 1.0

    return (p_o - p_e) / (1 - p_e)






