"""Generate the ConnectX building in isometric 2.5D, in four finishes, from one geometry.
Usage: python3 twin.py <outdir>
"""
import math, random, sys, os

C, S, K = math.cos(math.radians(30)), 0.5, 9.0
def P(x, y, z):
    return ((x - y) * C * K, (x + y) * S * K - z * K)

items = []  # (kind, pts3d) | ('line', kind, a, b) | ('tree', x, y, r, h) | ('ell', kind, x, y, z, r)

def poly(kind, *pts): items.append(('poly', kind, pts))
def line(kind, a, b): items.append(('line', kind, a, b))
def top(kind, x0, y0, x1, y1, z): poly(kind, (x0, y0, z), (x1, y0, z), (x1, y1, z), (x0, y1, z))
def fy(kind, x0, x1, y, z0, z1): poly(kind, (x0, y, z0), (x1, y, z0), (x1, y, z1), (x0, y, z1))
def fx(kind, x, y0, y1, z0, z1): poly(kind, (x, y0, z0), (x, y1, z0), (x, y1, z1), (x, y0, z1))
def box(pre, x0, y0, z0, x1, y1, z1):
    fy(pre + '-y', x0, x1, y1, z0, z1); fx(pre + '-x', x1, y0, y1, z0, z1); top(pre + '-top', x0, y0, x1, y1, z1)

# ---------------- site ----------------
SX, SY = 66, 62
fy('base-y', 0, SX, SY, -1.6, 0); fx('base-x', SX, 0, SY, -1.6, 0)
top('ground', 0, 0, SX, SY, 0)
top('grass', 1.5, 1.5, 15, 30, 0.02)
top('grass', 41, 31, 64.5, 60.5, 0.02)
top('paving', 15, 8, 41, 41, 0.02)
top('asphalt', 1.5, 33, 17, 60.5, 0.02)
for i in range(6):
    y = 35.5 + i * 4
    line('bay', (3.5, y, 0.03), (13.5, y, 0.03))
top('path', 41, 41, 64.5, 43, 0.03)
top('path', 50, 43, 52, 60.5, 0.03)
top('paving', 40, 4, 64.5, 29, 0.025)   # battery yard pad
# shadow (tower), drawn by renderer as 'shadow'
TX0, TY0, TX1, TY1 = 20, 14, 36, 30
G, FH, NF = 5.0, 3.6, 8
TOP = G + FH * NF
items.append(('shadow',))

# trees behind the tower
TREES_BACK = [(8, 6, 2.0, 5.5), (12, 13, 1.7, 4.8), (5, 20, 2.2, 6), (10, 26, 1.8, 5), (24, 6, 1.9, 5.2), (31, 4, 1.6, 4.6)]
for t in TREES_BACK: items.append(('tree',) + t)

# ---------------- tower ----------------
# ground floor: recessed glass lobby with columns
fy('glass-y', TX0 + .6, TX1 - .6, TY1 - .6, 0, G - .4)
fx('glass-x', TX1 - .6, TY0 + .6, TY1 - .6, 0, G - .4)
for i in range(7):
    x = TX0 + .6 + i * (TX1 - TX0 - 1.2) / 6
    line('mullion', (x, TY1 - .6, 0), (x, TY1 - .6, G - .4))
for i in range(7):
    y = TY0 + .6 + i * (TY1 - TY0 - 1.2) / 6
    line('mullion', (TX1 - .6, y, 0), (TX1 - .6, y, G - .4))
box('wall', TX1 - 1, TY1 - 1, 0, TX1, TY1, G)   # corner column
box('wall', TX0, TY1 - 1, 0, TX0 + 1, TY1, G)
box('wall', TX1 - 1, TY0, 0, TX1, TY0 + 1, G)
# entrance canopy
box('slab', 24, TY1, G - .9, 32, TY1 + 3.6, G - .5)
for x in (24.4, 31.6):
    box('metal', x - .12, TY1 + 3.2, 0, x + .12, TY1 + 3.44, G - .9)

