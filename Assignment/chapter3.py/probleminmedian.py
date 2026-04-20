'''
averaging the two middle number value is correct. it's not a bug. That how median rule works. The problem is that the result can feel less natual or representative when two middle numbers are far apart.
'''

import statistics
value = (9,11,22,34,17,22,34,22,40,34)
print(statistics.mean(value))

print(statistics.median(value))

print(statistics.mode(value))

