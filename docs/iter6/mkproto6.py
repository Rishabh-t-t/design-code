import json
P = 'canvas/root/project/'
IDS = json.load(open('ids5.json'))
FONTS = 'https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700&display=swap'
END = 2160          # end of the sticky story (scroll units, 100 = one screen); the page continues after it

def mk(w, v='hlA'): return f'<mark class="mk6p" style="--w: {{{{{v}}}}};">{w}</mark>'
def blk(key, pos, inner, cls=''):
    return f'            <div class="t6 {cls}" style="{pos} {{{{{key}}}}};">{inner}</div>\n'
L = 'left: 4.17cqi; top: 12.5cqi;'
T = ''
T += blk('tHero', 'left: 4.17cqi; top: 13.2cqi; width: 60cqi;', '<p class="k">We build full</p><h1 class="h xl">Working SaaS with<br>2 words ' + mk('energy') + '<br>and ' + mk('AI') + '</h1><p class="p" style="margin-top: 3.33cqi; max-width: 28cqi;"><b>Initial brief</b><br>ConnectX’s founder had a hunch: office buildings waste energy, and AI should help. No product. No screens. No plan.</p>')
T += blk('tStrat', L + ' width: 40cqi;', '<p class="k">We did the product strategy and definition</p><h2 class="h l">Helped the founder define the product and the business</h2>')
T += blk('tProb', L + ' width: 36cqi;', '<p class="k">What we kept hearing</p><h2 class="h l">Floor 6 cooled an empty office for three weeks</h2><p class="p">Nobody noticed. Until the bill.</p>')
T += blk('tW1', 'top: 24cqi;', '<p class="k">Once the product and strategy were defined</p><h2 class="h l">Building for the business</h2>', 'c')
T += blk('tDes', L + ' width: 28cqi;', '<p class="k">We designed the product</p><h2 class="h m">Five questions. One dashboard.</h2>')
T += blk('t3d', L + ' width: 28cqi;', '<p class="k">Then the brief changed</p><h2 class="h m">A 3D model, halfway through.</h2><p class="p">Same eight-week deadline.</p>')
T += blk('tReal', L + ' width: 28cqi;', '<p class="k">We connected real data</p><h2 class="h m">Real data, every 15 minutes.</h2><p class="p">Meters, bills and prices from a working office building.</p>')
T += blk('tMessy', L + ' width: 28cqi;', '<p class="k">We made it trustworthy</p><h2 class="h m">Messy data, cleaned.</h2><p class="p">Gaps labelled. Spikes checked. Totals matched to the bill.</p>')
T += blk('tBuild', L + ' width: 28cqi;', '<p class="k">We made it build itself</p><h2 class="h m">The model assembles itself.</h2><p class="p">Pick a building type and its energy sources.</p>')
T += blk('tBur', L + ' width: 28cqi;', '<p class="k">What wasn’t working</p><h2 class="h m">The answer was buried.</h2><p class="p">One small spike, on one of five screens.</p>')
T += blk('tChat', L + ' width: 28cqi;', '<p class="k">What we tried first</p><h2 class="h m">So we added a chat box.</h2><p class="p">It answered with a paragraph. You still had to find floor 6.</p>')
T += blk('tFlip', 'top: 6.5cqi;', '<h2 class="h l">So we flipped it.<br>' + mk('Asking', 'hlB') + ' comes first.</h2>', 'c')
T += blk('tScreen', L + ' width: 26cqi;', '<p class="k">Then</p><h2 class="h m">It builds the screen.</h2><p class="p">Floor 6, the cause and the fix.</p>')
T += blk('tSrc', L + ' width: 26cqi;', '<p class="k">And</p><h2 class="h m">Every number has a source.</h2><p class="p">Every figure links to its meter.</p>')
T += blk('tW8', 'top: 24cqi;', '<p class="k">Eight weeks after two words</p><h2 class="h l">Ready for investors</h2>', 'c')
T += blk('tOut', L + ' width: 38cqi;', '<p class="k">Where it landed</p><p class="qt6p">“We walked into the investor meeting with a product, not a pitch deck.”</p><span class="who6p">Founder, ConnectX <span class="ph6p">PLACEHOLDER</span></span>')
T += blk('tMon', 'top: 22cqi;', '<h2 class="h l">Floor 6 is now a question on Monday.</h2><p class="sub">Not a surprise on the bill.</p>', 'c')
T += blk('tTry', 'top: 1.5cqi;', '<p class="k" style="margin: 0;">Try it. Ask the building about floor 6.</p>', 'c')