# upper floors
for f in range(NF):
    z0 = G + f * FH; z1 = z0 + FH
    # +x face (east): punched window band with spandrels
    fx('wall-x', TX1, TY0, TY1, z0, z1)
    fx('glass-x' if f != 5 else 'alert-x', TX1, TY0 + .9, TY1 - .9, z0 + 1.05, z1 - .75)
    n = 9
    for i in range(1, n):
        y = TY0 + .9 + i * (TY1 - TY0 - 1.8) / n
        line('mullion', (TX1, y, z0 + 1.05), (TX1, y, z1 - .75))
    line('sill', (TX1, TY0 + .9, z0 + 1.05), (TX1, TY1 - .9, z0 + 1.05))
    # +y face (south): full-height glazing behind balconies
    fy('wall-y', TX0, TX1, TY1, z0, z1)
    fy('glass-y' if f != 5 else 'alert-y', TX0 + .9, TX1 - .9, TY1, z0 + .55, z1 - .6)
    for i in range(1, 8):
        x = TX0 + .9 + i * (TX1 - TX0 - 1.8) / 8
        line('mullion', (x, TY1, z0 + .55), (x, TY1, z1 - .6))
for f in range(NF):
    z0 = G + f * FH
    # balcony slab and glass rail on the south face
    box('slab', TX0 + .5, TY1, z0 - .05, TX1 - .5, TY1 + 1.7, z0 + .25)
    fy('rail', TX0 + .5, TX1 - .5, TY1 + 1.7, z0 + .25, z0 + 1.25)
    line('railtop', (TX0 + .5, TY1 + 1.7, z0 + 1.25), (TX1 - .5, TY1 + 1.7, z0 + 1.25))
    for i in range(0, 7):
        x = TX0 + .5 + i * (TX1 - TX0 - 1) / 6
        line('railpost', (x, TY1 + 1.7, z0 + .25), (x, TY1 + 1.7, z0 + 1.25))
# corner fins on the east face
for y in (TY0, TY1 - .25):
    box('wall', TX1 - .1, y, G, TX1 + .35, y + .25, TOP)

# roof: parapet + inner deck
box('wall', TX0, TY0, TOP, TX1, TY1, TOP + 1.1)
top('roof', TX0 + .6, TY0 + .6, TX1 - .6, TY1 - .6, TOP + 1.1)
# solar rows (tilted)
for r in range(4):
    y = TY0 + 1.6 + r * 2.6
    for c in range(5):
        x = TX0 + 1.6 + c * 2.1
        poly('solar', (x, y, TOP + 1.5), (x + 1.9, y, TOP + 1.5), (x + 1.9, y + 1.8, TOP + 2.3), (x, y + 1.8, TOP + 2.3))
        line('solargrid', (x + .95, y, TOP + 1.5), (x + .95, y + 1.8, TOP + 2.3))
        line('solargrid', (x, y + .9, TOP + 1.9), (x + 1.9, y + .9, TOP + 1.9))
# stair core and HVAC units
box('wall', 30.5, 25.2, TOP + 1.1, 34.6, 28.8, TOP + 4.2)
fy('door', 31.6, 33, 28.8, TOP + 1.1, TOP + 3.3)
box('metal', 22, 25.4, TOP + 1.1, 25, 28.4, TOP + 2.9)
box('metal', 26, 25.4, TOP + 1.1, 29, 28.4, TOP + 2.9)
items.append(('ell', 'fan', 23.5, 26.9, TOP + 2.92, 1.15))
items.append(('ell', 'fan', 27.5, 26.9, TOP + 2.92, 1.15))

# ---------------- battery yard ----------------
for i, y in enumerate((7, 11.5, 16)):
    box('container', 43, y, 0, 52, y + 3, 2.8)
    for k in range(1, 6):
        x = 43 + k * 1.5
        line('rib', (x, y + 3, .2), (x, y + 3, 2.6))
    fy('vent', 50, 51.4, y + 3, 1.4, 2.4)
box('metal', 55, 8, 0, 59.5, 13, 3.2)        # transformer
for k in range(1, 6):
    line('rib', (59.5, 8 + k * .83, .3), (59.5, 8 + k * .83, 3))
box('metal', 55, 17, 0, 60, 22.5, 2.4)       # generator
fy('vent', 56, 59, 22.5, .8, 1.8)
# fence
for x in range(41, 65, 3):
    line('fence', (x, 28.5, 0), (x, 28.5, 1.8))
