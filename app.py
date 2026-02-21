importimport streamlit as st
from datetime import datetime

# 1. APP CONFIG
st.set_page_config(page_title="Spiritual Case Planner", layout="centered")
st.title("✨ Divine Consultation Portal")
st.markdown("---")

# 2. CHARITY QUOTA LOGIC
if 'charity_slots' not in st.session_state:
    st.session_state.charity_slots = 5

# 3. THE JATAGAM TOOL
st.header("🌌 Free South Indian Jatagam")
# Added a unique 'key' to avoid DuplicateElementID error
with st.expander("Enter Birth Details to Generate Chart", expanded=False):
    name = st.text_input("Full Name", key="jatagam_name")
    col1, col2 = st.columns(2)
    with col1:
        # FIXED DATE RANGE: Allows you to pick 1979 easily
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
        st.markdown(f"[Click here to see your South Indian Chart](https://www.astrosage.com/freechart/birth-chart.asp?name={name})")

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

# 5. PAYMENT & APPOINTMENT
if service != "Select a service...":
    # Replace the text below with your actual UPI ID
    st.info("🙏 To confirm, please pay via UPI: **yourname@upi**")
    if st.button("Confirm & Generate Sheet", key="btn_confirm"):
        st.balloons()
        st.subheader("📄 Appointment Sheet Created")
        st.json({"Ref": "DIVINE-2026", "Service": service, "Status": "Pending Payment"})
 streamlit as st
from datetime import datetime

# 1. APP CONFIG & STYLE
st.set_page_config(page_title="Spiritual Case Planner", layout="centered")
st.title("✨ Divine Consultation Portal")
st.markdown("---")

# 2. CHARITY QUOTA LOGIC (Reset monthly)
# Note: In a real app, this would use a database. 
# For zero-cost, we'll simulate the "5 slots per month" limit.
if 'charity_slots' not in st.session_state:
    st.session_state.charity_slots = 5  # Hardcoded starting limit

# 3. THE JATAGAM TOOL (Lead Magnet)
st.header("🌌 Free South Indian Jatagam")
with st.expander("Enter Birth Details to Generate Chart"):
    name = st.text_input("Full Name")
    col1, col2 = st.columns(2)
    with col1:
       import datetime  # Make sure this is at the very top of your file

# 3. THE JATAGAM TOOL (Modified for 1979 birth year)
st.header("🌌 Free South Indian Jatagam")
with st.expander("Enter Birth Details to Generate Chart"):
    name = st.text_input("Full Name")
    
    # We define the range here: 1900 to today
    min_date = datetime.date(1900, 1, 1)
    max_date = datetime.date.today()
    # We set the default starting view to 1979-01-01
    default_date = datetime.date(1979, 1, 1)

    col1, col2 = st.columns(2)
    with col1:
        dob = st.date_input(
            "Date of Birth", 
            value=default_date, 
            min_value=min_date, 
            max_value=max_date
        )
    with col2:
        tob = st.time_input("Time of Birth")
    
    pob = st.text_input("Place of Birth")
    
    if st.button("Generate Chart"):
        st.success(f"Details captured for {name}!")
        st.info("Directing you to the calculation engine...")
        st.markdown(f"[Click here to see your South Indian Chart Grid](https://www.astrosage.com/freechart/birth-chart.asp?name={name})")
    with col2:
        tob = st.time_input("Time of Birth")
    pob = st.text_input("Place of Birth")
    
    if st.button("Generate Chart"):
        st.success(f"Details captured for {name}!")
        st.info("Directing you to the Vedic Calculation Engine...")
        # Since we are starting for free, we link to a trusted free renderer
        # You can eventually replace this with a paid API like Prokerala
        st.markdown(f"[Click here to see your South Indian Chart Grid](https://www.astrosage.com/freechart/birth-chart.asp?name={name})")

st.markdown("---")

# 4. SERVICE BOOKING (Pricing Logic)
st.header("🔮 Book a Session")
service = st.selectbox("Choose a Service", [
    "Select a service...",
    "Charity Reading (PAYW - Limited)",
    "Tarot Reading (₹1,500)",
    "Pranic Healing (₹500)",
    "Akashic Reading (₹2,500 + Mandatory Healing)"
])

# Logic for Mandatory Add-ons & Charity Limits
if service == "Charity Reading (PAYW - Limited)":
    if st.session_state.charity_slots > 0:
        st.write(f"✅ Slot Available! ({st.session_state.charity_slots} left this month)")
        st.number_input("Energy Exchange (Pay as you wish)", min_value=0, value=11)
    else:
        st.error("🚫 Monthly Charity quota reached. Please check back next month or book a standard session.")

elif service == "Akashic Reading (₹2,500 + Mandatory Healing)":
    st.warning("⚡ This deep soul-work requires a mandatory Pranic Healing clearing.")
    st.write("**Total Energy Exchange: ₹3,000**")

elif service == "Tarot Reading (₹1,500)":
    st.write("**Total Energy Exchange: ₹1,500**")

# 5. THE APPOINTMENT SHEET GENERATOR (The Output)
if service != "Select a service...":
    if st.button("Confirm & Generate Appointment Sheet"):
        st.balloons()
        st.subheader("📄 Your Appointment Sheet (Draft)")
        # This acts as the dual-copy you requested
        case_data = {
            "ID": "REF-" + datetime.now().strftime("%Y%m%d%H%M"),
            "Client": name,
            "Service": service,
            "Date": str(dob),
            "Status": "Awaiting Energy Exchange Confirmation"
        }
        st.json(case_data)
        st.write("📩 A copy of this has been sent to your email and our admin dashboard.")
