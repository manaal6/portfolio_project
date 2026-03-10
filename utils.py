import streamlit as st
import streamlit.components.v1 as components

def load_css():
    with open("styles/main.css") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    # Strip all Streamlit chrome and padding
    st.markdown("""
    <style>
        #MainMenu, footer, header { visibility: hidden; }
        div[data-testid="stToolbar"],
        div[data-testid="stDecoration"],
        div[data-testid="stStatusWidget"] { display: none !important; }
        .appview-container .main .block-container,
        .stMainBlockContainer {
            padding: 0 !important;
            max-width: 100% !important;
        }
        div[data-testid="stVerticalBlock"] > div { margin-bottom: 0 !important; }
        div[data-testid="stVerticalBlockBorderWrapper"] { padding: 0 !important; }
    </style>
    """, unsafe_allow_html=True)

def load_js():
    components.html("""
    <script>
    (function(){
        function initScrollSpy() {
            const doc = window.parent.document;
            const navLinks = doc.querySelectorAll('.nav-links a');
            if (!navLinks.length) { setTimeout(initScrollSpy, 300); return; }
            const ids = ['about','skills','projects','experience','contact'];
            const sections = ids.map(id => doc.querySelector('#' + id)).filter(Boolean);
            const observer = new window.parent.IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const id = entry.target.getAttribute('id');
                        navLinks.forEach(a => {
                            a.classList.remove('active');
                            if (a.getAttribute('href') === '#' + id) a.classList.add('active');
                        });
                    }
                });
            }, { threshold: 0.3 });
            sections.forEach(s => observer.observe(s));
        }
        setTimeout(initScrollSpy, 600);
    })();
    </script>
    """, height=0)
