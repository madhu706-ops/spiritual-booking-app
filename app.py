import streamlit as st
from datetime import datetime
import urllib.parse

# 1. APP CONFIG
st.set_page_config(page_title="Spiritual Case Planner", layout="centered")
st.title("✨ Divine Consultation Portal")
st.markdown("---")

# 2. THE JATAGAM TOOL (All fields restored)
st.header("🌌 Free South Indian Jatagam")

name = st.text_input("Full Name", key="name_input")
col1, col2 = st.columns(2)
with col1:
    dob = st.date_input("Date of Birth", value=datetime(1979, 1, 1), min_value=datetime(1900, 1, 1), key="dob_input")
with col2:
    tob = st.time_input("Time of Birth", key="tob_input")

# RESTORED FIELD: Place of Birth
pob = st.text_input("Place of Birth (City/State)", key="pob_input")

if st.button("Step 1: Save Details"):
    st.success(f"Details for {name} saved!")
    st.markdown("### Step 2: Get Your Chart")
    st.link_button("👉 Open South Indian Chart Calculator", "https://www.astrosage.com/free/kundli.asp")

st.markdown("---")

# 3. SERVICE BOOKING & WHATSAPP BRIDGE
st.header("🔮 Book a Session")
service = st.selectbox("Choose a Service", [
    "Select a service...",
    "Charity Reading (PAYW)",
    "Tarot Reading (₹1,500)",
    "Pranic Healing (₹500)",
    "Akashic Reading (₹3,000)"
])

if service != "Select a service...":
    # Replace the number below with your actual WhatsApp number
    phone_number = "919000000000" # Use format: 91 followed by 10 digits
    message = f"Hi! I want to book a {service}. My details: {name}, {dob}, {tob}, {pob}."
    encoded_msg = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_msg}"
    
    st.info("🙏 To confirm, please pay via UPI: **yourname@upi**")
