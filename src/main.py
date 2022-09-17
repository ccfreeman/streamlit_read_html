import streamlit as st
import streamlit.components.v1 as components
import plotly
import pandas as pd
import numpy as np


# with open("html/test.html", 'r') as f:
#     html_fig = f.read()
# components.html(html_fig)

# st.markdown(html_fig, unsafe_allow_html=True)

st.title('Uber pickups in NYC')

fig = plotly.io.read_json("graphics/test.json")

st.plotly_chart(fig)
