import streamlit as st
import serial.tools.list_ports as list_ports


st.title("Welcome to Brickeye's Tablet!")
button = st.button("Press for Ports")
if button:
    st.write("Hello World!")
    ports = list_ports.comports()
    st.write("Ports")
    st.write(ports)

    for port, desc, hwid in sorted(ports):
        st.write(f"{port}: {desc} [{hwid}]")