FAQ = [
 ('I only have an idea. Is that enough?', 'Yes. That’s exactly where ConnectX started: two words and a hunch. The first week is about finding the real problem.', None),
 ('Who will work on my product?', 'Three people: one designer and two developers, from the first conversation to the investor demo. The same people the whole way.', None),
 ('How will we work together?', 'One weekly review where you see everything we’ve built, so nothing is a surprise. For ConnectX the milestones were:', [('WEEK 1', 'We found the real problem'), ('WEEK 3', 'The design was agreed'), ('WEEK 4', 'It ran on real data'), ('WEEK 8', 'Investors used it')]),
 ('How soon could investors see something?', 'ConnectX did in eight weeks, running on real data from week four.', None),
 ('Will the AI make things up?', 'It answers from your data, checks exact numbers against your systems, and we test it on real questions before anyone relies on it.', None),
 ('Who owns what you build?', 'You do. The code, the designs and the data model are yours.', None),
 ('What if we don’t have data yet?', 'We start on realistic sample data, design for the gaps, and switch to your real sources when they’re ready.', None),
]
faq_html = ''
for j, (q, a, ms) in enumerate(FAQ):
    extra = ''
    if ms: extra = '<div class="ms">' + ''.join(f'<div><b>{x}</b><span>{y}</span></div>' for x, y in ms) + '</div>'
    faq_html += f'''          <div><button type="button" onClick="{{{{faqT{j}}}}}" aria-expanded="{{{{faqE{j}}}}}">{q}<span aria-hidden="true">{{{{faqS{j}}}}}</span></button><sc-if value="{{{{faqO{j}}}}}" hint-placeholder-val="{{{{ {'true' if j == 0 else 'false'} }}}}"><p>{a}</p>{extra}</sc-if></div>\n'''

AFTER = f'''    <!-- after the story: a normal scroll into the form, the questions and the footer -->
    <div class="af6">
      <div class="in" style="display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: start;">
        <div>
          <span class="k">Your turn</span>
          <h2>Got <mark class="mk6p" style="--w: 100%;">two words</mark> and a hunch?</h2>
          <p class="lead">That’s how ConnectX started. Tell us your idea and we’ll get back to you within a day.</p>
        </div>
        <form class="card6" onSubmit="{{{{submit}}}}">
          <sc-if value="{{{{sent}}}}" hint-placeholder-val="{{{{ false }}}}"><div style="display: flex; flex-direction: column; gap: 8px; padding: 8px 0;"><b style="font: 600 20px/28px var(--i6-f);">Thanks, it reached us.</b><span style="color: var(--i6-body);">We’ll reply within one business day.</span></div></sc-if>
          <sc-if value="{{{{notSent}}}}" hint-placeholder-val="{{{{ true }}}}">
            <div class="fld6"><label for="p6-what">What’s the idea?</label><textarea id="p6-what" rows="3" placeholder="Two words are enough to start." value="{{{{what}}}}" onChange="{{{{setWhat}}}}"></textarea></div>
            <div class="fld6"><label>Where are you with it?</label><div style="display: flex; gap: 8px; flex-wrap: wrap;"><sc-for list="{{{{stages}}}}" as="g" hint-placeholder-count="3"><button type="button" class="{{{{g.cls}}}}" onClick="{{{{g.pick}}}}">{{{{g.t}}}}</button></sc-for></div></div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;"><div class="fld6"><label for="p6-name">Name</label><input id="p6-name" placeholder="Your name"></div><div class="fld6"><label for="p6-mail">Email</label><input id="p6-mail" type="email" placeholder="you@company.com"></div></div>
            <button class="go6" type="submit">Start a project <span aria-hidden="true">→</span></button>
          </sc-if>
        </form>
      </div>
      <div class="in" style="padding-top: 0; display: grid; grid-template-columns: 340px 1fr; gap: 48px;">
        <div><span class="k">Questions</span><h2 style="font-size: 40px; line-height: 46px;">What founders ask us.</h2></div>
        <div class="faq6">
{faq_html}        </div>
      </div>
      <div class="ft6"><div class="in">
        <span style="display: flex; flex-direction: column; gap: 10px;"><b>tcules</b><small>Modern products, designed and engineered as one.</small></span>
        <nav><a href="#">Work</a><a href="#">Studio</a><a href="#">Contact</a></nav>
        <small>© Tcules 2026</small>
      </div></div>
    </div>
'''

