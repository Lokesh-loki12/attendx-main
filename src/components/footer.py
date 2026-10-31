import streamlit as st

def footer_home():
    #logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
        <div style="display:flex; gap:6px; justify-content:center; align-items:center; margin-top:2rem;">
            <p style="font-weight:bold;color:white;"> Created by Loki </p>
            
        </div>
        """,
        unsafe_allow_html=True
    )

def footer_dashboard():
    st.markdown(
            f"""
            <div style="display:flex; gap:6px; justify-content:center; align-items:center; margin-top:2rem;">
                <p style="font-weight:bold;color:black;"> Created by Loki </p>
                
            </div>
            """,
            unsafe_allow_html=True
        )