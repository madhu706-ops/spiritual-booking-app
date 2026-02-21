import streamlit as st
from datetime import datetime

# 1. APP CONFIG
st.set_page_config(page_title="Spiritual Case Planner", layout="centered")
st.title("✨ Divine Consultation Portal")
st.markdown("---")

# 2. CHARITY QUOTA LOGIC
if 'charity_slots' not in st.session_state:
    st.session_state.charity_slots = 5

# 3. THE JATAGAM TOOL (FIXED LINK)
st.header("🌌 Free South Indian Jatagam")
with st.expander("Enter Birth Details to Generate Chart", expanded=True):
    name = st.text_input("Full Name", key="jatagam_name")
    col1, col2 = st.columns(2)
    with col1:
        # Allows you to pick 1979 easily
        dob = st.date_input(
            "Date of Birth", 
            value=datetime(1979, 1, 1), 
            min_value=datetime(1900, 1, 1), 
            max_value=datetime.now(),
            key="jatagam_dob"
        )
    with col2:
        tob = st.time_input("Time of Birth", key="jatagam_tob")
    pob = st.text_input("Place of Birth", key="jatagam_pob")
    
    if st.button("Generate Chart", key="btn_chart"):
        st.success(f"Details captured for {name}!")
        # This link is now simplified to prevent the 404 error
        st.markdown("### [👉 CLICK HERE TO SEE YOUR CHART](https://www.astrosage.com/free/kundli.asp)")
        st.info("Once you reach the page, just re-verify your time and place for the most accurate South Indian result.")

st.markdown("---")

# 4. SERVICE BOOKING
st.header("🔮 Book a Session")
service = st.selectbox("Choose a Service", [
    "Select a service...",
    "Charity Reading (PAYW - Limited)",
    "Tarot Reading (₹1,500)",
    "Pranic Healing (₹500)",
    "Akashic Reading (₹2,500 + Mandatory Healing)"
], key="service_select")

if service == "Charity Reading (PAYW - Limited)":
    if st.session_state.charity_slots > 0:
        st.write(f"✅ Slot Available! ({st.session_state.charity_slots} left)")
        st.number_input("Energy Exchange", min_value=0, value=11, key="payw_val")
    else:
        st.error("🚫 Monthly Charity quota reached.")

elif service == "Akashic Reading (₹2,500 + Mandatory Healing)":
    st.warning("⚡ Includes mandatory Pranic Healing clearing (Total: ₹3,000).")

# 5. PAYMENT & CONFIRMATION
if service != "Select a service...":
    # IMPORTANT: Update 'yourname@upi' to your actual UPI ID
    st.info("🙏 To confirm, please pay via UPI: **yourname@upi**")
    if st.button("Confirm & Generate Sheet", key="btn_confirm"):
        st.balloons()
        st.subheader("📄 Appointment Sheet Created")
        st.write(f"Ref ID: DIVINE-{datetime.now().strftime('%M%S')}")
        st.write(f"Service: {service}")
        st.write("Status: Awaiting Payment Confirmation")
