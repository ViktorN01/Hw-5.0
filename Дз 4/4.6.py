from itertools import count, cycle

count1 = count(5)
cycle1 = cycle('damn')
for _ in range(5):
    print("(count1, cycle1) = ({},{})".format(next(count1), next(cycle1)))
