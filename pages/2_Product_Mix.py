import streamlit as st
import json

from engine.product_optimizer import optimize_mix


products=json.load(
open("config/products.json")
)


result=optimize_mix(

st.session_state.model["inventory"],

products

)



st.title(
"Product Mix Optimizer"
)


for k,v in result.items():

    st.write(

    k,

    v

    )