for y in range(4, 29, 3):
    line('fence', (64.2, y, 0), (64.2, y, 1.8))
line('fence', (41, 28.5, 1.8), (64.2, 28.5, 1.8)); line('fence', (64.2, 4, 1.8), (64.2, 28.5, 1.8))

# trees in the middle depth
for t in [(44, 36, 1.8, 5.2), (58, 34, 2.1, 6)]: items.append(('tree',) + t)

# ---------------- carport + EV ----------------
for i, y in enumerate((35, 39, 43, 47, 51, 55)):
    if i in (1, 4): continue
    box('car', 5.2, y + .6, .3, 9.4, y + 3.2, 1.3)
    box('carcab', 6.2, y + .9, 1.3, 8.6, y + 2.9, 2.0)
for y in (36.5, 44.5, 52.5):
    box('charger', 2.4, y, 0, 3.1, y + .6, 1.8)
    top('led', 2.4, y, 3.1, y + .6, 1.81)
for x in (3.6, 14.4):
    for y in (35, 45, 55.5):
        box('metal', x - .15, y - .15, 0, x + .15, y + .15, 3.4)
poly('solar', (3, 34.4, 3.4), (15, 34.4, 3.4), (15, 56.6, 4.1), (3, 56.6, 4.1))
for k in range(1, 6):
    x = 3 + k * 2
    line('solargrid', (x, 34.4, 3.4), (x, 56.6, 4.1))
for k in range(1, 11):
    y = 34.4 + k * 2.02; z = 3.4 + .7 * k / 11
    line('solargrid', (3, y, z), (15, y, z))
fy('slab-y', 3, 15, 56.6, 3.9, 4.1)

# front trees
for t in [(22, 46, 2.2, 6.2), (30, 50, 1.9, 5.4), (36, 45, 2.0, 5.6), (47, 50, 2.4, 6.6), (56, 54, 2.0, 5.6), (24, 57, 1.7, 4.8), (61, 46, 1.6, 4.4), (40, 57, 1.8, 5.0)]:
    items.append(('tree',) + t)
# benches / lamp posts on the plaza
for (x, y) in ((18, 38), (38, 38), (38, 12)):
    line('lamp', (x, y, 0), (x, y, 4.2)); items.append(('ell', 'lampglow', x, y, 4.25, .35))

# ---------------- rendering ----------------
def pts2(pts, j=0.0, rnd=None):
    out = []
    for p in pts:
        sx, sy = P(*p)
        if j: sx += rnd.uniform(-j, j); sy += rnd.uniform(-j, j)
        out.append(f'{sx:.1f},{sy:.1f}')
    return ' '.join(out)

def iso_ellipse(x, y, z, r, n=20):
    return [(x + r * math.cos(2 * math.pi * i / n), y + r * math.sin(2 * math.pi * i / n), z) for i in range(n)]

FLAT = {
    'base-y': '#E4E6EA', 'base-x': '#D3D6DC', 'ground': '#F3F4F6', 'grass': '#E4ECDD', 'paving': '#ECEDF0', 'asphalt': '#E1E3E8', 'path': '#F8F8F9',
    'wall-y': '#F4F5F7', 'wall-x': '#E2E5EA', 'wall-top': '#FFFFFF', 'glass-y': '#BCD2F6', 'glass-x': '#94B2EA', 'alert-y': '#F2A58C', 'alert-x': '#E8805F',
    'slab-y': '#F7F7F8', 'slab-x': '#E6E8EC', 'slab-top': '#FFFFFF', 'rail': '#CFE0FA', 'roof': '#EEF0F3', 'solar': '#8EA8EC', 'door': '#9FB4D8',
    'metal-y': '#E6E8EC', 'metal-x': '#CDD1D8', 'metal-top': '#F7F8F9', 'container-y': '#EEF0F3', 'container-x': '#D7DAE0', 'container-top': '#FAFAFB',
    'vent': '#C5CAD3', 'car-y': '#D9DCE2', 'car-x': '#C6CAD2', 'car-top': '#EEF0F3', 'carcab-y': '#9DB2D6', 'carcab-x': '#869CC6', 'carcab-top': '#E6EAF0',
    'charger-y': '#FFFFFF', 'charger-x': '#E1E4EA', 'charger-top': '#FFFFFF', 'led': '#3E8E63', 'fan': '#C9CED6', 'lampglow': '#FFFFFF',
}
LINES = {'mullion': ('#FFFFFF', .7, .75), 'sill': ('#FFFFFF', .8, .6), 'bay': ('#FFFFFF', 1.4, 1), 'railtop': ('#9FB6DE', .8, 1), 'railpost': ('#BCCBE6', .5, .8),
         'solargrid': ('#C7D5FA', .5, .9), 'rib': ('#C7CCD5', .6, 1), 'fence': ('#B9BEC8', .7, 1), 'lamp': ('#9AA0AB', .9, 1)}

