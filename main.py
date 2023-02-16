import streamlit as st
from PIL import Image

import style

st.set_page_config(layout="wide")
st.title("Pytorch Style Transfer Web App")
st.write("Upload an image to apply the candy style to it.")


# candy.pth | mosaic.pth | rain_princess.pth | udnie.pth
style_model = "saved_models/candy.pth"

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = Image.open(uploaded_file)
    st.image(image, width=400)
    st.write("Transforming...")

    model = style.load_model(style_model)
    style.stylize(model, uploaded_file, "images/output-images/output.jpg")
    image = Image.open("images/output-images/output.jpg")
    st.image(image, width=400)
