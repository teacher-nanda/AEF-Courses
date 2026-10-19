/* ===================== JOB INTERVIEW COURSE ENGINE ===================== */
/* ---- LEVEL SWITCH (Support / Standard / Challenge) ---- */
var LV_KEY = 'jic::level';
function setLevel(l){
  document.body.classList.remove('lv-support','lv-standard','lv-challenge');
  document.body.classList.add('lv-'+l);
  try{ localStorage.setItem(LV_KEY, l); }catch(e){}
  document.querySelectorAll('[data-lv]').forEach(function(b){ b.classList.toggle('on', b.dataset.lv === l); });
}
(function(){ var l='standard'; try{ l = localStorage.getItem(LV_KEY) || 'standard'; }catch(e){} setLevel(l); })();

/* ---- FLAG SORT: each card gets one of two answers ---- */
function fsPick(btn, key){
  var card = btn.closest('.fs-card');
  card.dataset.pick = key;
  card.classList.remove('ok','bad','empty-warn');
  card.querySelectorAll('.fs-btn').forEach(function(b){ b.classList.toggle('sel', b === btn); });
}
function fsCheck(id){
  document.querySelectorAll('#'+id+' .fs-card').forEach(function(c){
    c.classList.remove('ok','bad','empty-warn');
    if (!c.dataset.pick){ c.classList.add('empty-warn'); return; }
    c.classList.add(c.dataset.pick === c.dataset.ans ? 'ok' : 'bad');
  });
}
function fsReset(id){
  document.querySelectorAll('#'+id+' .fs-card').forEach(function(c){
    c.classList.remove('ok','bad','empty-warn'); delete c.dataset.pick;
    c.querySelectorAll('.fs-btn').forEach(function(b){ b.classList.remove('sel'); });
  });
}

/* ---- MULTI PICK: tick every option that fits ---- */
function mpToggle(el){ el.classList.remove('ok','bad'); el.classList.toggle('picked'); }
function mpCheck(id){
  document.querySelectorAll('#'+id+' .mp-opt').forEach(function(o){
    o.classList.remove('ok','bad');
    if (o.classList.contains('picked')) o.classList.add(o.dataset.correct === '1' ? 'ok' : 'bad');
  });
}
function mpReset(id){ document.querySelectorAll('#'+id+' .mp-opt').forEach(function(o){ o.classList.remove('picked','ok','bad'); }); }

/* ---- ORDER CHIPS: click to place into the next empty slot ---- */
function ogClick(chip){
  var og = chip.closest('.og');
  var inSlot = chip.parentNode.classList.contains('og-slot');
  og.classList.remove('checked');
  chip.classList.remove('ok','bad');
  if (inSlot){ chip.parentNode.classList.remove('filled'); og.querySelector('.og-pool').appendChild(chip); return; }
  var slots = og.querySelectorAll('.og-slot');
  for (var i=0;i<slots.length;i++){
    if (!slots[i].querySelector('.og-chip')){ slots[i].appendChild(chip); slots[i].classList.add('filled'); return; }
  }
}
function ogCheck(id){
  document.querySelectorAll('#'+id+' .og-slot').forEach(function(s, i){
    var c = s.querySelector('.og-chip'); if (!c) return;
    c.classList.remove('ok','bad');
    c.classList.add(parseInt(c.dataset.i,10) === i ? 'ok' : 'bad');
  });
}
function ogReset(id){
  var og = document.getElementById(id), pool = og.querySelector('.og-pool');
  og.querySelectorAll('.og-slot').forEach(function(s){
    var c = s.querySelector('.og-chip'); if (c){ c.classList.remove('ok','bad'); pool.appendChild(c); } s.classList.remove('filled');
  });
}

