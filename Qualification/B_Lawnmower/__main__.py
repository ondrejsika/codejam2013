from list2d import List2d

def is_lower(row, n):
    for d in row:
        if d > n:
            return False
    return True

def can_be_cuted(original):
    original = List2d(original)
    tmp = List2d(len(original.cols()), len(original.rows()), 100)
    for n in [3, 2, 1]:
        for row_p in range(len(tmp.rows())):
            if is_lower(original.row(row_p), n):
                for j in range(len(tmp.cols())):
                    tmp.set(row_p, j, n)
        for col_p in range(len(tmp.cols())):
            if is_lower(original.col(col_p), n):
                for j in range(len(tmp.rows())):
                    tmp.set(j, col_p, n)

    if tmp.data == original.data:
        return "YES"
    return "NO"

def get_garden():
    y, x = raw_input().split()
    x = int(x)
    y = int(y)
    return [raw_input().split() for row in range(y)], x, y

def int_garden(str_garden, mx, my):
    garden = []
    for x in range(len(str_garden)):
        row = []
        for y in range(len(str_garden[x])):
            row.append(int(str_garden[x][y]))
        garden.append(row)
    return garden


if __name__ == "__main__":
    for i in range(input()):
        i += 1
        garden, x, y = get_garden()
        garden = int_garden(garden, x, y)
        print "Case #%s: %s" % (i, can_be_cuted(garden))