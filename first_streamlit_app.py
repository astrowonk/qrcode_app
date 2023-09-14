import streamlit as st
import segno

content = st.text_input("Content for QR Code", placeholder="Enter text...")


if content:
    _qrcode = segno.make(content)

    st.image(_qrcode.svg_data_uri(), width=500)