/* ---- BUCKETS: pick a chip, then pick the bucket ---- */
var bkSel = null;
function bkChip(chip){
  if (bkSel) bkSel.classList.remove('sel');
  chip.classList.remove('ok','bad');
  bkSel = chip; chip.classList.add('sel');
}
function bkPut(bucket){
  if (!bkSel) return;
  bucket.querySelector('.bk-drop').appendChild(bkSel);
  bkSel.classList.remove('sel','ok','bad'); bkSel = null;
}
function bkCheck(id){
  var box = document.getElementById(id);
  box.querySelectorAll('.bk-chip').forEach(function(c){
    c.classList.remove('ok','bad');
    var b = c.closest('.bk-b'); if (!b) return;
    c.classList.add(b.dataset.b === c.dataset.ans ? 'ok' : 'bad');
  });
}
function bkReset(id){
  var box = document.getElementById(id), pool = box.querySelector('.bk-pool');
  box.querySelectorAll('.bk-chip').forEach(function(c){ c.classList.remove('ok','bad','sel'); pool.appendChild(c); });
  bkSel = null;
}

/* ---- TIMER ---- */
var tmHandles = {};
function tmBeep(){ try{ var C = new (window.AudioContext||window.webkitAudioContext)(); var o=C.createOscillator(), g=C.createGain(); o.connect(g); g.connect(C.destination); o.frequency.value=880; g.gain.value=.15; o.start(); setTimeout(function(){ o.stop(); C.close(); }, 450); }catch(e){} }
function tmStart(btn){
  var box = btn.closest('.tm'), d = box.querySelector('.tm-d'), id = box.id;
  if (tmHandles[id]){ clearInterval(tmHandles[id]); tmHandles[id]=null; btn.textContent='▶ Start'; return; }
  var left = parseInt(box.dataset.left || box.dataset.sec, 10);
  if (left <= 0) left = parseInt(box.dataset.sec,10);
  btn.textContent = '⏸ Pause'; box.classList.remove('done');
  tmHandles[id] = setInterval(function(){
    left--; box.dataset.left = left; d.textContent = left;
    if (left <= 0){ clearInterval(tmHandles[id]); tmHandles[id]=null; btn.textContent='▶ Start again'; d.textContent="Time's up!"; box.classList.add('done'); tmBeep(); }
  }, 1000);
}
function tmReset(btn){
  var box = btn.closest('.tm'); clearInterval(tmHandles[box.id]); tmHandles[box.id]=null;
  box.dataset.left = box.dataset.sec; box.querySelector('.tm-d').textContent = box.dataset.sec; box.classList.remove('done');
  box.querySelector('.tm-go').textContent = '▶ Start';
}

/* ---- ROULETTE ---- */
var RL = {};
function rlNext(id){
  var list = RL[id], box = document.getElementById(id);
  var n = nextNoRepeat('rl-'+id, list.length);
  box.querySelector('.rl-q').textContent = list[n][0];
  var f = box.querySelector('.rl-f'); if (f) f.textContent = list[n][1] || '';
  box.classList.add('spun');
}

/* ---- BRANCHING SCENARIO ---- */
function brPick(btn){
  var br = btn.closest('.br');
  br.querySelectorAll('.br-opt').forEach(function(b){ b.classList.remove('sel'); });
  btn.classList.add('sel');
  var fb = br.querySelector('.br-fb');
  fb.className = 'br-fb show ' + btn.dataset.rate;
  fb.innerHTML = btn.dataset.fb;
}

