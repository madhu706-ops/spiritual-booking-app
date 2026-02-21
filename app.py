import streamlit as st
import datetime

# 1. APP CONFIGURATION
st.set_page_config(page_title="Spiritual Portal", page_icon="✨", layout="centered")

st.title("✨ Divine Consultation Portal")
st.markdown("---")

# 2. CHARITY QUOTA (Simulated for Zero-Cost)
if 'charity_slots' not in st.session_state:
    st.session_state.charity_slots = 5

# 3. JATAGAM TOOL (Date range 1900-Today)
st.header("🌌 Free South Indian Jatagam")
with st.expander("Enter Birth Details", expanded=True):
    name = st.text_input("Full Name")
    
    # Selection range logic
    min_date = datetime.date(1900, 1, 1)
    max_date = datetime.date.today()
    default_date = datetime.date(1979, 1, 1)

    col1, col2 = st.columns(2)
    with col1:
        dob = st.date_input("Date of Birth", value=default_date, min_value=min_date, max_value=max_date)
    with col2:
        tob = st.time_input("Time of Birth")
    
    pob = st.text_input("Place of Birth")
    
    if st.button("Generate My Chart"):
        if name and pob:
            st.success(f"Namaste {name}!")
            st.markdown(f"### [👉 Click here to view your Chart](https://www.astrosage.com/freechart/birth-chart.asp?name={name})")
        else:
            st.warning("Please enter your details first.")

st.markdown("---")

# 4. SERVICES
st.header("🔮 Services")
service = st.selectbox("Choose a Service:", [
    "Select...", 
    "Charity Reading (PAYW)", 
    "Tarot (₹1,500)", 
    "Akashic (₹3,000 incl. Healing)"
])

if st.button("Confirm & Generate Ref ID"):
    ref_id = datetime.datetime.now().strftime('%Y%m%d%H%M')
    st.info(f"Booking Confirmed! Ref: {ref_id}")
    st.write("Please screenshot this and send it to your practitioner.")
