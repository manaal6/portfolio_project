import streamlit as st

CARD = "background:#0f0f0f;border:1px solid rgba(255,255,255,0.07);border-radius:14px;padding:2rem;position:relative;overflow:hidden;transition:border-color 0.3s,transform 0.3s;"
# Changed color to #ffffff (white) and increased opacity for better visibility
NUM  = "font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;color:#f39c12;line-height:1;margin-bottom:.5rem;"
TTL  = "font-family:'Syne',sans-serif;font-size:1.05rem;font-weight:700;color:#f0f0f0;margin-bottom:.8rem;"
DSC  = "font-size:.875rem;color:#888;line-height:1.7;font-weight:300;"

projects = [
    ("01", "IoT-Based Smart Parking System", "Designed and developed using sensors and microcontrollers to monitor parking availability in real-time with cloud-based tracking integration."),
    ("02", "Processor Architecture Simulation", "Simulated a basic processor including ALU operations, instruction cycles, and control unit logic to understand core computing systems."),
    ("03", "AI-Based NLP Chatbot", "Built an intelligent chatbot applying NLP concepts for automated user interaction and response handling."),
    ("04", "Cloud Deployment & Containerization", "Containerized applications using Docker and managed backend integration in a cloud environment for deployment."),
    ("05", "AWS Resource Monitoring Automation", "Developed Bash and Python scripts to track EC2, Lambda, IAM users, and S3 with cronjob-based logging for continuous monitoring."),
    ("06", "DC to AC Inverter Circuit", "Designed and tested a DC to AC inverter circuit with waveform analysis to evaluate power conversion efficiency."),
    ("07", "FPGA Digital Logic Simulation (Vivado)", "Implemented and simulated digital logic circuits on FPGA, gaining hands-on experience in hardware design, testing, and debugging."),
]

def projects_section():
    cards_html = "".join(
        f'<div style="{CARD}"><div style="{NUM}">{n}</div><div style="{TTL}">{t}</div><div style="{DSC}">{d}</div></div>'
        for n, t, d in projects
    )
    st.markdown(f'''
    <div id="projects" style="padding:5rem 5vw;scroll-margin-top:80px;position:relative;z-index:1;">
        <h2 style="font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:700;color:#f0f0f0;margin-bottom:2.5rem;letter-spacing:-.02em;">🚀 Projects</h2>
        <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:1.5rem;">
            {cards_html}
        </div>
    </div>
    <hr style="border:none;height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.07) 20%,rgba(255,255,255,0.07) 80%,transparent);margin:0;">
    ''', unsafe_allow_html=True)

# Calling the function to display
projects_section()