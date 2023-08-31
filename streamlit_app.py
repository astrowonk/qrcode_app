import streamlit as st
import segno

content = st.text_input("Content for QR Code", placeholder="Enter text...")

col1, col2, col3, col4 = st.columns(4)

data_dark = st.color_picker("Pick Data Dark Color")
# with col2:
#     dark = st.color_picker("Pick Dark Color")
# with col3:
#     data_light = st.color_picker("Pick Data Light Color", value="#FFFFFF")

# with col4:
#     light = st.color_picker("Light color", value="#FFFFFF")

if content:
    _qrcode = segno.make(content, micro=False)

    # st.image(_qrcode.svg_data_uri(data_dark=data_dark,
    #                               dark=dark,
    #                               data_light=data_light,
    #                               light=light),
    #          width=500)

    st.image(_qrcode.svg_data_uri(data_dark=data_dark), width=500)
