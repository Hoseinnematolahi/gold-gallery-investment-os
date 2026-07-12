import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        html, body, [class*="css"] {
            font-family: Vazirmatn, sans-serif;
        }

        .main {
            direction: rtl;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
