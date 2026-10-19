# -*- coding: utf-8 -*-
import sys, os, json, re, importlib
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
SH=os.path.join(HERE,'shared'); OUT=os.path.dirname(HERE)
BASEURL='https://teacher-nanda.github.io/AEF-Courses/Job-Interview-B2/'
def rd(p): return open(p,encoding='utf-8').read()

def build(mod):
    M=importlib.import_module('lessons.'+mod); L=M.L
    ids=[s[0] for s in L.S]; labels=[s[1] for s in L.S]
    assert len(set(ids))==len(ids), 'duplicate ids'
    name='Job Interview %d — %s' % (L.num, re.sub('<[^>]+>','',L.title+' '+L.accent).replace('  ',' '))
    lesson_name=re.sub('<[^>]+>',' ',L.title+' '+L.accent); lesson_name=' '.join(lesson_name.split())
    url=BASEURL+L.slug+'/index.html'
    fonts=M.FONTS
    css=rd(SH+'/base.css').replace('AEF4 4B \\2014  A Risky Business','Job Interview %d \\2014  %s' % (L.num, lesson_name))
    css+='\n'+rd(SH+'/engine.css')+'\n'+M.THEME
    chrome=rd(SH+'/chrome.html')+'''
<div id="lvBar"><button data-lv="support" onclick="setLevel('support')">🌱 Support</button><button data-lv="standard" onclick="setLevel('standard')">🎯 Standard</button><button data-lv="challenge" onclick="setLevel('challenge')">🔥 Challenge</button></div>'''
    nav=rd(SH+'/nav.html').replace('<button onclick="this.blur();clearAllNotes()"','<button onclick="openNotebook()" style="margin-left:6px;padding:5px 12px;background:#1F7A5A;color:#fff;border:none;border-radius:7px;font-size:.82rem;cursor:pointer;font-family:inherit;">📓 Notebook</button>\n  <button onclick="this.blur();clearAllNotes()"')
    jsn=rd(SH+'/js_nav.js'); jsg=rd(SH+'/js_generic.js')
    jsg=jsg.replace("function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; }","function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; try{ localStorage.setItem(notesStoreKey, JSON.stringify(notesData)); }catch(e){} }")
    eng=rd(SH+'/engine.js'); pdf=rd(SH+'/js_pdf.js').replace('__LESSON_NAME__',lesson_name).replace('__URL__',url)
    slides_html='\n\n'.join(s[2] for s in L.S)
    html='<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>%s</title>\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?%s&display=swap" rel="stylesheet">\n<style>\n%s\n</style>\n</head>\n<body data-lesson="Lesson %d">\n%s\n<div id="deck">\n\n%s\n\n</div><!-- END #deck -->\n\n%s\n<script>\n/* ===== SLIDE NAV DATA ===== */\nvar slideIds = %s;\nvar slideLabels = %s;\n%s\n%s\n%s\n%s\n%s\n</script>\n</body>\n</html>\n' % (
        name, fonts, css, L.num, chrome, slides_html, nav, json.dumps(ids), json.dumps(labels,ensure_ascii=False), jsn, jsg, eng, L.js, pdf)
    d=os.path.join(OUT,L.slug); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(html)
    print(L.slug, len(L.S),'slides', len(html),'bytes')

if __name__=='__main__':
    for m in (sys.argv[1:] or ['L1','L2','L3','L4','L5']): build(m)