/* ---- ANSWER BUILDER + INTERVIEW NOTEBOOK ---- */
var AB_KEY = 'jic::ans';
function abLoad(){ try{ return JSON.parse(localStorage.getItem(AB_KEY)) || {}; }catch(e){ return {}; } }
function abSave(o){ try{ localStorage.setItem(AB_KEY, JSON.stringify(o)); }catch(e){} }
function abStepsKey(ab){ return 'jic::in::' + ab.dataset.key; }
function abBuild(btn){
  var ab = btn.closest('.ab'), parts = [];
  ab.querySelectorAll('.ab-in').forEach(function(t){ var v = t.value.trim(); if (v) parts.push(v); });
  var out = ab.querySelector('.ab-out');
  if (!parts.length){ out.innerHTML = '<span class="ab-warn">Write at least one part first.</span>'; out.classList.add('show'); return; }
  var text = parts.join(' ');
  var all = abLoad(); all[ab.dataset.key] = {title: ab.dataset.title, text: text, lesson: document.body.dataset.lesson || '', order: ab.dataset.order || ab.dataset.key};
  abSave(all);
  out.innerHTML = '<b>Your answer</b><p>' + text.replace(/</g,'&lt;') + '</p><span class="ab-ok">✓ Saved to your Interview Notebook</span>';
  out.classList.add('show');
}
function abClear(btn){
  var ab = btn.closest('.ab');
  ab.querySelectorAll('.ab-in').forEach(function(t){ t.value=''; });
  try{ localStorage.removeItem(abStepsKey(ab)); }catch(e){}
  var all = abLoad(); delete all[ab.dataset.key]; abSave(all);
  var out = ab.querySelector('.ab-out'); out.classList.remove('show'); out.innerHTML='';
}
document.querySelectorAll('.ab').forEach(function(ab){
  var saved = null; try{ saved = JSON.parse(localStorage.getItem(abStepsKey(ab))); }catch(e){}
  ab.querySelectorAll('.ab-in').forEach(function(t, i){
    if (saved && saved[i]) t.value = saved[i];
    t.addEventListener('input', function(){
      var vals = []; ab.querySelectorAll('.ab-in').forEach(function(x){ vals.push(x.value); });
      try{ localStorage.setItem(abStepsKey(ab), JSON.stringify(vals)); }catch(e){}
    });
  });
});
function openNotebook(){
  var all = abLoad(), keys = Object.keys(all).sort(function(a,b){ return String(all[a].order).localeCompare(String(all[b].order)); });
  if (!keys.length){ alert('Your Interview Notebook is empty. Build an answer in a lesson first!'); return; }
  var win = window.open('', '_blank'), cards = '';
  keys.forEach(function(k){ var a = all[k]; cards += '<div class="c"><div class="h">'+a.lesson+' · '+a.title+'</div><p>'+String(a.text).replace(/</g,'&lt;')+'</p></div>'; });
  var today = new Date().toLocaleDateString('en-US',{weekday:'long',year:'numeric',month:'long',day:'numeric'});
  win.document.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>My Interview Notebook</title><style>'+
    'body{font-family:"DM Sans","Segoe UI",sans-serif;max-width:800px;margin:0 auto;padding:0 0 30px;color:#1C2B3A}'+
    '.hero{background:linear-gradient(135deg,#12324A,#1B6E96);color:#fff;padding:32px 34px;border-radius:0 0 24px 24px}'+
    '.hero small{letter-spacing:.2em;text-transform:uppercase;color:#FFD84D;font-weight:800}.hero h1{margin:6px 0 4px;font-size:2.1rem}.hero p{margin:0;opacity:.9}'+
    '.tip{margin:22px 28px;background:#FFF8E1;border:3px solid #FFD84D;border-radius:18px;padding:14px 20px;font-size:1.02rem;line-height:1.6}'+
    '.c{margin:0 28px 16px;border:1px solid #D5DEE5;border-radius:12px;overflow:hidden;break-inside:avoid}.h{background:#12324A;color:#fff;padding:8px 14px;font-weight:700}'+
    '.c p{margin:0;padding:12px 16px;line-height:1.75;font-size:1.05rem}*{print-color-adjust:exact;-webkit-print-color-adjust:exact}</style></head><body>'+
    '<div class="hero"><small>Conversational English with teacher Nanda</small><h1>🎤 My Interview Notebook</h1><p>'+today+'</p></div>'+
    '<div class="tip"><b>How to use this page:</b> read each answer out loud. Then say it again without looking, in your own words. Practice a little every day!</div>'+cards+'</body></html>');
  win.document.close(); setTimeout(function(){ win.print(); }, 600);
}

/* ---- course map ---- */
function mapPick(btn){
  var box = btn.closest('.mapwrap');
  box.querySelectorAll('.maptile').forEach(function(b){ b.classList.remove('on'); });
  btn.classList.add('on');
  box.querySelector('.mapinfo').innerHTML = btn.dataset.info;
}
/* ---- tick list ---- */
function tickToggle(el){ el.classList.toggle('picked'); }
