from itertools import cycle, count

count1 = count(1)
cycle1 = cycle('try')

for _ in range(8):
    print("(count1, cycle1,) = ({},{})".format(next(count1), next(cycle1)))