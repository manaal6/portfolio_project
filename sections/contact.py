import streamlit as st
import streamlit.components.v1 as components

def contact_section():
    components.html("""
<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400&display=swap" rel="stylesheet">
<style>
  body { margin:0; padding:0; background:#080808; font-family:'DM Sans',sans-serif; }
  .wrap { padding:5rem 5vw; }
  h2 { font-family:'Syne',sans-serif; font-size:2.2rem; font-weight:700; color:#f0f0f0; margin:0 0 2.5rem; letter-spacing:-.02em; }
  .grid { max-width:500px; display:flex; flex-direction:column; gap:1rem; }
  .card { display:flex; align-items:center; gap:1.2rem; background:#0f0f0f; border:1px solid rgba(255,255,255,0.09); border-radius:8px; padding:1.2rem 1.5rem; text-decoration:none; }
  .icon { width:40px; height:40px; border-radius:8px; background:rgba(243,156,18,0.12); display:flex; align-items:center; justify-content:center; font-size:1.1rem; flex-shrink:0; }
  .lbl { font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:#f39c12; font-weight:600; }
  .val { font-size:.9rem; color:#f0f0f0; font-weight:400; margin-top:.1rem; }
  .footer { text-align:center; padding:2.5rem 0 1rem; border-top:1px solid rgba(255,255,255,0.07); margin-top:3rem; color:#888; font-size:.8rem; }
  .footer span { color:#f39c12; }
</style>
</head>
<body>
<div class="wrap" id="contact">
  <h2>&#x1F4EC; Contact Me</h2>
  <div class="grid">
    <a href="mailto:manaalpervaiz6@gmail.com" class="card">
      <div class="icon">&#9993;</div>
      <div><div class="lbl">Email</div><div class="val">manaalpervaiz6@gmail.com</div></div>
    </a>
    <a href="https://www.linkedin.com/in/manaalpervaiz/" target="_blank" class="card">
      <div class="icon">&#128279;</div>
      <div><div class="lbl">LinkedIn</div><div class="val">Manaal Pervaiz</div></div>
    </a>
    <div class="card">
      <div class="icon">&#128205;</div>
      <div><div class="lbl">Location</div><div class="val">Lahore, Pakistan</div></div>
    </div>
  </div>
  <div class="footer">Crafted with focus by <span>Manaal Pervaiz</span> &middot; 2025</div>
</div>
</body>
</html>
""", height=500, scrolling=False)