TPL = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>ConnectX case study · iteration 6</title>
<script src="./support.js"></script>
<link rel="stylesheet" href="i6app.css">
<link rel="stylesheet" href="i5.css">
<link rel="stylesheet" href="i6p.css">
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="{FONTS}">
<style>body{{margin:0}}</style>
</helmet>
<div class="p5-root p6-root">
  <svg width="0" height="0" style="position: absolute;" aria-hidden="true"><filter id="lg5-refract" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.03" numOctaves="1" seed="4" result="n"></feTurbulence><feDisplacementMap in="SourceGraphic" in2="n" scale="7" xChannelSelector="R" yChannelSelector="G"></feDisplacementMap></filter></svg>
  <div class="p5-scroll" onScroll="{{{{onScroll}}}}" ref="{{{{scRef}}}}" style="overflow-y: {{{{ovY}}}};">
    <div style="height: {END + 220}vh; position: relative;">
      <div class="p5-sticky">
        <div class="dim6" style="opacity: {{{{winDim}}}};" aria-hidden="true"></div>
        <div class="p5-stage">
          <div class="mon6" style="{{{{monShell}}}}" aria-hidden="true"></div>
          <div class="s4" style="transform: {{{{winTf}}}}; clip-path: {{{{winClip}}}}; transform-origin: 50% 50%; background: {{{{scrBg}}}};">
            <div class="s4__bld" style="z-index: 2; opacity: {{{{bOp}}}}; transform: {{{{bTf}}}}; transition: opacity .5s ease; transform-origin: 52% 55%;">
              <canvas class="p5-cv" width="1600" height="1000" ref="{{{{cvRef}}}}" aria-label="The building, from plan to finished tower" role="img"></canvas>
            </div>
            <sc-if value="{{{{uiOn}}}}" hint-placeholder-val="{{{{ false }}}}">
              <div style="position: absolute; inset: 0; z-index: 4; opacity: {{{{uiOp}}}};">
                <dc-import name="I6App" mode="{{{{mode}}}}" parts="{{{{parts}}}}" ui="1" fill="{{{{fill}}}}" ai="1" noai="0" chat="{{{{chat}}}}" chart="{{{{chart}}}}" src="{{{{src}}}}" q="{{{{q}}}}" focus="{{{{focus}}}}" on-send="{{{{send}}}}" on-q="{{{{setQ}}}}" on-key="{{{{onKey}}}}" on-pick="{{{{pick}}}}" hint-size="100%,100%"></dc-import>
              </div>
            </sc-if>
            <div class="veil6p" style="opacity: {{{{veil}}}};" aria-hidden="true"></div>
            <div class="call6p" style="left: 56.2cqi; top: 47.2cqi; opacity: {{{{callOp}}}};"><span><i></i>Floor 6, in here somewhere</span><s></s></div>
{T}          </div>
          <div class="t6 c" style="top: 1.6cqi; {{{{tTry}}}};"><p class="k" style="margin: 0;">Try it. Ask the building about floor 6.</p></div>
        </div>
      </div>
    </div>
{AFTER}  </div>

  <div class="pg6p" style="opacity: {{{{pgOp}}}};"><em>Scroll</em><s><i style="width: {{{{pctW}}}};"></i></s><span>{{{{pct}}}}%</span></div>

  <!-- week rail (iteration 5): ticks, and the current week only while its scene is on screen -->
  <div class="r5" style="opacity: {{{{railOp}}}}; height: {{{{railH}}}};" aria-hidden="true">
    <sc-for list="{{{{ticks}}}}" as="t" hint-placeholder-count="44"><i class="r5-t" style="top: {{{{t.y}}}}; width: {{{{t.w}}}}; opacity: {{{{t.o}}}};"></i></sc-for>
    <sc-for list="{{{{wk}}}}" as="w" hint-placeholder-count="9">
      <span class="{{{{w.cls}}}}" style="top: {{{{w.y}}}}; opacity: {{{{w.o}}}}; transform: translate({{{{w.x}}}}, -50%);"><sc-if value="{{{{w.major}}}}" hint-placeholder-val="{{{{ true }}}}"><b></b></sc-if>{{{{w.n}}}}<sc-if value="{{{{w.hasSub}}}}" hint-placeholder-val="{{{{ false }}}}"><small>{{{{w.sub}}}}</small></sc-if></span>
    </sc-for>
  </div>

  <!-- loader: a dark screen whose band opens while the numbers change -->
  <sc-if value="{{{{ldOn}}}}" hint-placeholder-val="{{{{ false }}}}">
    <div class="ld6o" style="opacity: {{{{ldOp}}}};" aria-label="Loading the case study">
      <div class="band" style="height: {{{{bandH}}}};"></div>
      <sc-for list="{{{{ldRows}}}}" as="r" hint-placeholder-count="3">
        <div class="row" style="opacity: {{{{r.o}}}}; transform: translateY(calc(-50% + {{{{r.y}}}})); transition-delay: {{{{r.dl}}}};"><span class="c">{{{{r.c}}}}</span><span class="n">{{{{r.n}}}}</span><span class="l">{{{{r.l}}}}</span></div>
      </sc-for>
    </div>
  </sc-if>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"at":{{"editor":"text","default":""}},"$preview":{{"width":1440,"height":900}}}}'>
