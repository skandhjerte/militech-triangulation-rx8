import math

class TriangulationRX8:
    def __call__(self, loc_a, loc_b, r1, r2):
        x0, y0 = loc_a.as_point()
        x1, y1 = loc_b.as_point()

        dx = x1 - x0
        dy = y1 - y0
        d = math.hypot(dx, dy)

        if d > r1 + r2:
            print("[MILITECH RX8 DIAGNOSTIC]: NO INTERSECTION: TARGET OUT OF RANGE.\n")
            return []
        if d < abs(r1 - r2):
            print("[MILITECH RX8 DIAGNOSTIC]: NO INTERSECTION: ONE ZONE INSIDE THE OTHER.\n")
            return []
        if d == 0 and r1 == r2:
            print("[MILITECH RX8 DIAGNOSTIC]: INFINITE INTERSECTIONS: ZONES IDENTICAL.\n")
            return []

        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = math.sqrt(max(0, r1**2 - a**2))

        xm = x0 + a * dx / d
        ym = y0 + a * dy / d

        rx = -dy * (h / d)
        ry = dx * (h / d)

        p1 = (xm + rx, ym + ry)
        p2 = (xm - rx, ym - ry)

        return [p1] if h == 0 else [p1, p2]
        
    
class RX8Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_point(self):
        return (self.x, self.y)