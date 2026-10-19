# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,'..')
from lib import *

L = Lesson(1, 'Welcome to the', 'Interview Lab', 'L1')
FONTS = 'family=Fredoka:wght@500;600;700&family=DM+Sans:wght@400;500;700;800'
THEME = theme('#12324A','#1B9AAA','#E6F6F8','#FFD84D',
  'radial-gradient(circle at 25% 20%, #1B6E96 0%, #12324A 60%, #0A1B28 100%)',
  pattern='linear-gradient(rgba(27,154,170,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(27,154,170,.08) 1px,transparent 1px)', patsize='34px 34px')

cover(L, [('🧪','top:10%;left:7%'),('🔬','top:14%;right:8%;animation-delay:-2s'),('⚗️','bottom:24%;left:9%;animation-delay:-4s'),('💼','bottom:26%;right:10%;animation-delay:-1s'),('🎤','top:44%;left:3%;animation-delay:-3s')],
      'Experiment, practice and get ready for the real thing.')

# ---------------- LEAD-IN
L.slide('s-lead','Lead-in – Your last interview','lead','Can you remember your last job interview?',
  '<p class="inst-light">Think about it for a moment. Then tell me your answers. Use each box as a prompt.</p>'
  '<div class="stack">'
  '<div class="ccq-box"><div class="discuss-label">🤔 Why do you think people get nervous in a job interview?</div></div>'
  '<div class="ccq-box"><div class="discuss-label">🧰 What do you usually do to prepare yourself for the interview?</div></div>'
  '<div class="ccq-box"><div class="discuss-label">✅ How do you know you had a good interview?</div></div></div>'
  + sup('Sentence starters:<br>• People get nervous because… (the interviewer, the questions, English…)<br>• Before an interview, I usually… (read about the company, practice answers…)<br>• I know it was good when… ')
  + chal('Now give me a <b>full</b> answer to each question in 20 seconds. Add one real example from your own experience.'))

# ---------------- STORYTELLING
L.slide('s-story','Interview = Storytelling','read','Job interview = storytelling',
  '<div class="twocol"><div>'
  '<div class="tipbox"><h3>🎬 Why stories?</h3>An incredibly useful skill in a job interview is <span class="chip-a">storytelling</span>. '
  'Make sure you have <span class="chip-b">some stories</span> about your professional life that you can share with the interviewer.<br><br>'
  '<b>One story = many purposes.</b> The same story can answer many different questions.</div>'
  + sup('<b>story</b> <span class="pt">história</span> = a short description of something that happened to you.<br><b>interviewer</b> <span class="pt">entrevistador</span> = the person who asks you questions.')
  + '</div><div>'
  '<div class="say-it"><b>My story:</b> the time my colleague and I disagreed on the structure of a project.</div>'
  '<p class="instruction">Which of these questions could I answer with this story? There are 3 in total.</p>'
  + multipick('mp-story',[
     ('How are your teamwork skills?',True),
     ('What is your notice period?',False),
     ('How do you deal with disagreement?',True),
     ('Which software programs can you use?',False),
     ('How do you deal with changes?',True),
     ('Are you willing to relocate?',False)])
  + '</div></div>')

L.slide('s-stories','My story bank','speak','My story bank',
  '<p class="inst-light">Choose <b>three</b> real stories from your professional life. Write only a short title for each one. Tell me a little about each story, too.</p>'
  + ab('L1-stories','My story bank',[
     ('Story 1','A time you worked with a team or a colleague.','Frame: The time I worked with… on…'),
     ('Story 2','A time you solved a problem.','Frame: The time I had to solve…'),
     ('Story 3','A time you were proud of your result.','Frame: The time I finished… successfully.')],'L1-b')
  + chal('For each story, name <b>two different interview questions</b> it could answer.'))

