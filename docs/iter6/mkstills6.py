import json, re, os, sys
P = 'canvas/root/project/'
# scene stills: the prototype frozen at a scroll position (100 = one screen). One source of truth with Proto6.
SC = [
 (20, 'Hero', '0–140', 'After the loader (8 weeks · 1 MVP · 3 people, the band opening), your hero in Manrope, softer and smaller. The finished building with floor 6 lit is the promise. No rail yet.',
  'Hero text rises out. The building fades and the floor plan fades in as the whole background: we rewind to week 1. The tick rail fades in.'),
 (235, 'Strategy', '175–300', 'Week 1. The plan covers the background at 30%. One line above, one claim.', 'The plan slowly tilts into 3D (frames 0 → 22) and shrinks towards the building position.'),
 (362, 'The problem', '305–420', 'The problem as one concrete moment. Floor 6 enters the story.', 'Veil blurs in; the first slab appears underneath. The week pill shows only while text is on screen.'),
 (475, 'Week 1 · end', '430–520', 'Chapter break.', 'Veil clears. Floors rise (weeks 2–4 are floors only). The three bottom cards fade in, empty: the first piece of UI.'),
 (640, 'Design', '545–692', 'Partial UI: only the three cards, skeletons. No logo, tabs or building name.', 'More floors (45 → 58).'),
 (745, 'The 3D model', '696–792', 'Change, handled calmly.', 'Data arrives: the card figures count up. Floors complete by the end of week 4 (frame 75).'),
 (845, 'Real data', '796–892', 'The cards fill with live numbers.', 'Second layer of the skeleton starts (week 5).'),
 (940, 'Messy data', '896–982', 'Engineering in one line.', 'The cards fade away; the skeleton keeps growing (92 → 100).'),
 (1035, 'It builds itself', '986–1082', 'No UI. Just the model and one line.', 'Only the cost card returns, now as a chart with one red spike; the callout draws in.'),
 (1140, 'Buried', '1088–1182', 'One card on its own tells the problem.', 'The card leaves; only the chat panel slides in, with a long paragraph answer.'),
 (1240, 'The chat box', '1188–1292', 'One panel on its own tells the common approach.', 'Everything leaves; the building fades to 20%. Only the search box appears; the underline draws under “Asking”.'),
 (1380, 'We flipped it', '1320–1430', 'Text and the search box only. No logo, tabs, side icons or cards.', 'The question types itself into the search box (week 7, the facade starts closing).'),
 (1490, 'You ask', '1420–1520', 'No story text: the search box speaks.', 'The scan runs over the building; the assistant shows its steps above the input.'),
 (1550, 'The scan', '1520–1580', 'Three pieces: scan, assistant, input.', 'The building completes (end of week 7), floor 6 lights, the answer card and pin arrive.'),
 (1630, 'It builds the screen', '1580–1664', 'The payoff, still partial: answer card, input, pin.', 'The input leaves; the cooling card and its source popover rise.'),
 (1705, 'Every number has a source', '1668–1744', 'Trust, shown on a real figure.', 'The UI fades; veil; week 8.'),
 (1790, 'Week 8', '1750–1828', 'The last chapter break.', 'Veil clears; the building moves right; the quote rises.'),
 (1878, 'Outcome', '1834–1922', 'The founder’s voice (placeholder until confirmed).', 'Floor 6 lights again; the building fades behind the statement.'),
 (1962, 'Monday', '1928–1998', 'Closes the floor 6 thread.', 'The rail leaves. The whole app appears for the first time, inside a thin-bezel monitor (no stand), on a soft studio backdrop.'),
 (2140, 'Try it', '1995–2380', 'The full, live product in the device. Ask, scan, answer.', 'A normal scroll continues into the page: the enquiry form, then the questions (including how we worked), then the footer.'),
]
def board(at, n, title):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{n:02d} · {title}</title>
<script src="./support.js"></script>
<link rel="stylesheet" href="i6app.css">
<link rel="stylesheet" href="i5.css">
<link rel="stylesheet" href="i6p.css">
</head>
<body>
<x-dc>
<helmet><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&family=Figtree:wght@400;500;600;700&family=Manrope:wght@400;500;600;700&display=swap"><style>body{{margin:0}}</style></helmet>
<div style="position: relative; width: 1440px; height: 900px; overflow: hidden;">
  <dc-import name="Proto6" at="{at}" hint-size="100%,100%"></dc-import>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":900}}}}'>
