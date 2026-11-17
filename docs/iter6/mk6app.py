P='canvas/root/project/'
s=open(P+'I4App.dc.html').read()
def rep(a,b,n=1):
    global s
    c=s.count(a); assert c>=(1 if n=='all' else n), (a[:80],c)
    s=s.replace(a,b) if n=='all' else s.replace(a,b,n)
rep('<title>ConnectX UI, new theme</title>','<title>ConnectX UI · iteration 6 polish</title>')
rep('href="i4.css"','href="i6app.css"')
# assistant + input column: on the 8px grid, 16px from the right rail, 16px between the two cards, hidden when the dashboard has no AI yet
rep('left: 66.4cqi; top: 10cqi; width: 26.4cqi; display: flex; flex-direction: column; gap: .5cqi; opacity: {{a2}};','left: 66.9cqi; top: 10cqi; width: 26.4cqi; display: flex; flex-direction: column; gap: 1.11cqi; opacity: {{a2c}};')
rep('padding: 1.9cqi; display: flex; flex-direction: column; gap: 1.6cqi; animation: {{aiAnim}};','padding: 1.67cqi; display: flex; flex-direction: column; gap: 1.11cqi; animation: {{aiAnim}};')
rep('padding: 1.7cqi 1.9cqi 1.9cqi; display: flex; flex-direction: column; gap: 1.4cqi;','padding: 1.39cqi 1.67cqi 1.67cqi; display: flex; flex-direction: column; gap: 1.11cqi;')
rep('padding: 1.7cqi 1.9cqi; height: 12.4cqi; display: flex; flex-direction: column; gap: 1.3cqi;','padding: 1.67cqi; height: 11.67cqi; display: flex; flex-direction: column; gap: 1.11cqi;',3)
rep('grid-template-columns: 1fr 1.08fr 1fr; gap: 1.2cqi;','grid-template-columns: 1fr 1.08fr 1fr; gap: 1.11cqi;')
rep('padding-bottom: 1.1cqi; border-bottom: .08cqi solid var(--hair);"><span style="display: flex; flex-direction: column; gap: .35cqi;"><b style="font-size: 1.2cqi;','padding-bottom: 1.11cqi; border-bottom: .07cqi solid var(--hair);"><span style="display: flex; flex-direction: column; gap: .28cqi;"><b style="font-size: 1.2cqi;','all')
rep('padding-bottom: 1.4cqi; border-bottom: .08cqi solid var(--hair);','padding-bottom: 1.11cqi; border-bottom: .07cqi solid var(--hair);')
# chat box state (the 'before'): a paragraph answer in the assistant card
rep('      <sc-if value="{{showSteps}}"','''      <sc-if value="{{showChat}}" hint-placeholder-val="{{ false }}">
        <div style="display: flex; flex-direction: column; gap: 1.11cqi;">
          <span style="align-self: flex-end; max-width: 86%; background: var(--surface-2); border-radius: var(--r-in) var(--r-in) .3cqi var(--r-in); padding: .83cqi 1.11cqi; font-size: 1.05cqi; line-height: 1.45;">Why is floor 6 using so much cooling?</span>
          <span style="display: flex; flex-direction: column; gap: .55cqi;"><span class="lab4">Assistant</span><span style="font-size: 1.05cqi; line-height: 1.6; color: var(--ink2);">Cooling on floor 6 has been higher than expected in recent afternoons. This could be due to occupancy patterns, HVAC scheduling, solar gain through the west façade or equipment efficiency. You may want to review the HVAC schedule, check the floor’s sensors and compare it with…</span></span>
        </div>
      </sc-if>
      <sc-if value="{{showSteps}}"''')
# cost card: optional chart where floor 6 is one small tick among everything else
rep('''      <sc-if value="{{hasData}}" hint-placeholder-val="{{ true }}">
        <div style="display: flex; gap: 1.6cqi; align-items: center;">''','''      <sc-if value="{{showChart}}" hint-placeholder-val="{{ false }}">
        <svg viewBox="0 0 400 70" preserveAspectRatio="none" style="width: 100%; height: 4.6cqi; display: block;" aria-label="Cost through the day, floor 6 is one small spike">
          <path d="M0 62 L40 58 L80 60 L120 50 L160 54 L200 44 L240 47 L270 36 L300 40 L330 30 L360 34 L400 22" fill="none" stroke="#9AA1AB" stroke-width="2" vector-effect="non-scaling-stroke"></path>
          <path d="M296 41 L312 31" fill="none" stroke="#D84A3B" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
          <path d="M0 69 L400 69" stroke="rgba(15,25,40,.12)" stroke-width="1" vector-effect="non-scaling-stroke"></path>
        </svg>
      </sc-if>
      <sc-if value="{{showNums}}" hint-placeholder-val="{{ true }}">
        <div style="display: flex; gap: 1.6cqi; align-items: center;">''')
