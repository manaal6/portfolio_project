import streamlit as st

def skills_section():
    st.markdown('''
<div id="skills" style="padding:5rem 5vw;scroll-margin-top:80px;position:relative;z-index:1;">
    <h2 style="font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:700;color:#f0f0f0;margin-bottom:2.5rem;letter-spacing:-.02em;">🛠 Skills</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.07);border-radius:14px;overflow:hidden;">
        <div style="background:#0f0f0f;padding:1.8rem;">
            <div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:#f39c12;font-weight:600;margin-bottom:.8rem;">Programming</div>
            <div style="color:#888;font-size:.9rem;line-height:1.7;font-weight:300;">C &nbsp;·&nbsp; C++ &nbsp;·&nbsp; Python</div>
        </div>
        <div style="background:#0f0f0f;padding:1.8rem;">
            <div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:#f39c12;font-weight:600;margin-bottom:.8rem;">Cloud &amp; Tools</div>
            <div style="color:#888;font-size:.9rem;line-height:1.7;font-weight:300;">Azure &nbsp;·&nbsp; Linux &nbsp;·&nbsp; Git &nbsp;·&nbsp; Docker</div>
        </div>
        <div style="background:#0f0f0f;padding:1.8rem;">
            <div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:#f39c12;font-weight:600;margin-bottom:.8rem;">AR/XR Development</div>
            <div style="color:#888;font-size:.9rem;line-height:1.7;font-weight:300;">Unity &nbsp;·&nbsp; ARCore &nbsp;·&nbsp; ARKit</div>
        </div>
        <div style="background:#0f0f0f;padding:1.8rem;">
            <div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:#f39c12;font-weight:600;margin-bottom:.8rem;">Design</div>
            <div style="color:#888;font-size:.9rem;line-height:1.7;font-weight:300;">Adobe Photoshop &nbsp;·&nbsp; CorelDraw &nbsp;·&nbsp; Canva</div>
        </div>
        <div style="background:#0f0f0f;padding:1.8rem;">
            <div style="font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:#f39c12;font-weight:600;margin-bottom:.8rem;">Other</div>
            <div style="color:#888;font-size:.9rem;line-height:1.7;font-weight:300;">SQL &nbsp;·&nbsp; Raspberry Pi &nbsp;·&nbsp; PowerShell &nbsp;·&nbsp; CMD</div>
        </div>
    </div>
</div>
<hr style="border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.07) 20%,rgba(255,255,255,0.07) 80%,transparent);margin:0;">
''', unsafe_allow_html=True)