class Component extends DCLogic {{ renderVals() {{ return {{}}; }} }}
</script>
</body>
</html>
'''
files = []
for k, (at, title, rng, note, nxt) in enumerate(SC, 1):
    fn = f'I6S-{k:02d}-' + re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-') + '.dc.html'
    open(P + fn, 'w').write(board(at, k, title)); files.append(fn)
if '--no-canvas' in sys.argv: print(len(files)); sys.exit()
d = json.load(open(P + 'canvas.json'))
old = [k for k in d['boards'] if re.match(r'I6-\d\d-', k)]
for k in old: d['boards'].pop(k)
for k in [k for k in d['boards'] if k.startswith('I6S-') or k == 'Proto6.dc.html']: d['boards'].pop(k)
d['order'] = [k for k in d['order'] if not (re.match(r'I6-\d\d-', k) or k.startswith('I6S-') or k == 'Proto6.dc.html')]
for k in [k for k in d['notes'] if re.match(r'i6[nt]\d\d', k) or k.startswith('i6s')]: d['notes'].pop(k)
d['boards']['Proto6.dc.html'] = dict(page='iter6', x=4720, y=0, w=1440, h=900, title='Iteration 6 · Live prototype (scroll it)')
d['order'].append('Proto6.dc.html')
d['notes']['i6sp'] = {'page': 'iter6', 'x': 4720, 'y': 930, 'w': 1440, 'size': 20, 'fill': 'green', 'text': 'Scroll it. The loader plays first (about 3 s), then the story runs on one scroll: the building is the camera, the app assembles around it in the iteration 5 timeline, and the window frame only appears at “Try it”, where the prototype is live.'}
Y0, STEP = 1300, 1200
for k, fn in enumerate(files):
    at, title, rng, note, nxt = SC[k]
    y = Y0 + k * STEP
    d['boards'][fn] = dict(page='iter6', x=0, y=y, w=1440, h=900, title=f'{k+1:02d} · {title} · scroll {rng}')
    d['order'].append(fn)
    d['notes'][f'i6s{k+1:02d}'] = {'page': 'iter6', 'x': 1560, 'y': y, 'w': 520, 'size': 22, 'fill': 'blue', 'text': note}
    if nxt: d['notes'][f'i6st{k+1:02d}'] = {'page': 'iter6', 'x': 0, 'y': y + 930, 'w': 1440, 'size': 20, 'fill': 'green', 'text': f'↓ {k+1:02d} → {k+2:02d} · ' + nxt}
if 'I6App.dc.html' in d['boards']: d['boards']['I6App.dc.html'].update(x=2300, y=Y0)
if 'i6t' in d['notes']: d['notes']['i6t']['text'] = 'Iteration 6 · one scroll: loader → hero → five chapters → try it → close'
if 'i6sys' in d['notes']: d['notes']['i6sys']['text'] = ('System\n• Page: iteration 4 cool greys. Ink #0F1115, body #5B616B, labels #8A9099. App green #0F9160, floor 6 red #D84A3B, highlighter #2EE37A on three moments only (energy/AI, Asking, two words).\n'
    '• Type: Bricolage Grotesque for headlines (128 hero, 96 chapters, 64 once the app is on screen); Figtree for the line above and the one line of detail.\n'
    '• Text: at most a line above, a headline and one line. Left edge on the iteration 5 column (14cqi), clear of the tick rail; product scenes use the app’s title slot.\n'
    '• Timeline (iteration 5): the app assembles full-bleed around the building in week 2, data arrives in week 4, AI as a chat box in week 6, it leaves at the flip and returns as the product. The window frame appears only at Try it.\n'
    '• Chrome: tick rail with the glass week pill, and the progress line bottom right.')
d['launch'] = {'file': 'Proto6.dc.html', 'view': 'focused'}
json.dump(d, open(P + 'canvas.json', 'w'), indent=1, ensure_ascii=False)
json.dump({'new': files, 'old': old}, open('i6s.json', 'w'))
print(len(files), 'stills; removed', len(old))