# source popover over the 16 kW figure
rep('  <!-- answer pin -->','''  <sc-if value="{{showSrc}}" hint-placeholder-val="{{ false }}">
    <div class="c4 src6" style="left: 34.4cqi; top: 35cqi; width: 22.2cqi; padding: 1.39cqi 1.67cqi; display: flex; flex-direction: column; gap: .83cqi; z-index: 5;">
      <span class="lab4" style="display: flex; align-items: center; gap: .55cqi;"><span class="dot4"></span>Source</span>
      <b style="font-size: 1.2cqi; font-weight: 500;">16 kW · meter F6-AHU-2</b>
      <span style="font-size: .97cqi; line-height: 1.5; color: var(--ink2);">Read at 10:45 today. Floor 6 air handler, west side.</span>
      <span style="font-size: .97cqi; font-weight: 600; color: var(--green);">Open the meter data →</span>
    </div>
  </sc-if>
  <!-- answer pin -->''')
rep("    return {\n","    const noai = Math.max(0, Math.min(1, +(P.noai || 0))), chat = P.chat === '1' || P.chat === 1, chart = P.chart === '1' || P.chart === 1;\n    return {\n      a2c: home ? 0 : (a2 * (1 - noai)).toFixed(3), a2cx: ((1 - a2 * (1 - noai)) * 6).toFixed(2) + 'cqi', showChat: chat, showChart: chart, showSrc: (P.src === '1' || P.src === 1) && mode === 'answer',\n")
rep("showTiles: mode === 'story' || mode === 'home',","showTiles: (mode === 'story' && !chat) || mode === 'home',")
rep("hasData: (mode === 'story' && fill > 0.02) || mode === 'answer',","hasData: (mode === 'story' && fill > 0.02) || mode === 'answer', showNums: ((mode === 'story' && fill > 0.02) || mode === 'answer') && !chart,")
# new props in the editor list
rep('"focus":{"editor":"enum"','"noai":{"editor":"text","default":""},"notitle":{"editor":"text","default":""},"chat":{"editor":"text","default":""},"chart":{"editor":"text","default":""},"src":{"editor":"text","default":""},"focus":{"editor":"enum"')
rep("titleOp: home ? 0 : 1,","titleOp: (home || P.notitle === '1' || P.notitle === 1) ? 0 : 1,")
rep("gap: 1.11cqi; opacity: {{a2c}}; transform: translateX({{a2x}});","gap: 1.11cqi; opacity: {{a2c}}; transform: translateX({{a2cx}});")

# ---- parts: show single pieces of the app for the story (empty = everything) ----
T6='; transition: opacity .5s ease'
rep('<div class="scan5" aria-hidden="true">','<div class="scan5" aria-hidden="true" style="opacity: {{oScan}}'+T6+';">')
rep('top: 2.2cqi; height: 3.6cqi; display: flex; align-items: center; justify-content: space-between; opacity: {{a1}};','top: 2.2cqi; height: 3.6cqi; display: flex; align-items: center; justify-content: space-between; opacity: {{oTop}};')
rep('<span class="ib4" style="position: absolute; left: var(--gut); top: 10cqi;">','<span class="ib4" style="position: absolute; left: var(--gut); top: 10cqi; opacity: {{oLeft}}'+T6+';">')
rep('<div style="position: absolute; left: var(--gut); top: 21.6cqi; display: flex; flex-direction: column; gap: 1.2cqi;">','<div style="position: absolute; left: var(--gut); top: 21.6cqi; display: flex; flex-direction: column; gap: 1.2cqi; opacity: {{oLeft}}'+T6+';">')
rep('<div class="c4" style="position: relative; padding: 1.67cqi; display: flex; flex-direction: column; gap: 1.11cqi; animation: {{aiAnim}};">','<div class="c4" style="position: relative; padding: 1.67cqi; display: flex; flex-direction: column; gap: 1.11cqi; animation: {{aiAnim}}; opacity: {{oAI}}'+T6+';">')
rep('<div class="c4" style="position: relative; padding: 1.39cqi 1.67cqi 1.67cqi; display: flex; flex-direction: column; gap: 1.11cqi;">','<div class="c4" style="position: relative; padding: 1.39cqi 1.67cqi 1.67cqi; display: flex; flex-direction: column; gap: 1.11cqi; opacity: {{oIN}}'+T6+';">')
rep('right: var(--gut); top: 21.6cqi; display: flex; flex-direction: column; gap: 1.2cqi; opacity: {{a2}};','right: var(--gut); top: 21.6cqi; display: flex; flex-direction: column; gap: 1.2cqi; opacity: {{oRR}};')
rep('gap: 1.11cqi; opacity: {{a3}};','gap: 1.11cqi; opacity: {{oCards}};')
for k in (1,2,3):
    rep('<div class="c4" style="position: relative; padding: 1.67cqi; height: 11.67cqi; display: flex; flex-direction: column; gap: 1.11cqi;">','<div class="c4" style="position: relative; padding: 1.67cqi; height: 11.67cqi; display: flex; flex-direction: column; gap: 1.11cqi; opacity: {{oC%d}}%s;">'%(k,T6))
