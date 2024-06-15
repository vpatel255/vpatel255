#!/usr/bin/env python3

def join_sets(s1, s2):
    # join_sets will return a set that contains every value from both s1 and s2
    return s1.union(s2)

def match_sets(s1, s2):
    # match_sets will return a set that contains all values found in both s1 and s2
    return s1.intersection(s2)

def diff_sets(s1, s2):
    # diff_sets will return a set that contains all different values which are not shared between the sets
    return s1.symmetric_difference(s2)

if __name__ == '__main__':
    set1 = set(range(1, 10))
    set2 = set(range(5, 15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))


import lab4a
set1 = {1, 2, 3, 4, 5}
set2 = {2, 1, 0, -1, -2}
print(lab4a.join_sets(set1, set2))  # Will output {-2, -1, 0, 1, 2, 3, 4, 5}
print(lab4a.match_sets(set1, set2))  # Will output {1, 2}
print(lab4a.diff_sets(set1, set2))  # Will output {-2, -1, 0, 3, 4, 5}

