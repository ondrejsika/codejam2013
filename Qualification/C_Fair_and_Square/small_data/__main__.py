import math

for r in range(input()):
    r += 1
    c = 0

    l, h = raw_input().split()
    h = int(h)
    l = int(l)
    for i in range(l, h+1):
        si = str(i)
        sq = math.sqrt(i)
        ssq = str(int(sq))
        if si == si[::-1] and int(sq) == sq and ssq == ssq[::-1]:
            c += 1
    print "Case #%s: %s" % (r, c)
