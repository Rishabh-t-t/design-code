"""Generates src/components/twin-mini.svg: a small isometric twin of Meridian Tower.
Each energy asset is a <g class="a" data-asset="..."> so CSS can highlight, dim or focus it.
Run: python3 tools/gen-twin-mini.py"""
import math, os

S = 13.0                      # scene units -> px
C, H = math.cos(math.radians(30)) * S, 0.5 * S
pts_all = []

def P(x, y, z=0):
    X, Y = (x - y) * C, (x + y) * H - z * S
    pts_all.append((X, Y))
    return X, Y

def poly(points, cls):
    return '<polygon class="%s" points="%s"/>' % (cls, ' '.join('%.1f,%.1f' % p for p in points))

def box(x, y, z, w, d, h):
    """Three visible faces of an iso box: top, left (+y side), right (+x side)."""
    top = [P(x, y, z + h), P(x + w, y, z + h), P(x + w, y + d, z + h), P(x, y + d, z + h)]
    left = [P(x, y + d, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x, y + d, z + h)]
    right = [P(x + w, y, z), P(x + w, y + d, z), P(x + w, y + d, z + h), P(x + w, y, z + h)]
    return poly(top, 't') + poly(left, 'l') + poly(right, 'r')

def line(points, cls):
    return '<polyline class="%s" points="%s"/>' % (cls, ' '.join('%.1f,%.1f' % P(*p) for p in points))

out = []
# ground plate
out.append(poly([P(0, 0), P(11, 0), P(11, 10), P(0, 10)], 'ground'))
# cables on the ground (drawn first so assets sit on top)
out.append('<g class="cables">')
out.append('<g class="a" data-asset="grid">' + line([(7.9, 2.4), (7.9, 3.4), (6.0, 3.4)], 'cable') + '</g>')
out.append('<g class="a" data-asset="battery">' + line([(7.6, 4.6), (6.0, 4.6)], 'cable') + '</g>')
out.append('<g class="a" data-asset="ev">' + line([(4.2, 7.3), (4.2, 6.0)], 'cable') + '</g>')
out.append('</g>')
# substation / grid connection (back right)
out.append('<g class="a" data-asset="grid">' + box(7.2, 0.8, 0, 1.6, 1.4, 1.3) + '</g>')
# tower with floor lines
tower = box(3, 3, 0, 3, 3, 7)
floors = ''.join(line([(3, 6, z), (6, 6, z), (6, 3, z)], 'floor') for z in range(1, 7))
out.append('<g class="tower">' + tower + floors + '</g>')
# rooftop: solar array and HVAC unit
solar = poly([P(3.3, 3.3, 7.02), P(4.9, 3.3, 7.02), P(4.9, 5.7, 7.02), P(3.3, 5.7, 7.02)], 'panel')
solar += ''.join(line([(3.3, y, 7.03), (4.9, y, 7.03)], 'panel-line') for y in (3.9, 4.5, 5.1))
out.append('<g class="a" data-asset="solar">' + solar + '</g>')
out.append('<g class="a" data-asset="hvac">' + box(5.15, 3.4, 7, 0.65, 0.9, 0.55) + '</g>')
# battery cabinets (right)
out.append('<g class="a" data-asset="battery">' + box(7.6, 4.0, 0, 0.9, 0.55, 0.9) + box(7.6, 4.75, 0, 0.9, 0.55, 0.9) + '</g>')
# EV chargers (front)
ev = ''.join(box(x, 7.4, 0, 0.32, 0.32, 0.85) for x in (3.2, 4.0, 4.8))
ev += ''.join(line([(x - 0.15, 8.0), (x - 0.15, 9.4)], 'bay') for x in (3.0, 3.8, 4.6, 5.4))
out.append('<g class="a" data-asset="ev">' + ev + '</g>')

xs, ys = [p[0] for p in pts_all], [p[1] for p in pts_all]
pad = 6
vb = (min(xs) - pad, min(ys) - pad, max(xs) - min(xs) + 2 * pad, max(ys) - min(ys) + 2 * pad)
svg = ('<svg class="twin-mini" viewBox="%.1f %.1f %.1f %.1f" role="img" aria-label="Simplified 2.5D twin of Meridian Tower '
       'with its solar array, HVAC, battery, EV chargers and grid connection">' % vb) + ''.join(out) + '</svg>\n'
path = os.path.join(os.path.dirname(__file__), '..', 'src', 'components', 'twin-mini.svg')
open(path, 'w').write(svg)
print('wrote', os.path.normpath(path), len(svg), 'bytes, viewBox', ['%.0f' % v for v in vb])
