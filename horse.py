"""
@author StagnantIce (tria-aa@mail.ru)
@url https://github.com/StagnantIce/knight_tour
"""

import sys, time


if len(sys.argv) < 3:
    print """
    Please, write 2 param: x and y for horse, from 0 to 7
    Example: horse.py 0 7
    """
    exit(0)

x, y = int(sys.argv[1]), int(sys.argv[2])

path = []
path.append((x, y))

nopath = []
steps = []
for i in range(8):
    steps.append([])
    for j in range(8):
        steps[i].append([])
        if (i,j) not in path:
            nopath.append((i,j))
        for (hx, hy) in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, 1), (2, -1), (1, -2), (1, 2)]:
            if i + hx >= 0 and i + hx <=7 and j + hy >= 0 and j + hy <= 7:
                steps[i][j].append((hx, hy))

def nextStep(path, nopath, c):
    x, y = path[-1]
    step = steps[x][y]
    for hx, hy in step:
        el =  (x + hx, y + hy)
        if c > 32 and el in nopath or c <= 32 and el not in path:
            nopath2 = list(nopath)
            nopath2.remove(el)
            yield path + [el], nopath2


t = time.time()

def main(path, nopath, c):
    if c >= 63:
        print "Steps %d" % c
        print path
        print time.time() - t
        #exit(0)
    for path, nopath in nextStep(path, nopath, c):
        main(path, nopath, c + 1)


t = time.time()
main(path, nopath, 1)
