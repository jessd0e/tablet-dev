import streamlit as st
import serial.tools.list_ports as list_ports


# docker build . -t jessicadoe/tablet-dev --no-cache=true
# docker run -p 8501:8501 --restart always jessicadoe/tablet-dev

st.title("Welcome to Brickeye's Tablet!")
button = st.button("Press for Ports")
if button:
    st.write("Hello World!")
    ports = list_ports.comports()
    st.write("Ports")
    st.write(ports)

    for port, desc, hwid in sorted(ports):
        st.write(f"{port}: {desc} [{hwid}]")
