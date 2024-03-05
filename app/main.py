import streamlit as st
import serial.tools.list_ports as list_ports


# docker build . -t tablet-dev --no-cache=true
# docker run -p 8501:8501 --restart always tablet-dev


button = st.button("Press for Ports")
if button:
    st.write("Hello World!")
    ports = list_ports.comports()

    for port, desc, hwid in sorted(ports):
        st.write(f"{port}: {desc} [{hwid}]")
