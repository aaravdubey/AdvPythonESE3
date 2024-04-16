import streamlit as st
import pandas as pd

st.title("Advanced Python ESE 3")
st.write("")

st.markdown(
    """
  Name - Dubey Aarav Shailesh

  Reg No - 2347114

  Class - 3 MCA A
"""
)


df = pd.read_csv("./data/WomensClothingE-CommerceReviews.csv")
st.session_state["df"] = df
