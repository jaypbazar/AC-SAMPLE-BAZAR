import streamlit as st
import numpy as np
import pandas as pd
import time

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.title("😎Applied Cryptography First App 😎")
st.write(
    "Lorem ipsum dolor sit amet consectetur adipisicing elit."
    "A obcaecati alias dolores facilis, et inventore dolore itaque voluptatem "
    "veritatis ad accusantium officia similique nemo praesentium doloremque ratione "
    "ipsum magni distinctio! Lorem ipsum, dolor sit amet consectetur adipisicing elit. "
    "Nobis praesentium maxime neque nostrum asperiores quis cumque provident, itaque eaque "
    "iure minima assumenda at nam exercitationem harum amet vitae deleniti libero. "
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo asperiores sequi "
    "quasi mollitia impedit possimus rerum blanditiis, ratione unde saepe sunt veniam "
    "sit ex ad cumque, obcaecati, reiciendis porro laboriosam."
)

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#0012FF")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)