def render(mode, alert=False):
    rnd = random.Random(7)
    out = []; defs = []
    xs, ys = [], []
    for it in items:
        if it[0] == 'poly':
            for p in it[2]: x, y = P(*p); xs.append(x); ys.append(y)
    for it in items:
        if it[0] == 'tree':
            x, y = P(it[1], it[2], it[4] + it[3]); ys.append(y - it[3] * K)
    pad = 24
    minx, maxx, miny, maxy = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad
    W, H = maxx - minx, maxy - miny

    real = mode == 'real'; sketch = mode == 'sketch'
    if real:
        defs.append('''
<linearGradient id="gY" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EDEFF3"/></linearGradient>
<linearGradient id="gX" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E4E8EF"/><stop offset="1" stop-color="#CDD3DD"/></linearGradient>
<linearGradient id="glY" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E8F1FF"/><stop offset=".35" stop-color="#A8C4F3"/><stop offset=".55" stop-color="#D6E5FD"/><stop offset="1" stop-color="#7F9FE0"/></linearGradient>
<linearGradient id="glX" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9DB8EC"/><stop offset=".45" stop-color="#6F92DA"/><stop offset=".62" stop-color="#B6CCF4"/><stop offset="1" stop-color="#5E80CC"/></linearGradient>
<linearGradient id="alY" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFD4C2"/><stop offset="1" stop-color="#F08A65"/></linearGradient>
<linearGradient id="alX" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F49B7A"/><stop offset="1" stop-color="#D9643F"/></linearGradient>
<linearGradient id="sol" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B4C6F4"/><stop offset=".5" stop-color="#7B97E4"/><stop offset="1" stop-color="#9AB1EE"/></linearGradient>
<linearGradient id="grd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FAFAFB"/><stop offset="1" stop-color="#ECEEF1"/></linearGradient>
<linearGradient id="grass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E8F0E0"/><stop offset="1" stop-color="#D6E3CC"/></linearGradient>
<radialGradient id="tree" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#C3D9B1"/><stop offset=".6" stop-color="#8FB47A"/><stop offset="1" stop-color="#6E9660"/></radialGradient>
<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FF7A50" stop-opacity=".55"/><stop offset="1" stop-color="#FF7A50" stop-opacity="0"/></radialGradient>
<filter id="blur" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="blur2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2"/></filter>''')
    REALFILL = {'wall-y': 'url(#gY)', 'wall-x': 'url(#gX)', 'glass-y': 'url(#glY)', 'glass-x': 'url(#glX)', 'alert-y': 'url(#alY)', 'alert-x': 'url(#alX)',
                'solar': 'url(#sol)', 'ground': 'url(#grd)', 'grass': 'url(#grass)', 'slab-y': 'url(#gY)', 'carcab-y': 'url(#glY)', 'carcab-x': 'url(#glX)'}

    for it in items:
        t = it[0]
        if t == 'poly':
            kind, pts = it[1], it[2]
            if not alert and kind.startswith('alert'):
                kind = kind.replace('alert', 'glass')
            if sketch:
                fill = '#FBFAF6' if not kind.startswith(('glass', 'alert', 'rail')) else '#F3F4F7'
                if kind in ('grass',): fill = '#F4F6EF'
                if kind == 'solar': fill = '#E9ECF4'
                p = pts2(pts, .7, rnd)
                op = ' fill-opacity=".5"' if kind == 'rail' else ''
                out.append(f'<polygon points="{p}" fill="{fill}"{op} stroke="#3B3B39" stroke-width=".9" stroke-linejoin="round"/>')
                if kind.endswith('-x') and kind.startswith(('wall', 'metal', 'container')):
                    # hatch the shaded face
                    a, b, c, d = pts
                    for k in range(1, 7):
                        u = k / 7
                        p1 = tuple(a[i] + (b[i] - a[i]) * u for i in range(3)); p2 = tuple(d[i] + (c[i] - d[i]) * u for i in range(3))
                        out.append(f'<polyline points="{pts2([p1, p2], .5, rnd)}" fill="none" stroke="#3B3B39" stroke-width=".35" opacity=".45"/>')
                continue
            fill = (REALFILL.get(kind) if real else None) or FLAT.get(kind, '#FF00FF')
            extra = ''
            if kind == 'rail': extra = ' fill-opacity=".45"'
            stroke = ' stroke="#C3C8D1" stroke-width=".45" stroke-linejoin="round"' if not real else ' stroke="#B9C0CC" stroke-width=".3" stroke-linejoin="round"'
            if kind in ('ground', 'grass', 'paving', 'asphalt', 'path'): stroke = ''
            out.append(f'<polygon points="{pts2(pts)}" fill="{fill}"{extra}{stroke}/>')
        elif t == 'line':
            kind, a, b = it[1], it[2], it[3]
            col, w, op = LINES[kind]
            if sketch:
                col, op = '#3B3B39', .55 if kind not in ('bay',) else .35
                w = .5
                out.append(f'<polyline points="{pts2([a, b], .5, rnd)}" fill="none" stroke="{col}" stroke-width="{w}" opacity="{op}"/>')
            else:
                out.append(f'<line x1="{P(*a)[0]:.1f}" y1="{P(*a)[1]:.1f}" x2="{P(*b)[0]:.1f}" y2="{P(*b)[1]:.1f}" stroke="{col}" stroke-width="{w}" opacity="{op}"/>')
        elif t == 'ell':
            kind, x, y, z, r = it[1:]
            pts = iso_ellipse(x, y, z, r)
            if sketch:
                out.append(f'<polygon points="{pts2(pts, .4, rnd)}" fill="#FBFAF6" stroke="#3B3B39" stroke-width=".7"/>')
            elif kind == 'fan':
                out.append(f'<polygon points="{pts2(pts)}" fill="{FLAT["fan"]}" stroke="#A9B0BB" stroke-width=".5"/>')
                out.append(f'<polygon points="{pts2(iso_ellipse(x, y, z, r * .35))}" fill="#8F97A3"/>')
            else:
                out.append(f'<polygon points="{pts2(pts)}" fill="#FFFFFF" stroke="#C3C8D1" stroke-width=".4"/>')
        elif t == 'tree':
            _, x, y, r, h = it
            gx, gy = P(x, y, 0); cx, cy = P(x, y, h * .78)
            if sketch:
                out.append(f'<line x1="{gx:.1f}" y1="{gy:.1f}" x2="{cx:.1f}" y2="{cy:.1f}" stroke="#3B3B39" stroke-width=".8"/>')
                # loose scribble crown
                pts = []
                for i in range(15):
                    a = 2 * math.pi * i / 14; rr = r * K * (1 + rnd.uniform(-.12, .12))
                    pts.append(f'{cx + rr * math.cos(a):.1f},{cy - r * K * .2 + rr * .92 * math.sin(a):.1f}')
                out.append(f'<polygon points="{" ".join(pts)}" fill="#FBFAF6" stroke="#3B3B39" stroke-width=".8" stroke-linejoin="round"/>')
                continue
            sh = f'<ellipse cx="{gx + r * K * .5:.1f}" cy="{gy + 1:.1f}" rx="{r * K * 1.05:.1f}" ry="{r * K * .5:.1f}" fill="#98A2B3" opacity="{.22 if real else .16}"' + (' filter="url(#blur2)"' if real else '') + '/>'
            out.append(sh)
            out.append(f'<line x1="{gx:.1f}" y1="{gy:.1f}" x2="{cx:.1f}" y2="{cy:.1f}" stroke="#9A8B78" stroke-width="2"/>')
            # soft crown: two overlapping rounded blobs
            R = r * K * 1.35
            if real:
                out.append(f'<ellipse cx="{cx + R * .25:.1f}" cy="{cy - R * .05:.1f}" rx="{R * .8:.1f}" ry="{R * .72:.1f}" fill="#7FA56C"/>')
                out.append(f'<ellipse cx="{cx - R * .12:.1f}" cy="{cy - R * .3:.1f}" rx="{R * .82:.1f}" ry="{R * .75:.1f}" fill="url(#tree)"/>')
            else:
                out.append(f'<ellipse cx="{cx + R * .25:.1f}" cy="{cy - R * .05:.1f}" rx="{R * .8:.1f}" ry="{R * .72:.1f}" fill="#9DBE8B"/>')
                out.append(f'<ellipse cx="{cx - R * .12:.1f}" cy="{cy - R * .3:.1f}" rx="{R * .82:.1f}" ry="{R * .75:.1f}" fill="#B9D2A8"/>')
        elif t == 'shadow':
            if sketch: continue
            fp = [(TX0, TY0, 0), (TX1, TY0, 0), (TX1, TY1 + 1.7, 0), (TX0, TY1 + 1.7, 0)]
            dx, dy = TOP * .55, -TOP * .3
            sh = fp + [(x + dx, y + dy, 0) for x, y, _ in fp]
            pts = [P(*p) for p in sh]
            # convex hull
            pts = sorted(set(pts))
            def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
            lo, hi = [], []
            for p in pts:
                while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0: lo.pop()
                lo.append(p)
            for p in reversed(pts):
                while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0: hi.pop()
                hi.append(p)
            hull = lo[:-1] + hi[:-1]
            hp = ' '.join(f'{a:.1f},{b:.1f}' for a, b in hull)
            if real:
                out.append(f'<polygon points="{hp}" fill="#8C96A8" opacity=".2" filter="url(#blur)"/>')
                ao = ' '.join(f'{P(*p)[0]:.1f},{P(*p)[1]:.1f}' for p in [(TX0 - 1.5, TY0 - 1.5, 0), (TX1 + 2, TY0 - 1.5, 0), (TX1 + 2, TY1 + 4, 0), (TX0 - 1.5, TY1 + 4, 0)])
                out.append(f'<polygon points="{ao}" fill="#7D879A" opacity=".18" filter="url(#blur)"/>')
            else:
                out.append(f'<polygon points="{hp}" fill="#B8BFCC" opacity=".22"/>')

    if alert:
        # glow behind the alert floor on both faces
        z = G + 5 * FH + FH / 2
        gx, gy = P(TX1, (TY0 + TY1) / 2, z)
        if real or mode == 'flat':
            out.append(f'<ellipse cx="{gx:.1f}" cy="{gy:.1f}" rx="150" ry="60" fill="url(#glow)" />' if real else '')
    if sketch:
        # construction lines: extend the tower's verticals and a ground line
        for (x, y) in ((TX0, TY1), (TX1, TY1), (TX1, TY0)):
            a = P(x, y, -3); b = P(x, y, TOP + 8)
            out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#4A6FE3" stroke-width=".5" stroke-dasharray="3 3" opacity=".6"/>')
        a = P(-6, SY, 0); b = P(SX + 6, SY, 0)
        out.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#4A6FE3" stroke-width=".5" stroke-dasharray="3 3" opacity=".6"/>')
    d = ''.join(defs)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="{minx:.1f} {miny:.1f} {W:.1f} {H:.1f}">'
            + (f'<defs>{d}</defs>' if d else '') + ''.join(out) + '</svg>')

if __name__ == '__main__':
    od = sys.argv[1]; os.makedirs(od, exist_ok=True)
    for name, mode, alert in (('twin-sketch', 'sketch', False), ('twin-25d', 'flat', False), ('twin-render', 'real', False), ('twin-render-alert', 'real', True), ('twin-25d-alert', 'flat', True)):
        s = render(mode, alert)
        open(os.path.join(od, name + '.svg'), 'w').write(s)
        print(name, len(s))
