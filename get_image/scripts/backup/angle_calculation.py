import math


def slope(x1, y1, x2, y2): # Line slope given two points:
    return (y2-y1)/(x2-x1)


def angle(s1, s2):
    return math.degrees(math.atan((s2-s1)/(1+(s2*s1))))


slope1 = slope(100, 10, 10, 20)
slope2 = slope(50, 30, 20, 30)

ang = angle(slope1, slope2)
print('Angle in degrees = ', ang)