__JS__
</script>
</body>
</html>
'''
# the try-it caption was added twice above (inside the stage block list); drop the stage-list copy
TPL = TPL.replace(blk('tTry', 'top: 1.5cqi;', '<p class="k" style="margin: 0;">Try it. Ask the building about floor 6.</p>', 'c'), '')

JS = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    const at = props.at !== undefined && props.at !== '' && props.at !== null ? +props.at : null;
    this.at = at;
    this.state = { d: at ?? 0, pct: at === null ? 0 : Math.round(100 * at / __END__), ph: 'home', q: '', focus: 'f6', lp: at === null ? 0 : 4, sent: false, faq: 0, stage: 0 };
    this.target = 0; this.raf = 0; this.drawn = -1; this.want = 0; this.started = false;
    this.IDS = __IDS__;
    let ready = 0;
    this.imgs = this.IDS.map((id, i) => { const im = new Image(); im.decoding = 'async'; im.onload = () => { if (i === 150 || i === 0) { ready++; this.tryStart(); } if (Math.abs(i - this.want) < 3) { this.drawn = -1; this.draw(this.want); } }; im.src = '/_blob/' + id; return im; });
    this.fontsOk = false;
    try { (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(() => { this.fontsOk = true; this.tryStart(); }); } catch (e) { this.fontsOk = true; }
    // the loader plays only once the page is on screen and the first renders and fonts are in
    this.tryStart = () => {
      if (this.at !== null || this.started || !this.sc || !this.fontsOk || ready < 2) return;
      this.started = true;
      this.lts = [1000, 1900, 2800, 3600].map((t, j) => setTimeout(() => this.setState({ lp: j + 1 }), t));
    };
    this.failSafe = at === null ? setTimeout(() => { ready = 2; this.fontsOk = true; this.tryStart(); }, 6000) : 0;
    this.scRef = (el) => { this.sc = el; this.tryStart(); };
    this.cvRef = (el) => { this.cv = el; this.drawn = -1; this.draw(this.want); };
    this.draw = (i) => {
      this.want = i;
      if (!this.cv || i === this.drawn) return;
      let k = -1;
      for (let r = 0; r < this.imgs.length; r++) { const a = this.imgs[i - r], b = this.imgs[i + r]; if (a && a.complete && a.naturalWidth) { k = i - r; break; } if (b && b.complete && b.naturalWidth) { k = i + r; break; } }
      if (k < 0) return;
      const ctx = this.cv.getContext('2d'); ctx.clearRect(0, 0, 1600, 1000); ctx.drawImage(this.imgs[k], 0, 0, 1600, 1000);
      this.drawn = k === i ? i : -1;
    };
    this.tick = () => {
      this.raf = 0;
      const d = this.state.d, diff = this.target - d;
      if (Math.abs(diff) < 0.05) { if (d !== this.target) this.setState({ d: this.target, pct: this.pctNow }); return; }
      this.setState({ d: d + Math.max(-8, Math.min(8, diff * 0.12)), pct: this.pctNow });
      this.raf = requestAnimationFrame(this.tick);
    };
    this.onScroll = (e) => {
      if (this.at !== null) return;
      const el = e.currentTarget, vh = el.clientHeight || 800;
      this.target = Math.max(0, Math.min(__END__, el.scrollTop / vh * 100));
      this.pctNow = Math.round(100 * Math.min(1, el.scrollTop / vh / (__END__ / 100)));
      this.after = el.scrollTop / vh * 100 > __END__ + 60;
      if (!this.raf) this.raf = requestAnimationFrame(this.tick);
    };
    this.focusOf = (q) => { const s = (q || '').toLowerCase(); if (/ev|charg/.test(s)) return 'ev'; if (/peak|price|tariff|cost/.test(s)) return 'tariff'; if (/solar|sun/.test(s)) return 'solar'; return 'f6'; };
    this.ask = (q, f) => { this.setState({ q, focus: f, ph: 'loading' }); clearTimeout(this.lt); this.lt = setTimeout(() => this.setState({ ph: 'answer' }), 6200); };
    this.send = () => { const q = this.state.q || 'Why is floor 6 using so much cooling?'; this.ask(q, this.focusOf(q)); };
    this.setQ = (e) => this.setState({ q: e.target.value });
    this.onKey = (e) => { if (e.key === 'Enter') { e.preventDefault(); this.send(); } };
    this.pick = (f, q) => this.ask(q, f);
  }
  componentWillUnmount() { if (this.raf) cancelAnimationFrame(this.raf); clearTimeout(this.lt); clearTimeout(this.failSafe); (this.lts || []).forEach(clearTimeout); }
  renderVals() {
    const d = this.state.d, lp = this.state.lp, loaded = lp >= 3;
    const c = (x) => Math.max(0, Math.min(1, x));
    const sm = (x) => { x = c(x); return x * x * (3 - 2 * x); };
    const S = (a, b) => sm((d - a) / (b - a));
    const lin = (a, b) => c((d - a) / (b - a));
    const f3 = (x) => (+x).toFixed(3);
    const ph = this.state.ph, live = d >= 1990;
    const Q = 'Why is floor 6 using so much cooling?';
    const seg = (a, b, f0, f1) => f0 + Math.round((f1 - f0) * lin(a, b));

    // ---- the building: weeks 1 plan, 2–4 floors, 5–6 second skeleton layer, 7 finishing, 8 floor 6 lit ----
    let i = 150;
    if (d >= 158) i = 0;
    if (d >= 300) i = seg(300, 420, 0, 22);
    if (d >= 420) i = seg(420, 520, 22, 30);
    if (d >= 520) i = seg(540, 692, 30, 45);
    if (d >= 692) i = seg(692, 792, 45, 58);
    if (d >= 792) i = seg(792, 892, 58, 75);
    if (d >= 892) i = seg(892, 982, 75, 92);
    if (d >= 982) i = seg(982, 1082, 92, 100);
    if (d >= 1082) i = seg(1082, 1182, 100, 108);
    if (d >= 1182) i = seg(1182, 1292, 108, 114);
    if (d >= 1420) i = seg(1420, 1520, 114, 128);
    if (d >= 1520) i = seg(1520, 1580, 128, 140);
    if (d >= 1580) i = seg(1580, 1612, 140, 149);
    if (d >= 1615) i = 150;
    if (d >= 1830) i = 149;
    if (d >= 1925) i = 150;
    if (live) i = ph === 'answer' && this.state.focus === 'f6' ? 150 : 149;
    this.draw(i);

    // camera, in stage units: [scroll, x, y, scale]. The plan starts as the whole background and slowly becomes the building.
    const K = [[0, 31.25, 2.78, 1.12], [140, 31.25, 2.78, 1.12], [158, 0, 4, 1.75], [300, 0, 4, 1.75], [420, 8, 3.5, 1.3], [520, 14, 2.5, 1.08], [692, 12, 2, 1.02],
      [1082, 12, 2, 1.02], [1182, 8, 1.5, 1], [1300, 8, 1.5, 1], [1420, 6, 3.4, 1.06], [1745, 6, 3.4, 1.06], [1810, 29, 2.5, 1.0], [1900, 29, 2.5, 1.0], [1940, 6, 3.4, 1.06]];
    let bx = K[0][1], by = K[0][2], bs = K[0][3];
    for (let j = 0; j < K.length - 1; j++) { const [a, x0, y0, s0] = K[j], [b, x1, y1, s1] = K[j + 1]; if (d >= a && d <= b) { const u = sm((d - a) / (b - a)); bx = x0 + (x1 - x0) * u; by = y0 + (y1 - y0) * u; bs = s0 + (s1 - s0) * u; } }
    if (d > K[K.length - 1][0]) [, bx, by, bs] = K[K.length - 1];
    let bOp = loaded ? 1 : 0;
    if (d >= 140) bOp = 1 - S(140, 158);
    if (d >= 158) bOp = 0.3 * S(158, 195);
    if (d >= 300) bOp = 0.3 + 0.3 * S(300, 420);
    if (d >= 420) bOp = 0.6 + 0.4 * S(420, 480);
    if (d >= 1300) bOp = 1 - 0.8 * S(1300, 1340);
    if (d >= 1420) bOp = 0.2 + 0.1 * S(1420, 1460);
    if (d >= 1520) bOp = 0.3 + 0.7 * S(1520, 1545);
    if (d >= 1925) bOp = 1 - 0.8 * S(1925, 1950);
    if (d >= 1985) bOp = 0.2 + 0.08 * S(1985, 2030);
    if (live && ph !== 'home') bOp = 1;

    // ---- the app, one piece at a time; the whole thing only at the end ----
    let parts = '', mode = 'story', uiOp = 0, chat = '', chart = '', src = '';
    if (d >= 540 && d < 1085) { parts = 'card1,card2,card3'; uiOp = S(545, 600) * (1 - S(985, 1005)); }
    if (d >= 1085 && d < 1185) { parts = 'card2'; chart = '1'; uiOp = S(1088, 1110); }
    if (d >= 1185 && d < 1310) { parts = 'ai'; chat = '1'; chart = '1'; uiOp = 1 - S(1292, 1310); }
    if (d >= 1310 && d < 1520) { mode = 'home'; parts = 'hinput'; uiOp = S(1335, 1365); }
    if (d >= 1520 && d < 1580) { mode = 'loading'; parts = 'scan,ai,input'; uiOp = 1; }
    if (d >= 1580 && d < 1666) { mode = 'answer'; parts = 'ai,input,pin'; uiOp = 1; }
    if (d >= 1666 && d < 1770) { mode = 'answer'; parts = 'ai,pin,card2,src'; src = '1'; uiOp = 1 - S(1742, 1765); }
    if (live) { mode = ph; parts = ''; uiOp = S(1995, 2030); }
    const uiOn = uiOp > 0.001 || (d >= 540 && d < 1770) || live;
    const typed = live ? this.state.q : (d >= 1500 ? Q : Q.slice(0, Math.round(Q.length * lin(1440, 1500))));

    // ---- story text: rises in, holds, rises out; one block at a time ----
    const mv = (a, b) => {
      const p = (d - a) / (b - a);
      if (p <= 0 || p >= 1) return { op: 0, y: p <= 0 ? 1.4 : -1.4 };
      const inn = sm(p / 0.2), out = 1 - sm((p - 0.8) / 0.2);
      return { op: Math.min(inn, out), y: (1 - inn) * 1.4 - (1 - out) * 1.4 };
    };
    const ops = [];
    const st = (a, b) => { const m = mv(a, b); ops.push(m.op); return 'opacity: ' + f3(m.op) + '; transform: translate3d(0, ' + m.y.toFixed(2) + 'cqi, 0)'; };
    const heroOut = S(70, 125);
    const tHero = 'opacity: ' + f3((loaded ? 1 : 0) * (1 - heroOut)) + '; transform: translate3d(0, ' + (loaded ? -1.4 * heroOut : 1.4).toFixed(2) + 'cqi, 0); transition: opacity .8s ease .2s, transform .8s cubic-bezier(.2,.8,.2,1) .2s';
    const tx = { tStrat: st(175, 300), tProb: st(305, 420), tW1: st(430, 520), tDes: st(590, 692), t3d: st(696, 792), tReal: st(796, 892), tMessy: st(896, 982),
      tBuild: st(986, 1082), tBur: st(1088, 1182), tChat: st(1188, 1292), tFlip: st(1320, 1430), tScreen: st(1590, 1664), tSrc: st(1668, 1744),
      tW8: st(1750, 1828), tOut: st(1834, 1922), tMon: st(1928, 1998) };
    const textOp = Math.max(...ops);

    // ---- the monitor: the whole app, in a device, only at the end ----
    const win = S(1995, 2060);
    const wK = 1 - 0.19 * win, SH = 62.5, wDy = 1.3 * win, bz = 0.83;
    const wL = 100 * (1 - wK) / 2, wW = 100 * wK, wH = SH * wK, wT = SH * (1 - wK) / 2 + wDy;

    // ---- week rail: ticks; the week label only while its scene's text is on screen; hidden for the hero and the device ----
    const RE = 1990, N = 44, GAP = 9, cur = c(d / RE) * (N - 1);
    const WK = [[175, 'Week 1', 0], [430, 'Week 1', 0, 'end'], [540, 'Week 2', 1], [696, 'Week 3', 0], [796, 'Week 4', 0], [896, 'Week 5', 0], [1088, 'Week 6', 1], [1420, 'Week 7', 0], [1745, 'Week 8', 1]];
    const tickOf = (x) => Math.round(c(x / RE) * (N - 1));
    let wi = -1; WK.forEach(([a], j) => { if (d >= a) wi = j; });
    const majorTicks = WK.filter((w) => w[2]).map((w) => tickOf(w[0]));
    const ticks = Array.from({ length: N }, (_, j) => { const k = c(1 - Math.abs(j - cur) / 3); const maj = majorTicks.includes(j); return { y: j * GAP + 'px', w: (maj ? 14 : 10) + 16 * k + 'px', o: f3((maj ? 0.34 : 0.2) + 0.6 * k) }; });
    const wk = WK.map(([a, n, maj, sub], j) => ({ n, sub: sub || '', hasSub: !!sub, major: !!maj, cls: maj ? 'r5-w lg5' : 'r5-w r5-minor', y: tickOf(a) * GAP + 'px', o: j === wi ? f3((maj ? 1 : 0.9) * textOp) : '0', x: j === wi ? '0px' : '-8px' }));

    const ROWS = [['001', '8 weeks', 'to build'], ['002', '1 MVP', 'built by'], ['003', '3 people', '']];
    const BAND = ['41.8%', '70.2%', '98.7%', '100%', '100%'];
    const STAGES = ['Just an idea', 'Some designs', 'A product already'];
    const FQ = {}; for (let j = 0; j < 7; j++) { const o = this.state.faq === j; FQ['faqO' + j] = o; FQ['faqE' + j] = o ? 'true' : 'false'; FQ['faqS' + j] = o ? '−' : '+'; FQ['faqT' + j] = () => this.setState({ faq: this.state.faq === j ? -1 : j }); }
    return {
      ...tx, ...FQ, tHero,
      onScroll: this.onScroll, scRef: this.scRef, cvRef: this.cvRef, ovY: lp >= 4 || this.at !== null ? 'auto' : 'hidden',
      ldOn: lp < 4, ldOp: lp >= 3 ? '0' : '1', bandH: BAND[lp] || '100%',
      ldRows: ROWS.map(([cc, n, l], k) => ({ c: cc, n, l, o: lp === k ? '1' : '0', y: (lp > k ? -24 : lp < k ? 24 : 0) + 'px', dl: lp === k ? '.3s' : '0s' })),
      bOp: f3(bOp), bTf: 'translate3d(' + bx.toFixed(2) + 'cqi, ' + by.toFixed(2) + 'cqi, 0) scale(' + bs.toFixed(4) + ')',
      uiOn, uiOp: f3(uiOp), mode, parts, chat, chart, src, fill: f3(d >= 1300 ? 1 : S(800, 870)),
      q: typed, focus: live ? this.state.focus : 'f6', send: this.send, setQ: this.setQ, onKey: this.onKey, pick: this.pick,
      veil: f3(S(425, 455) * (1 - S(500, 525)) + S(1745, 1775) * (1 - S(1810, 1835))),
      callOp: f3(S(1105, 1130) * (1 - S(1170, 1185))),
      hlA: loaded && heroOut < 0.5 ? '100%' : '0%', hlB: mv(1320, 1430).op > 0.6 ? '100%' : '0%',
      tTry: 'opacity: ' + f3(S(2040, 2070)),
      scrBg: win > 0.001 ? 'linear-gradient(180deg, #E4E7EB 0%, #DFE2E6 60%, #E3E6EA 100%)' : 'transparent', winDim: f3(win), winTf: win > 0.001 ? 'translate3d(0, ' + wDy.toFixed(3) + 'cqi, 0) scale(' + wK.toFixed(4) + ')' : 'none',
      winClip: win > 0.001 ? 'inset(0 round ' + (1.4 / wK).toFixed(2) + 'cqi)' : 'none',
      monShell: 'opacity: ' + f3(win) + '; left: ' + (wL - bz).toFixed(3) + 'cqi; width: ' + (wW + 2 * bz).toFixed(3) + 'cqi; top: ' + (wT - bz).toFixed(3) + 'cqi; height: ' + (wH + 2 * bz).toFixed(3) + 'cqi;',
      pct: this.state.pct, pctW: this.state.pct + '%', pgOp: loaded && !this.after && win < 0.5 ? '1' : '0',
      railOp: f3(S(150, 185) * (1 - S(1975, 1995))), railH: (N - 1) * GAP + 'px', ticks, wk,
      sent: this.state.sent, notSent: !this.state.sent,
      what: this.state.what ?? '', setWhat: (e) => this.setState({ what: e.target.value }),
      submit: (e) => { e.preventDefault(); this.setState({ sent: true }); },
      stages: STAGES.map((t, j) => ({ t, cls: 'chip6' + (this.state.stage === j ? ' on' : ''), pick: () => this.setState({ stage: j }) })),
    };
  }
}'''
js = JS.replace('__IDS__', json.dumps(IDS)).replace('__END__', str(END))
open(P + 'Proto6.dc.html', 'w').write(TPL.replace('__JS__', js))
print('ok')
