{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import streamlit as st\
from components.styles import load_css\
\
\
st.set_page_config(\
    page_title="Gold Gallery OS",\
    page_icon="\uc0\u55357 \u57313 ",\
    layout="wide"\
)\
\
\
load_css()\
\
\
st.title(\
"\uc0\u55357 \u57313  Gold Gallery Investment OS"\
)\
\
\
st.markdown("""\
\uc0\u1587 \u1740 \u1587 \u1578 \u1605  \u1607 \u1608 \u1588 \u1605 \u1606 \u1583  \u1575 \u1605 \u1705 \u1575 \u1606 \u8204 \u1587 \u1606 \u1580 \u1740  \u1585 \u1575 \u1607 \u8204 \u1575 \u1606 \u1583 \u1575 \u1586 \u1740  \u1711 \u1575 \u1604 \u1585 \u1740  \u1591 \u1604 \u1575 \
\
\uc0\u1588 \u1740 \u1585 \u1575 \u1586  | \u1575 \u1607 \u1608 \u1575 \u1586  | \u1605 \u1585 \u1608 \u1583 \u1588 \u1578  | \u1575 \u1585 \u1587 \u1606 \u1580 \u1575 \u1606 \
\
""")\
\
\
# Global State\
\
if "model" not in st.session_state:\
\
    st.session_state.model = \{\
\
        "city":"\uc0\u1588 \u1740 \u1585 \u1575 \u1586 ",\
\
        "gold_price":7000000,\
\
        "inventory":750,\
\
        "cash":1200000000,\
\
        "sales":150,\
\
        "rent":150000000,\
\
        "salary":80000000\
\
    \}\
\
\
st.sidebar.success(\
"\uc0\u1587 \u1740 \u1587 \u1578 \u1605  \u1570 \u1605 \u1575 \u1583 \u1607  \u1578 \u1581 \u1604 \u1740 \u1604  \u1575 \u1587 \u1578 "\
)\
\
\
st.sidebar.write(\
st.session_state.model\
)}