import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("# 3D Plot Visualization 📈")
st.write("")
st.write("")
st.write("")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
df = st.session_state.df
st.subheader("Dataset")
st.write(df)

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.plot3D(
    sorted(df["Age"]), sorted(df["Rating"]), sorted(df["Positive Feedback Count"])
)

ax.set_title("3D Scatter plot")
ax.set_xlabel("Age")
ax.set_ylabel("Rating")
ax.set_zlabel("Positive Feedback Count")

st.write("")
st.write("")
st.write("")
st.subheader("3D Plot between Age, Rating and Positive Feedback Count")
st.pyplot(fig)
