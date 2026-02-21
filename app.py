import streamlit as st
from datetime import datetime

# 1. APP CONFIG
st.set_page_config(page_title="Spiritual Case Planner", layout="centered")
st.title("✨ Divine Consultation Portal")
st.markdown("---")

# 2. THE JATAGAM TOOL (Simplified to prevent 404)
st.header("🌌 Free South Indian Jatagam")
st.write("Enter your details below, then click the button to open the calculator.")

with st.container():
    name = st.text_input("Full Name", key="name_input")
    col1, col2 = st.columns(2)
    with col1:
        dob = st.date_input(
            "Date of Birth", 
            value=datetime(1979, 1, 1), 
            min_value=datetime(1900, 1, 1), 
            key="dob_input"
        )
    with col2:
        tob = st.time_input("Time of Birth", key="tob_input")
    
    # This button now acts as a reliable bridge
    if st.button("Step 1: Save Details & Get Link"):
        st.success(f"Details for {name} saved to your session!")
        st.markdown("### Step 2: Click the link below")
        # Direct link to the main entry page which never 404s
        st.link_button("👉 Open South Indian Chart Calculator", "https://www.astrosage.com/free/kundli.asp")

st.markdown("---")

# 3. SERVICE BOOKING & UPI
st.header("🔮 Book a Session")
service = st.selectbox("Choose a Service", [
    "Select a service...",
    "Charity Reading (PAYW)",
    "Tarot Reading (₹1,500)",
    "Pranic Healing (₹500)",
    "Akashic Reading (₹3,000)"
])

if service != "Select a service...":
    # Change 'yourname@upi' below to your actual UPI ID
    st.info("🙏 To confirm, please pay via UPI: **yourname@upi**")
    if st.button("Confirm Booking"):
        st.balloons()
        st.subheader("📄 Appointment Created")
        st.write(f"Ref: DIVINE-{datetime.now().strftime('%M%S')}")
        st.write(f"Service: {service}")
