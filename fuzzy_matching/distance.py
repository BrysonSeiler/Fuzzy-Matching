from math import floor
import Levenshtein_search

class Jaro:

    def __init__(self, string_1, string_2):
        self.distance = self.measure(string_1, string_2)

    def measure(self, string_1, string_2):

        m = 0
        t = 0

        match_bound = floor(max(len(string_1), len(string_2))/2) - 1

        for i, c in enumerate(string_1):
            if c in list(string_2):
                if abs(i - list(string_2).index(c)) < match_bound:
                    if i != list(string_2).index(c):
                        t += 1
                    m += 1

        if m == 0:
            return 1
        else:
            return 1 - (1/3) * ((m/len(string_1)) + (m/len(string_2)) + ((m-t)/m))


class Levenshtein:

