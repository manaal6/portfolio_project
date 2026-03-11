import streamlit as st
import streamlit.components.v1 as components
import os
import time

def load_css():
    css_path = os.path.join("styles", "main.css")
    if os.path.exists(css_path):
        with open(css_path) as f:
            css = f.read()
        # Cache buster to ensure style updates immediately
        st.markdown(f"<style>{css} /* {time.time()} */</style>", unsafe_allow_html=True)
    
    st.markdown("""
    <style>
        #MainMenu, footer, header { visibility: hidden; }
        .stAppDeployButton { display:none; }
        [data-testid="stAppViewBlockContainer"] { padding: 0 !important; }
    </style>
    """, unsafe_allow_html=True)

def load_js():
    components.html("""
    <script>
    const doc = window.parent.document;
    const navLinks = doc.querySelectorAll('.nav-links a');
    
    // 1. Force scroll to top on fresh load
    if (!window.parent.location.hash) {
        window.parent.scrollTo(0, 0);
    }

    // 2. Smooth Scroll Logic
    navLinks.forEach(link => {
        link.onclick = function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').slice(1);
            const target = doc.getElementById(targetId);
            if (target) {
                target.scrollIntoView({behavior: "smooth", block: "start"});
            }
        };
    });

    // 3. ScrollSpy Logic: Highlights the menu item as you scroll
    function updateActiveLink() {
        let fromTop = window.parent.scrollY + 150; // Offset for navbar height

        navLinks.forEach(link => {
            const sectionId = link.getAttribute('href').slice(1);
            const section = doc.getElementById(sectionId);

            if (section) {
                if (
                    section.offsetTop <= fromTop &&
                    section.offsetTop + section.offsetHeight > fromTop
                ) {
                    link.classList.add('active');
                } else {
                    link.classList.remove('active');
                }
            }
        });
    }

    window.parent.addEventListener('scroll', updateActiveLink);
    // Initial call to set active state on load
    setTimeout(updateActiveLink, 500);
    </script>
    """, height=0)