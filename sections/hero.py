import streamlit as st

def hero_section():
    st.markdown('''
<section id="about" style="position:relative;padding:7rem 5vw 6rem;overflow:hidden;">
    <div class="hero-wrapper" style="position:relative;max-width:1200px;">
        <div class="hero-tag" style="display:inline-flex;align-items:center;gap:.5rem;font-size:.8rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:#f39c12;background:rgba(243,156,18,0.12);border:1px solid rgba(243,156,18,0.2);padding:.35rem .9rem;border-radius:30px;margin-bottom:1.5rem;">&#9658; Cloud &amp; Embedded Systems Enthusiast</div>
        <h1 class="hero-name" style="font-family:'Syne',sans-serif;font-size:clamp(3rem,7vw,6.5rem);font-weight:800;line-height:1.0;margin-bottom:1.2rem;letter-spacing:-.03em;color:#f0f0f0;">Manaal<br><span style="color:#f39c12;">Pervaiz</span></h1>
        <p class="hero-subtitle" style="font-size:1rem;color:#888;font-weight:300;letter-spacing:.06em;text-transform:uppercase;margin-bottom:1.5rem;">
            Embedded Systems <span style="color:#f39c12;margin:0 .4rem;font-size:.5rem;vertical-align:middle;">&#9679;</span>
            Cloud <span style="color:#f39c12;margin:0 .4rem;font-size:.5rem;vertical-align:middle;">&#9679;</span>
            AI <span style="color:#f39c12;margin:0 .4rem;font-size:.5rem;vertical-align:middle;">&#9679;</span>
            FPGA
        </p>
        <p class="hero-bio" style="max-width:540px;color:#aaa;font-size:1rem;line-height:1.8;margin-bottom:2.5rem;font-weight:300;">
            I’m Manaal Pervaiz, an Embedded Systems & AI enthusiast with hands-on experience in IoT, cloud, AR/XR, and AI projects. Skilled in Python, C/C++, graphics design, and cloud technologies, I love turning ideas into functional, interactive applications. Open to opportunities and passionate about creating impactful tech solutions.
        </p>
        <div class="hero-cta" style="display:flex;gap:1rem;flex-wrap:wrap;">
            <a href="mailto:manaalpervaiz6@gmail.com" class="btn-primary" style="display:inline-flex;align-items:center;gap:.5rem;padding:.8rem 1.8rem;border-radius:8px;font-weight:600;font-size:.9rem;text-decoration:none;background:#f39c12;color:#0a0a0a;box-shadow:0 0 30px rgba(243,156,18,0.35);">&#9993; Get In Touch</a>
            <a href="https://www.linkedin.com/in/manaalpervaiz/" target="_blank" class="btn-secondary" style="display:inline-flex;align-items:center;gap:.5rem;padding:.8rem 1.8rem;border-radius:8px;font-weight:600;font-size:.9rem;text-decoration:none;background:transparent;color:#f39c12;border:1px solid rgba(243,156,18,0.4);">&#128279; LinkedIn</a>
        </div>
    </div>
</section>
<hr style="border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.07) 20%,rgba(255,255,255,0.07) 80%,transparent);margin:0;">
''', unsafe_allow_html=True)
