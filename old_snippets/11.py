# TODO: NOT DONE. TROUBLE :/ :/ :/


import numpy

def get_adjacent_neighbors(x, y, a):
    match_val = a[x][y]
    if neighbors:
        neighbors.pop(0)
    done.append((x,y))

    """ N for some reason is the y co-ordinate and M is the x co-ordinate"""

    c1 = x - 1  # Left
    c2 = x + 1  # Right
    c3 = y - 1  # Up
    c4 = y + 1  # Down

    """
    * N & M (limes 25 and 35) were initially swapped, but that didn't work so I swapped them around and it 
    started working :/. Clearly I still don't fully get the matrix indicing.
    
    * Also for some reason the code doesn't work online and I'm sick of this problem. It breaks on line 48.
    It complains saying "IndexError: too many indices for array". Python 3 in both places. No clue why.
    
    * Numpy isn't a thing in the IDE either so I need to rewrite it without numpy.
    
    * Tried some more and it's still failing so really, I have NOT solved this :/
    
    * tl;dr All said and done, I am sick of this problem, feel I understood recursion well enough to move on. 
    If I have time I will come back to this later
    """

    if c1 >= 0 and a[c1][y] == match_val:
        neighbors.append((c1, y))
    else:
        pass

    if c2 < M and a[c2][y] == match_val:
        neighbors.append((c2, y))
    else:
        pass

    if c3 >= 0 and a[x][c3] == match_val:
        neighbors.append((x, c3))
    else:
        pass

    if c4 < N and a[x][c4] == match_val:
        neighbors.append((x, c4))
    else:
        pass

    for point in neighbors:
        if point not in done:
            get_adjacent_neighbors(point[0], point[1], a)
        else:
            continue

    for point in done:
        t1, t2 = point
        a[t1][t2] = K

    return done

T = int(input())
for t in range(0, T):
    neighbors = []
    done = []
    N, M = [int(x) for x in input().split(' ')]
    values = input().split(' ')
    values = [values[i:i+N] for i in range(0, len(values), N)]
    x, y, K = [int(x) for x in input().split(' ')]
    a = numpy.array(values)
    get_adjacent_neighbors(x, y, a)

    s1 = ''
    t3 = a.flatten()
    for c1 in t3:
        s1 += str(c1)
    print(' '.join(s1))