# ---------------- COURSE MAP
def tile(label, info): return '<button class="maptile" data-info="%s" onclick="mapPick(this)">%s</button>' % (q(info), label)
L.slide('s-map','The course map','lead','Our Job Interview Course',
  '<p class="instruction">Click each circle to see what we will practice. Which one do you need most?</p>'
  '<div class="mapwrap"><div class="mapgrid">'
  + tile('Common questions','<b>Practice answers for common interview questions</b><br>• focus on the purpose of each question<br>• know what to say and what not to say<br>• focus on language usage')
  + tile('Situational questions','<b>Practice answers for situational interview questions</b><br>• highlight your soft skills<br>• focus on the purpose of each question<br>• know what to say and what not to say<br>• focus on language usage')
  + tile('CV questions','<b>Practice answers for questions based on your CV</b><br>• focus on personalized questions<br>• know what the interviewer might find interesting from your CV<br>• make sure your strengths stand out')
  + tile('Working on confidence','<b>Feel more comfortable during the job interview</b><br>• tips on how to feel less nervous<br>• be prepared to ask questions as well<br>• understand your limitations, and work with your strengths')
  + tile('Company knowledge','<b>Tips for students</b><br>• review the job description: qualifications, skills, experience<br>• research the company<br>• use LinkedIn: a useful tool for updates on the company')
  + tile('Culture awareness','<b>Tips for students</b><br>• research a bit about the country you are applying in<br>• get tips from people who have been in that situation before<br>• know the main differences between your country and the target one')
  + '</div><div class="mapinfo">👆 Choose a circle.</div></div>'
  '<p class="inst-light" style="margin-top:14px;">In every lesson we also work on: <span class="pill">vocabulary</span><span class="pill">grammar</span><span class="pill">pronunciation</span><span class="pill">connectors</span></p>')

# ---------------- WHY DO THEY ASK
pur = ('<div class="tipbox"><h3>🧠 What the interviewer wants</h3>'
 '<b>a.</b> They want to know if you can meet deadlines and stay productive.<br>'
 '<b>b.</b> They want to see your ambition and how the job fits your career.<br>'
 '<b>c.</b> They want to get to know you as a person and as a professional.<br>'
 '<b>d.</b> They want to see how much you really want this job and this company.<br>'
 '<b>e.</b> They want to understand your self-awareness.<br>'
 '<b>f.</b> They want to know what drives and inspires you at work.</div>')
qs = [('Can you tell me about yourself?','c'),('What are your greatest strengths and weaknesses?','e'),('Why are you interested in this position?','d'),
      ('What motivates you to perform well in your work?','f'),('What are your short-term and long-term career goals?','b'),('How do you prioritize your work and manage your time effectively?','a')]
rows = ['<div class="ex-row"><span class="example-badge">✓</span>%s <span style="color:#1A7A4A;font-weight:800;background:#E3F5EA;padding:1px 9px;border-radius:5px;">%s</span></div>' % (qs[0][0], qs[0][1])]
for i,(t,a) in enumerate(qs[1:],1):
    rows.append('<div class="ex-row"><span class="circ-num">%d</span>%s <input class="ans-input" style="width:56px" type="text" maxlength="1" data-ans="%s" aria-label="purpose %d"></div>' % (i,t,a,i))
L.slide('s-purpose','Why do they ask?','vocab','Why do they ask that?',
  '<p class="instruction">Match each question to what the interviewer wants. Type the letter.</p>'
  '<div class="twocol"><div id="ex-purpose">' + ''.join(rows) + btns("checkSlide('ex-purpose')","resetSlide('ex-purpose')") + '</div><div>' + pur + '</div></div>'
  + sup('<b>self-awareness</b> <span class="pt">autoconhecimento</span> · <b>ambition</b> <span class="pt">ambição</span> · <b>deadline</b> <span class="pt">prazo</span> · <b>drives</b> <span class="pt">motiva / move</span>')
  + chal('Pick one question. Tell me what a <b>bad</b> answer sounds like, and why the interviewer would not like it.'))

