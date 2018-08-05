
def OverlappingBoxes(p1, p2):
    if overlapping(p1[0], p1[2], p2[0], p2[2]) and overlapping(p1[1], p1[3], p2[1], p2[3]):
        return True

def overlapping(a1, a2, b1, b2):

    if greater(abs(a1 - (b1 + b2)),abs((a1 + a2) - b1)) > (a2 + b2):
        return False
    else:
        return True

def greater(x,y):
    if x > y:
        return x
    else:
        return y