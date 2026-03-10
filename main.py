import streamlit as st
from utils import load_css, load_js
from sections import hero, skills, projects, experience, contact

st.set_page_config(
    page_title="Manaal Pervaiz | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS (must be first)
load_css()

# Navigation bar
st.markdown("""
<nav class="nav-wrap">
    <div class="nav-logo">Manaal<span>.</span></div>
    <ul class="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#skills">Skills</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#experience">Experience</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>
    <div class="avail-badge"><div class="avail-dot"></div>Open to Opportunities</div>
</nav>
""", unsafe_allow_html=True)

# Page sections
hero.hero_section()
skills.skills_section()
projects.projects_section()
experience.experience_section()
contact.contact_section()

# Load JS last
load_js()