rep('<div style="display: flex; flex-direction: column; align-items: center; gap: .9cqi;">','<div style="display: flex; flex-direction: column; align-items: center; gap: .9cqi; opacity: {{oHH}}'+T6+';">')
rep('<div class="c4" style="position: relative; width: 100%; padding: 1.9cqi; display: flex; flex-direction: column; gap: 1.4cqi;">','<div class="c4" style="position: relative; width: 100%; padding: 1.67cqi; display: flex; flex-direction: column; gap: 1.39cqi; opacity: {{oHI}}'+T6+';">')
rep('<div style="display: flex; gap: .5cqi; flex-wrap: wrap; padding-top: 1.3cqi; border-top: .08cqi solid var(--hair);">','<div style="display: flex; gap: .5cqi; flex-wrap: wrap; padding-top: 1.3cqi; border-top: .07cqi solid var(--hair); opacity: {{oCh}}'+T6+';">')
rep('<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .8cqi; width: 100%;">','<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .8cqi; width: 100%; opacity: {{oHB}}'+T6+';">')
rep('<span class="lab4">Modelled from the last 90 days of meter data</span>','<span class="lab4" style="opacity: {{oHB}}'+T6+';">Modelled from the last 90 days of meter data</span>')
rep("    return {\n      a2c:","    const PT = (P.parts || '').split(',').map((x) => x.trim()).filter(Boolean), has = (x) => !PT.length || PT.includes(x), on = (x) => has(x) ? 1 : 0;\n    return {\n      oScan: on('scan'), oTop: (home ? 1 : a1) * on('top'), oLeft: on('left'), oAI: on('ai'), oIN: on('input'), oRR: (home ? 0 : a2) * on('right'), oCards: (home ? 0 : a3), oC1: on('card1'), oC2: on('card2'), oC3: on('card3'), oHH: on('hhead'), oHI: on('hinput'), oCh: on('chips'), oHB: on('hbrief'),\n      a2c:")
rep("titleOp: (home || P.notitle === '1' || P.notitle === 1) ? 0 : 1,","titleOp: (home || P.notitle === '1' || P.notitle === 1 || !has('title')) ? 0 : 1,")
rep("showSrc: (P.src === '1' || P.src === 1) && mode === 'answer',","showSrc: (P.src === '1' || P.src === 1) && mode === 'answer' && has('src'),")
rep("showPin: mode === 'answer',","showPin: mode === 'answer' && has('pin'),")
rep('"noai":{"editor":"text","default":""}','"noai":{"editor":"text","default":""},"parts":{"editor":"text","default":""}')

open(P+'I6App.dc.html','w').write(s)
c=open(P+'i4.css').read()
c=c.replace('/* Iteration 4 theme','/* Iteration 6 app theme (copy of i4.css, polished: 24px card radius, 16px inner radius, 8px spacing grid)\n   Iteration 4 theme',1)
c=c.replace('--r-card: 1.6cqi;','--r-card: 1.67cqi;').replace('--r-in: 1.1cqi;','--r-in: 1.11cqi;')
c+='\n.src6::before { content: ""; position: absolute; left: 3.2cqi; bottom: -1.2cqi; width: .1cqi; height: 1.2cqi; background: rgba(15, 25, 40, .35); }\n'
open(P+'i6app.css','w').write(c)
print('ok')