# ---------------- TELL ME ABOUT YOURSELF
tell = ['I\'m currently a marketing assistant at a design agency in Brasília, where I manage social media and write client emails.',
        'Before that, I studied communication at university and worked as an intern at a radio station for two years.',
        'Those experiences taught me to work under pressure and to explain ideas clearly.',
        'Now I\'m looking for a role where I can grow into project management, which is why this position interests me.']
L.slide('s-tell','Tell me about yourself','speak','Can you tell me about yourself?',
  '<div class="twocol"><div>'
  '<div class="tipbox"><h3>💡 Tips on how to answer</h3>'
  'This question lets the interviewer <span class="chip-b">get to know you on a personal and professional level</span>.<br><br>'
  'They are looking for a <span class="chip-b">brief summary</span> of your background: relevant experiences, skills and accomplishments.<br><br>'
  'Share <span class="chip-b">information that directly relates to the position</span>.<br><br>'
  'Use a <span class="chip-a">timeline</span> to organize your answer: <b>present → past → future</b>.</div></div><div>'
  '<p class="instruction">A good answer is in the wrong order! Click the sentences to put them in the right order.</p>'
  + ordergame('og-tell', tell, seed=11) + '</div></div>'
  + sup('<b>currently</b> <span class="pt">atualmente</span> · <b>intern</b> <span class="pt">estagiário(a)</span> · <b>work under pressure</b> <span class="pt">trabalhar sob pressão</span> · <b>grow into</b> <span class="pt">crescer até se tornar</span>'))

# ---------------- LANGUAGE
bank = ''.join('<span class="pill">%s</span>' % w for w in ['currently','before that','for','since','hope','looking','graduated','moved'])
L.slide('s-lang','Timeline language','gram','Language for your timeline',
  '<div class="tipbox"><h3>🧭 Present · Past · Future</h3>'
  + chipa('Present') + ' I\'m <b>currently</b> a… / I work as a… &nbsp;&nbsp; '
  + chipb('Past') + ' I <b>graduated</b> in… / I worked as a… <b>for</b> two years / <b>Before that</b>, I… &nbsp;&nbsp; '
  + chipc('Future') + ' I\'m <b>looking</b> for… / I <b>hope</b> to…<br>'
  '<br><b>Present perfect</b> links the past with now: I\'ve worked in sales <span class="chip-a">for</span> four years (how long) · I\'ve been here <span class="chip-a">since</span> 2021 (the starting point).</div>'
  '<p class="instruction">Complete the sentences with the words in the box. Use each word once.</p><p>' + bank + '</p>'
  + gap('ex-lang',[
      ('I\'m','currently','a customer service agent at a telecom company.','now'),
      ('I','graduated','in business administration in 2019.'),
      ('','before that','I worked as an intern at a bank for six months.','Before that,'),
      ('I\'ve worked in sales','for','four years.'),
      ('I\'ve been with this company','since','2021.'),
      ('I\'m','looking','for a role where I can lead small teams.'),
      ('I','hope','to become a team leader in the next three years.'),
      ('In 2022, I','moved','to Lisbon for a new job.')],
      example=('In 2018, I','started','my first job at a hotel.'), width=150)
  + sup('<b>currently</b> atualmente · <b>before that</b> antes disso · <b>graduated</b> me formei · <b>for</b> por (quanto tempo) · <b>since</b> desde (quando) · <b>looking for</b> procurando · <b>hope</b> espero · <b>moved</b> me mudei')
  + chal('Upgrade two sentences with more formal language, for example <i>I\'m seeking a position where…</i> or <i>I aim to…</i>.'))

