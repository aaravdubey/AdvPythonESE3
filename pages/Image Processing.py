import streamlit as st
import cv2

st.write("# Image Processing")
st.write("")
st.write("")
st.write("")
st.subheader("Original Image")
img = cv2.imread(".\data\image1.jpg")
img_width = img.shape[1]
img_height = img.shape[0]
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
st.image(img)
st.write(f"Image Shape: {img.shape}")

st.write("")
st.write("")
st.write("")
st.write("")
st.subheader("Resize Image")
width = st.slider("Width in Pixels", min_value=0, max_value=500, value=200, step=1)
height = st.slider("Height in Pixels", min_value=0, max_value=500, value=200, step=1)
resized = cv2.resize(img, (width, height))
st.image(resized)

st.write("")
st.write("")
st.write("")
st.write("")
st.subheader("Grayscale Image")
grayscaled = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
st.image(grayscaled)

st.write("")
st.write("")
st.write("")
st.write("")
st.subheader("Crop Image")
crop_width = st.slider(
    "Width in Pixels", min_value=0, max_value=img_width, value=img_width, step=1
)
crop_height = st.slider(
    "Height in Pixels", min_value=0, max_value=img_height, value=img_height, step=1
)
cropped = img[0:crop_height, 0:crop_width]
st.image(cropped)

st.write("")
st.write("")
st.write("")
st.write("")
st.subheader("Rotate Image")
angle = st.slider("Rotation Angle", min_value=0, max_value=360, step=1)
(height, width) = img.shape[:2]
center = (width / 2, height / 2)

angle = angle
scale = 1.0
matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(img, matrix, (width, height))
st.image(rotated)
