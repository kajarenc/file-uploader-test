import streamlit as st
from streamlit import config


st.write(config.get_options_for_section("server"))

image = st.camera_input("CAMERA INPUT")

if image:
    st.image(image)

single_file = st.file_uploader("SINGLE FILE UPLOADER")

if single_file:
    st.write(single_file.name)

multiple_files = st.file_uploader("MULTIPLE FILE UPLOADER", accept_multiple_files=True)

if multiple_files:
    for f in multiple_files:
        st.write(f.name)
