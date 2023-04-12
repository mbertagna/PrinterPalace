import streamlit as st
import mysql.connector
from itertools import chain

db = mysql.connector.connect(
    host = "",
    user = "",
    password = "",
    database = "PrinterPalace"
)

cursor = db.cursor()


col1, col2, col3 = st.columns([1,4.5,1])


st.balloons()

with col2:
    st.markdown("<h1 style='text-align: center;'>~ Printer Palace ~</h1>", unsafe_allow_html=True)
    st.markdown("![Alt Text](https://media.giphy.com/media/h5LYyNFkOk0MjIArZW/giphy.gif)")


