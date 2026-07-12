import streamlit as st

from engine.financial_engine import *


model=st.session_state.model



investment = inventory_value(

model["inventory"],

model["gold_price"]

)



revenue = calculate_revenue(

model["sales"],

model["gold_price"],

0.2

)



cost = (

model["rent"]

+

model["salary"]

)



profit = calculate_profit(

revenue*0.15,

cost

)



c1,c2,c3,c4=st.columns(4)



c1.metric(
"سرمایه",
f"{investment/1e9:.2f} B"
)


c2.metric(
"فروش ماهانه",
f"{revenue/1e9:.2f} B"
)


c3.metric(
"سود",
f"{profit/1e6:.0f} M"
)


c4.metric(
"ROI",
f"{calculate_roi(profit*12,investment):.1f}%"
)
