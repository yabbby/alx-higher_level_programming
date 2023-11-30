#!/usr/bin/python3
def best_score(a_dictionary):
    score = None
    if a_dictionary is None:
        return score

    for k, v in a_dictionary.items():
        if score is None:
            score = k
            continue
        if v > a_dictionary[score]:
            score = k

    return score