# ---------------- PITCH
L.slide('s-pitch','60-second pitch','speak','Your 60-second pitch',
  '<p class="instruction">Answer <i>"Can you tell me about yourself?"</i> out loud. Look at the timer, not at your notes!</p>'
  '<div class="twocol"><div>' + timer('tm-pitch', 60) +
  '<div class="sup">Take <b>30 seconds</b> first. Say only two parts: <i>now</i> and <i>next</i>.</div>'
  '<div class="chal">Only <b>45 seconds</b>, and then I will ask one follow-up question about something you mentioned.</div></div>'
  '<div><p class="instruction">Self-check (tick what you did):</p><div class="stack">'
  '<button class="mp-opt" onclick="tickToggle(this)">⏱️ I used a timeline: present, past, future</button>'
  '<button class="mp-opt" onclick="tickToggle(this)">🎯 I talked about things that relate to the job</button>'
  '<button class="mp-opt" onclick="tickToggle(this)">✂️ I kept it brief</button>'
  '<button class="mp-opt" onclick="tickToggle(this)">😊 I sounded calm and confident</button></div></div></div>')

# ---------------- ANSWER BUILDER
L.slide('s-build','Answer builder','speak','Build your own answer',
  '<p class="inst-light">Write your own answer to <b>"Can you tell me about yourself?"</b> in four parts. Then press the button.</p>'
  + ab('L1-tell','Can you tell me about yourself?',[
      ('1 · Right now','What is your job or study now?','Frame: I\'m currently a… at…, where I…'),
      ('2 · Before','What did you do before? Your studies or past jobs.','Frame: Before that, I studied… / I worked as… for…'),
      ('3 · Your strengths','What did you learn? Which skills do you have?','Frame: Those experiences taught me to…'),
      ('4 · Next','What do you want next? Why this job?','Frame: Now I\'m looking for… which is why…')],'L1-a'))

# ---------------- WRAP-UP
L.slide('s-wrap','Lab report','review','Lab report: what did we discover?',
  '<div class="tipbox"><h3>🔬 Today you can…</h3>• explain why <b>one story</b> can answer many questions<br>• say what the interviewer wants with common questions<br>• organize your answer with a <b>timeline</b> (present → past → future)<br>• use <b>currently, before that, for, since</b> in your answer</div>'
  '<p class="instruction">Which one is still difficult for you? Tell me, and we will practice it next time.</p>'
  '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>'
  '<div class="say-it">👀 <b>Next lesson:</b> strengths and weaknesses. Start thinking: what are you really good at?</div>')

# ---------------- HOMEWORK
hwcover(L)
L.slide('hw-1','HW1 – Timeline tenses','hw','Choose the correct option',
  '<p class="instruction">Circle the correct option for each sentence.</p>'
  + mcq('hw1',[
     ('I',['work','have worked','worked'],'have worked','in marketing for five years now.'),
     ('Last year, I',['led','have led','lead'],'led','a big project for a client.'),
     ('I',['work','have worked','worked'],'have worked','at this company since 2020.'),
     ('In 2019, I',['have finished','finished','am finishing'],'finished','my degree.'),
     ('At the moment, I',['lead','led','have led'],'lead','a team of six.'),
     ('I\'d like to',['grow','growing','grew'],'grow','into a management role.'),
     ('Before that, I',['worked','work','have worked'],'worked','in a small bakery for two years.'),
     ('Next year, I hope',['becoming','to become','become'],'to become','a project manager.')],
     example=('I','lived','in Recife when I was a child.')))
L.slide('hw-2','HW2 – Say it','hw','Practice out loud',
  '<p class="instruction">Take your answer from the Answer Builder.</p>'
  '<div class="tipbox"><h3>🎧 Your plan for this week</h3>1. Read your answer out loud <b>three times</b>.<br>2. Record yourself <b>once</b> on your phone and listen to it.<br>3. Tell me one thing you want to improve.</div>'
  + timer('tm-hw', 60) + '<div class="btn-row"><button class="btn-suggest" onclick="openNotebook()">📓 Open my Interview Notebook</button></div>')
