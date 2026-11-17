import json, re, sys
P = 'canvas/root/project/'
IDS = json.load(open('ids5.json'))  # 151 rendered frames, iteration 5 sequence (same model as iteration 4)
FONTS = 'https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..700&family=Figtree:wght@400;500;600;700&display=swap'

def page(title, body, cls=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
<link rel="stylesheet" href="i6app.css">
<link rel="stylesheet" href="i6.css">
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap">
<style>body{{margin:0}}</style>
</helmet>
<div class="b6 {cls}">
{body}</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":900}}}}'>
class Component extends DCLogic {{ renderVals() {{ return {{}}; }} }}
</script>
</body>
</html>
'''

def bld(f, tx=0, ty=0, s=1, op=1, z=None):
    zz = f' z-index: {z};' if z is not None else ''
    return f'  <div class="bld6" style="transform: translate({tx}px, {ty}px) scale({s}); opacity: {op};{zz}"><img src="/_blob/{IDS[f]}" alt=""></div>\n'

def pill(w, sub=''):
    if not w: return '<span class="wk6-sp"></span>'
    return f'<span class="wk6"><i></i>{w}{" <em>· " + sub + "</em>" if sub else ""}</span>'

def col(wk, k, h, size='l', proof='', l=60, w=872, t=128, extra=''):
    return (f'  <div class="col6" style="left: {l}px; top: {t}px; width: {w}px;">\n    {pill(*wk) if isinstance(wk, tuple) else pill(wk)}\n'
            + (f'    <p class="k6">{k}</p>\n' if k else '    <p class="k6">&nbsp;</p>\n')
            + f'    <h2 class="h6 {size}">{h}</h2>\n' + proof + extra + '  </div>\n')

def proof(label, text, small='', cls=''):
    s = f'    <div class="pr6 {cls}">' + (f'<b>{label}</b>' if label else '') + f'<span>{text}</span>'
    if small: s += f'<small>{small}</small>'
    return s + '</div>\n'

def cen(wk, k, h, size='l', top=300, sub='', extra=''):
    return (f'  <div class="cen6" style="top: {top}px;">\n' + (f'    {pill(*wk) if isinstance(wk, tuple) else pill(wk)}\n' if wk else '')
            + (f'    <p class="k6">{k}</p>\n' if k else '') + f'    <h2 class="h6 {size}">{h}</h2>\n'
            + (f'    <p class="sub6">{sub}</p>\n' if sub else '') + extra + '  </div>\n')

def mk(w): return f'<mark class="mk6">{w}</mark>'

# the app inside a product window. Building transform is in app units (cqi), the same values the live prototype uses.
STORY_T = 'translate(8cqi, 1cqi) scale(1)'
PROD_T = 'translate(6cqi, 3.4cqi) scale(1.06)'
WX, WY, WW = 508, 168, 872   # columns 5-12, top on the line-above row
def win(frame, tf, x=WX, y=WY, w=WW, title='ConnectX <span>· Meridian Tower</span>', bop=1, **app):
    attrs = ' '.join(f'{k}="{v}"' for k, v in app.items())
    return (f'  <div class="win6" style="left: {x}px; top: {y}px; width: {w}px;">\n'
            f'    <div class="win6-bar"><span class="win6-dots"><i></i><i></i><i></i></span><span class="win6-title">{title}</span><span class="win6-live"><b></b>Live</span></div>\n'
            f'    <div class="s4">\n      <div class="s4__bld" style="transform: {tf}; transform-origin: 52% 55%; opacity: {bop};"><img src="/_blob/{IDS[frame]}" alt="Meridian Tower"></div>\n'
            f'      <div style="position: absolute; inset: 0;"><dc-import name="I6App" {attrs} hint-size="100%,100%"></dc-import></div>\n'
            f'    </div>\n  </div>\n')

def prog(p): return f'  <div class="pg6"><span>Scroll</span><s><i style="width: {p}%;"></i></s><span>{p}%</span></div>\n'

B = []   # (slug, title, body, cls, note, transition-to-next)
def add(slug, title, body, note, nxt, cls=''): B.append((slug, title, body, cls, note, nxt))

# ---------- loader ----------
def loader(c, n, lab, h):
    top = (900 - h) // 2
    return (f'  <div class="band6" style="top: {top}px; height: {h}px;"><div class="ldr6"><span class="c">{c}</span><span class="n">{n}</span><span class="l">{lab}</span></div></div>\n')
LOAD = [('001', '8 weeks', 'to build', 376), ('002', '1 MVP', 'built by', 632), ('003', '3 people', '', 888)]

# ---------- story ----------
BRIEF = 'ConnectX’s founder had a hunch: office buildings waste a lot of energy, and AI should help. But there was no product. No screens. No plan.'
add('01-Hero', 'Hero · two words',
    bld(150, 450, 40, 1.12)
    + col('Start', 'We build full', f'Working SaaS with<br>2 words {mk("energy")}<br>and {mk("AI")}', 'xl', w=1000)
    + f'  <div class="pr6" style="position: absolute; left: 60px; top: 648px; z-index: 5; margin: 0;"><b>Initial brief</b><span>{BRIEF}</span></div>\n',
    'Hero · your title and layout, on the cool grey. The finished building with floor 6 already lit sits right and bleeds off the edge: the payoff is shown before the story starts. Highlighter only on the two words of the brief.',
    'Scroll 100vh. Hero text fades up 24px and out. The finished building dissolves back into its plan drawing (frame 150 → 0) as it slides right: we rewind to week 1.')
add('02-Strategy', 'Strategy',
    bld(0, 420, 40, 1.2, .38)
    + col('Week 1', 'We did the product strategy and definition', 'Helped the founder define the product and the business',
          proof=proof('How we did it', 'We spoke to the people who run office buildings: facility managers, finance and sustainability leads. Then we agreed with the founder who the product is for, what it must answer first and how it makes money.')),
    'Chapter 1 opens. Plan drawing at 55% behind the text: strategy is the blueprint, nothing is built yet. Three levels: what we did, the claim, how we did it.',
    'Text cross-fades in place (out, then in). The plan tilts into 3D (frames 0 → 22) and moves further right.')
add('03-Problem', 'The problem',
    bld(22, 470, 50, 1.08, .8)
    + col('Week 1', 'What we kept hearing', 'Floor 6 cooled an empty office for three weeks',
          proof=proof('Nobody noticed', 'The meters recorded all of it. Facilities, finance and sustainability looked at the same numbers and each needed a different answer. So it showed up on the bill.', 'An illustrative example, built from what facility teams told us.')),
    'The problem, as one concrete moment. Floor 6 enters the story here and comes back four more times.',
    'Veil blurs in over 40vh. Underneath, the first structure rises (22 → 40). The week pill moves to the centre and changes to “Week 1 · end”.')
add('04-Week-1-end', 'Week 1 · end',
    bld(40, 160, 40, 1.1) + '  <div class="veil6"></div>\n'
    + cen(('Week 1', 'end'), 'Once the product and strategy were defined', 'Building for the business', top=332),
    'Chapter break. The building keeps rising under a blurred cool-grey veil; text centred. Closes discovery, opens design.',
    'Veil clears. The building keeps rising (40 → 92) and the product window grows around it, from full-bleed down to columns 5–12. Dashboard panels fade in one by one: top bar, then cards. Story text returns at 64px in columns 1–4.')
QS = ['Where are we wasting energy right now?', 'What’s this month going to cost us?', 'When do prices spike?', 'Are we on track for our targets?', 'What should we fix today?']
add('05-Design', 'Design · five questions',
    win(92, STORY_T, mode='story', noai='1', ui='1', fill='1', ai='0', focus='f6')
    + col('Week 2', 'We designed the product', 'Five questions became one dashboard', 'm', w=424,
          proof='    <div class="pr6 tight"><ol class="ql6">' + ''.join(f'<li><b>{i:02d}</b>{q}</li>' for i, q in enumerate(QS, 1)) + '</ol></div>\n'),
    'Into the product for the first time: the real iteration 4 dashboard, before AI (assistant hidden). Text in columns 1–4, window in 5–12, both on the 168 line.',
    'Window frame dissolves outward, panels fade. The building scales out of the window back to the right slot (frames 92 → 100).')
add('06-3D-model', 'The 3D model',
    bld(100, 420, 30, 1.04)
    + col('Week 3', 'Then the brief changed', 'A 3D model of the building, halfway through',
          proof=proof('How we handled it', 'ConnectX wanted people to see where the energy goes, not just read about it. We re-planned around the model and kept the eight-week date.')),
    'Change, handled calmly. The building fills in to walls-done.',
    'Text cross-fades. Camera pushes in slightly (scale 1.04 → 1.1) as wiring starts (100 → 108).')
add('07-Real-data', 'Real data',
    bld(108, 400, 20, 1.1)
    + col('Week 4', 'We connected real data', 'A real office building, every 15 minutes',
          proof=proof('How we did it', 'Through the electricity provider’s API: meters, bills, prices and sensors from a working commercial building. From week four, every screen ran on it.')),
    'Engineering chapter starts. Wiring appears in the model.',
    'The one sideways move: text fades out first, then the building slides to the left half (x +400 → −470) while wiring completes (108 → 114). New text rises in columns 8–12.')
add('08-Messy-data', 'Messy data',
    bld(114, -520, 20, 1.04)
    + col('Week 5', 'We made the data trustworthy', 'Real data is messy. We cleaned it.', l=852, w=528,
          proof=proof('How we did it', 'Readings go missing. Meters glitch. Totals don’t match the bill. We fill gaps and label them, check spikes against nearby meters, and match every total to what finance sees.')),
    'Mirrored for rhythm: building left, text in columns 8–12. The boring hard stuff, said plainly.',
    'Text fades, building slides back right while the facade starts closing (114 → 128).')
add('09-Builds-itself', 'It builds itself',
    bld(128, 400, 20, 1.08)
    + col('Week 5', 'We made the 3D model build itself', 'Pick a building type. It puts itself together.',
          proof=proof('How we did it', 'The model is generated from a library of parts and the building’s energy sources, so the next building doesn’t need a 3D artist.')),
    'Built to scale beyond one building. Facade closing from the top.',
    'Facade completes (128 → 149) as the window grows around the building again, same move as 04 → 05. Dashboard, still no AI. The red callout draws last.')
add('10-Buried', 'Buried',
    win(149, STORY_T, mode='story', noai='1', chart='1', ui='1', fill='1', ai='0', focus='f6')
    + col('Week 6', 'What wasn’t working', 'The answer was there. Buried in a chart.', 'm', w=424,
          proof=proof('', 'Floor 6 was one small spike in the cost chart, on one of five screens. You had to know where to look.', cls='tight'))
    + '  <div class="lead6" style="left: 1011px; top: 688px; width: 1px; height: 92px;"></div>\n  <span class="call6" style="left: 1004px; top: 790px;"><i></i>Floor 6, in here somewhere</span>\n',
    'So close, yet buried. The real dashboard; the floor 6 spike is the only red on the board, and the callout points at it from outside the window.',
    'Window holds. The assistant card slides in from the right (8% → 0); the question and the paragraph answer type in.')
add('11-Chat-box', 'The chat box',
    win(149, STORY_T, mode='story', chat='1', ui='1', fill='1', ai='1', focus='f6')
    + col('Week 6', 'What we tried first', 'A chat box in the corner', 'm', w=424,
          proof=proof('', 'It answered with a paragraph. Then you still had to go and find floor 6 yourself.', cls='tight')),
    'The common approach and why it falls short: a real chat answer, long and vague, next to a dashboard that still hides the problem.',
    'Everything leaves: panels fade, the window frame dissolves, the building fades to 18%. The statement rises line by line; the highlighter draws under “Asking” last.')
add('12-We-flipped-it', 'We flipped it',
    bld(149, 86, 48, 1.06, .18)
    + cen('Week 6', '', f'So we flipped it.<br>{mk("Asking")} comes first.<br>The screen is the answer.', top=268),
    'The turn of the whole story. The interface disappears so it can come back in its new form.',
    'Statement fades. The window rebuilds around the building in product mode: home screen first, then the question types in.')
add('13-You-ask', 'You ask',
    win(149, PROD_T, bop=.35, mode='home', q='Why is floor 6 using so much cooling?', focus='f6')
    + col('Week 7', 'How it works now', 'You ask.', 'm', w=424,
          proof=proof('', 'In plain words. It works out what you mean, pulls the right numbers and checks them against the meters. It doesn’t guess.', cls='tight')),
    'Product mode, the real iteration 4 home screen with the question typed in. Simple from the user’s seat.',
    'Send. The scan runs (plot, then floor by floor, the iteration 4 loading state, about 2 s), then the answer card slides in, floor 6 lights (149 → 150) and the pin drops.')
add('14-It-builds-the-screen', 'It builds the screen',
    win(150, PROD_T, mode='answer', q='Why is floor 6 using so much cooling?', focus='f6')
    + col('Week 7', 'Then', 'It builds the screen for you.', 'm', w=424,
          proof=proof('', 'The building turns to floor 6. The cards show the problem. And it suggests the fix: pre-cool at 11:00, before the sun hits the west glass.', cls='tight')),
    'The payoff: the real answer screen. Floor 6 lit, pin, answer card, the cards re-written for floor 6.',
    'The source popover rises from the 16 kW figure (16px, fade). Nothing else moves.')
add('15-Every-number-has-a-source', 'Every number has a source',
    win(150, PROD_T, mode='answer', src='1', q='Why is floor 6 using so much cooling?', focus='f6')
    + col('Week 7', 'And', 'Every number has a source.', 'm', w=424,
          proof=proof('', 'It runs on ConnectX’s own servers and only sees what you’re allowed to see. Every figure links back to its meter. We tested it on 24+ real questions.', cls='tight')),
    'Trust, shown not told: the source popover on a real figure.',
    'Window recedes and the frame dissolves; the veil blurs in; the pill changes to Week 8.')
add('16-Week-8', 'Week 8',
    bld(149, 160, 40, 1.06) + '  <div class="veil6"></div>\n'
    + cen('Week 8', 'Eight weeks after two words', 'Ready for investors', top=332),
    'Chapter break, the last one. Finished building under the veil.',
    'Veil clears. Building settles into the right slot; the quote fades in after the headline.')
add('17-Outcome', 'Outcome',
    bld(149, 420, 30, 1.0)
    + col('Week 8', 'Where it landed', 'A working product on a real building, in front of investors',
          extra='    <div style="margin-top: 56px; display: flex; flex-direction: column; gap: 16px; max-width: 600px;"><p class="qt6">“We walked into the investor meeting with a product, not a pitch deck.”</p><span class="who6">Founder, ConnectX <span class="ph6">PLACEHOLDER</span></span></div>\n'),
    'Real result in the founder’s voice (placeholder quote until confirmed).',
    'Text fades; the building lights floor 6 again (149 → 150) and fades to 20% behind the statement.')
add('18-Monday', 'Monday, not the bill',
    bld(150, 86, 48, 1.06, .2)
    + cen('Week 8', '', 'For the facility manager, floor 6 is now a question on Monday.', top=300, sub='Not a surprise on the bill.'),
    'Closes the floor 6 thread for the person who had the problem.',
    'Background dims to the window backdrop; the product window scales up from the centre and the live app loads inside.')
add('19-Try-it', 'Try it',
    '  <div style="position: absolute; inset: 0; background: linear-gradient(180deg, #D3D8DE 0%, #CBD1D8 100%);"></div>\n'
    + '  <div class="cen6" style="top: 48px; left: 0; right: 0;"><span class="wk6" style="margin-bottom: 16px;"><i></i>Week 8 <em>· prototype</em></span><h2 class="h6 m">Don’t take our word for it. Try it.</h2></div>\n'
    + win(149, PROD_T, x=220, y=196, w=1000, title='ConnectX <span>· live prototype · you’re in the real product</span>', bop=.35, mode='home', focus='f6'),
    'Story mode is over. The iteration 5 product window with the real app inside; this is where the prototype goes live.',
    'Window slides up and out; the page lightens back to the cool grey.')
add('20-How-we-worked', 'How we worked',
    col('', 'How we worked', 'Three people. One weekly review. Everything is theirs.', 'm',
        proof=proof('', 'One designer and two developers, from the first conversation to the investor demo. ConnectX sat in every weekly review, so nothing was a surprise. The code, the designs and the data model all belong to them.'), w=648)
    + '  <div style="position: absolute; left: 852px; top: 216px; width: 528px; display: flex; flex-direction: column; gap: 32px; z-index: 5;">\n'
    + ''.join(f'    <div class="ms6"><b>{a}</b><span>{b}</span></div>\n' for a, b in [('WEEK 1', 'We found the real problem'), ('WEEK 3', 'The design was agreed'), ('WEEK 4', 'It ran on real data'), ('WEEK 8', 'Investors used it')])
    + '  </div>\n',
    'What working with us is like. Text in columns 1–6, milestones in 8–12.',
    'Milestones fade out; the closing line rises.')
FAQ = [('I only have an idea. Is that enough?', 'Yes. That’s where ConnectX started. The first week is about finding the real problem.'),
       ('How soon could I show investors something?', 'ConnectX did in eight weeks, running on real data from week four.'),
       ('Do you design it or build it?', 'Both. The same three people work it out, design it and build it.'),
       ('Will the AI make things up?', 'It answers from your data, checks your systems for exact numbers, and we test it on real questions first.')]
add('21-Your-turn', 'Your turn',
    cen('', 'Your turn', f'Got {mk("two words")} and a hunch?<br>That’s how ConnectX started.', top=96,
        extra='    <div style="margin-top: 40px; display: flex; align-items: center; gap: 24px;"><span class="btn6">Start a project <span aria-hidden="true">→</span></span><span class="tiny6" style="font-size: 16px;">We reply within a day.</span></div>\n')
    + '  <div style="position: absolute; left: 60px; right: 60px; top: 568px; display: grid; grid-template-columns: 1fr 1fr; column-gap: 24px; z-index: 5;">\n'
    + ''.join(f'    <div class="faq6" style="padding-right: 88px;"><b>{q}</b><span>{a}</span></div>\n' for q, a in FAQ)
    + '  </div>\n',
    'Back to the reader’s two words. One button, four plain questions.', '')

LT = ['Band grows 376 → 632px (0.8 s, ease-out). “8 weeks” slides up and out, “1 MVP” rises in; counter 001 → 002.',
      'Band grows 632 → 888px. “1 MVP” → “3 people”; counter 002 → 003.',
      'Band opens to full screen (0.6 s); the number fades. Hero line above and headline rise 24px, one line every 80 ms; the highlighter draws left to right under “energy” and “AI”; the building fades in and lifts 16px; pill and brief last.']
LN = ['Loader 1 of 3. Black screen, cool-grey band. Reads as one sentence across three beats: 8 weeks to build · 1 MVP · built by 3 people.', 'Loader 2 of 3.', 'Loader 3 of 3. The band is almost full; next it opens into the hero.']

# ---------- write boards ----------
n = len(B); files = []
for i, (c, num, lab, h) in enumerate(LOAD):
    fn = f'I6-L{i+1}-Loader.dc.html'
    open(P + fn, 'w').write(page(f'Loader {i+1}', loader(c, num, lab, h) + f'  <span class="tag6"><b>L{i+1}</b>Loader · {num}</span>\n', 'ld6'))
    files.append(fn)
for i, (slug, title, body, cls, note, nxt) in enumerate(B):
    pct = round(100 * (i + 1) / n)
    fn = f'I6-{slug}.dc.html'
    open(P + fn, 'w').write(page(title, body + prog(pct) + f'  <span class="tag6"><b>{i+1:02d}</b>{title}</span>\n', cls))
    files.append(fn)

if '--no-canvas' in sys.argv: print('boards only', len(files)); sys.exit()
# ---------- canvas page ----------
d = json.load(open(P + 'canvas.json'))
if not any(p['id'] == 'iter6' for p in d['pages']): d['pages'].append({'id': 'iter6', 'name': 'Iteration 6'})
for k in [k for k in d['boards'] if k.startswith('I6-') and k != 'I6App.dc.html']: d['boards'].pop(k)
d['order'] = [k for k in d['order'] if not (k.startswith('I6-'))]
for k in [k for k in d['notes'] if k.startswith('i6')]: d['notes'].pop(k)
NX = 1560
for i, fn in enumerate(files[:3]):
    d['boards'][fn] = dict(page='iter6', x=i * 1540, y=0, w=1440, h=900, title=f'L{i+1} · Loader')
    d['order'].append(fn)
    d['notes'][f'i6l{i+1}'] = {'page': 'iter6', 'x': i * 1540, 'y': 930, 'w': 1440, 'size': 20, 'fill': 'blue', 'text': LN[i] + '   →  ' + LT[i]}
Y0, STEP = 1300, 1200
for i, fn in enumerate(files[3:]):
    slug, title, body, cls, note, nxt = B[i]
    y = Y0 + i * STEP
    d['boards'][fn] = dict(page='iter6', x=0, y=y, w=1440, h=900, title=f'{i+1:02d} · {title}')
    d['order'].append(fn)
    d['notes'][f'i6n{i+1:02d}'] = {'page': 'iter6', 'x': NX, 'y': y, 'w': 520, 'size': 22, 'fill': 'blue', 'text': note}
    if nxt: d['notes'][f'i6t{i+1:02d}'] = {'page': 'iter6', 'x': 0, 'y': y + 930, 'w': 1440, 'size': 20, 'fill': 'green', 'text': f'↓ {i+1:02d} → {i+2:02d} · ' + nxt}
d['boards']['I6App.dc.html'] = dict(page='iter6', x=2300, y=Y0, w=1440, h=900, title='Component · ConnectX app, iteration 6 polish (story / home / loading / answer + noai, chat, chart, src)')
if 'I6App.dc.html' not in d['order']: d['order'].append('I6App.dc.html')
d['notes']['i6t'] = {'page': 'iter6', 'x': 0, 'y': -320, 'text': 'Iteration 6 · the story, refined: loader → hero → five chapters → close', 'kind': 'title1', 'maxW': 3000}
d['notes']['i6sys'] = {'page': 'iter6', 'x': 4700, 'y': 0, 'w': 560, 'size': 20, 'text':
    'System\n• Page: iteration 4 cool greys. Ink #0F1115, body #5B616B, labels #8A9099. App green #0F9160, floor 6 red #D84A3B, highlighter #2EE37A on three moments only (energy/AI, Asking, two words).\n'
    '• Type: Bricolage Grotesque 128/112 · 96/88 · 64/64; Figtree 32/40 line above, 20/30 body.\n'
    '• Grid: 12 columns, 60px margins, 24px gutters. Pill at y128, line above at 168, headline at 216, proof 56px below the headline.\n'
    '• Process folds: text in columns 1–8, building right. Product folds: text in columns 1–4, app window in 5–12 from y168.\n'
    '• Chrome: progress line bottom right only, plus the week pill.\n'
    '• Building: one continuous render sequence (frames 0–150); every board names its frame; the next board continues from it.'}
json.dump(d, open(P + 'canvas.json', 'w'), indent=1, ensure_ascii=False)
json.dump(files, open('i6files.json', 'w'))
print(len(files), 'boards')
