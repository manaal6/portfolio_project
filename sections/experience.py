import streamlit as st
import streamlit.components.v1 as components

def experience_section():
    # External anchor for the main page navigation
    st.markdown('<div id="experience" style="scroll-margin-top: 100px;"></div>', unsafe_allow_html=True)
    
    components.html("""
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400&display=swap" rel="stylesheet">
<style>
  body { margin:0; padding:0; background:#080808; font-family:'DM Sans',sans-serif; overflow:hidden; }
  .wrap { padding:3rem 5vw; }
  h2 { font-family:'Syne',sans-serif; font-size:2.2rem; font-weight:700; color:#f0f0f0; margin:0 0 2.5rem; letter-spacing:-.02em; }
  .timeline { border-left:1px solid rgba(255,255,255,0.07); padding-left:2rem; margin-left:.5rem; }
  .item { position:relative; padding:1rem 0 2rem; }
  .dot { position:absolute; left:-2.4rem; top:1.4rem; width:10px; height:10px; border-radius:50%; background:#f39c12; box-shadow:0 0 12px rgba(243,156,18,0.5); border:2px solid #080808; }
  .role { font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#f0f0f0; margin-bottom:.2rem; }
  .org  { font-size:.8rem; color:#f39c12; font-weight:500; letter-spacing:.04em; text-transform:uppercase; margin-bottom:.6rem; }
  .desc { font-size:.875rem; color:#888; line-height:1.7; font-weight:300; max-width:700px; }
</style>
</head>
<body>
<div class="wrap">
  <h2>💼 Experience</h2>
  <div class="timeline">
    <div class="item"><div class="dot"></div>
      <div class="role">Digital Presence Manager</div>
      <div class="org">enARtifi &amp; Brain Creatives</div>
      <div class="desc">Achieved 300% growth in brand reach through digital campaigns, trained AR developer interns, and supported peer startups.</div>
    </div>
    <div class="item"><div class="dot"></div>
      <div class="role">Social Media Manager</div>
      <div class="org">ZUNF Medicare</div>
      <div class="desc">Managed content, campaigns, and social media strategy for brand awareness.</div>
    </div>
    <div class="item"><div class="dot"></div>
      <div class="role">Digital Presence Manager</div>
      <div class="org">Brain Creative</div>
      <div class="desc">Visiting schools across Pakistan for behavioral analysis, providing counseling, and opening a skill-based institute focusing on children's mental health.</div>
    </div>
    <div class="item"><div class="dot"></div>
      <div class="role">Business Development Executive</div>
      <div class="org">Lojics</div>
      <div class="desc">Managed client communication and identified IT business opportunities.</div>
    </div>
    <div class="item"><div class="dot"></div>
      <div class="role">WordPress Developer</div>
      <div class="org">DS Trainings</div>
      <div class="desc">Developed training website with certificate verification system.</div>
    </div>
    <div class="item"><div class="dot"></div>
      <div class="role">Graphics Designer</div>
      <div class="org">ZUNF Medicare</div>
      <div class="desc">Maintained brand consistency, UI/UX design, and promotional graphics.</div>
    </div>
  </div>
</div>
</body>
</html>
""", height=850, scrolling=False)