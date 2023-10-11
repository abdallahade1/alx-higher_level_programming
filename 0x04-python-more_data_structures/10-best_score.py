#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sort_scores = sorted(a_dictionary, key=a_dictionary.get)
    best_one = sort_scores[-1]
    return best_one
