import streamlit as st

# 1. Page Settings (Walmart Theme Colors)
st.set_page_config(
    page_title="Walmart Sales Predictor", 
    page_icon="🛒", 
    layout="centered"
)

# Custom CSS for clean layout
st.markdown("""
    <style>
    .main { background-color: #F4F6F8; }
    .walmart-title {
        background-color: #0071CE;
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #FFC220;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Beautiful Simple Header
st.markdown("""
    <div class="walmart-title">
        <h1 style='color: white; margin: 0;'>🛒 Walmart Sales Predictor</h1>
        <p style='color: #FFC220; margin: 5px 0 0 0; font-weight: bold;'>Vocational Training Project</p>
    </div>
""", unsafe_allow_html=True)

# 3. Two Pages (Tabs) - Simple & Clean
tab1, tab2 = st.tabs(["🏢 1. Store Information", "🔮 2. Predict Future Sales"])

# ==============================================================================
# TAB 1: STORE INFORMATION (Simple Guide)
# ==============================================================================
with tab1:
    st.subheader("Easily Understand Store & Department IDs")
    st.write("Confusion door karne ke liye niche di gayi details dekhein:")
    
    st.markdown("### 📍 Location Guide (Store IDs):")
    st.write("- **Store 1 to 10:** Big Cities (like New York, New Jersey) - High Sales")
    st.write("- **Store 11 to 20:** Southern Areas (like Texas, Florida) - Medium Sales")
    st.write("- **Store 21 to 45:** Other Regional Markets - Normal Sales")
    
    st.markdown("### 📦 Product Guide (Department IDs):")
    st.write("- **Department 1:** Electronics & Gadgets")
    st.write("- **Department 2:** Clothing & Footwear")
    st.write("- **Department 3:** Grocery & Food items")
    st.write("- **Department 4:** Home Decor & Furniture")
    st.write("- **Other IDs:** Festival & Seasonal Items")
    
    st.info("💡 **Kaam Kaise Karein:** Pehle yahan se apni choice ka Store aur Department dhyan mein rakh lein, phir upar **'2. Predict Future Sales'** tab par click karein.")

# ==============================================================================
# TAB 2: PREDICT FUTURE SALES (Main Feature)
# ==============================================================================
with tab1 if False else tab2:
    st.subheader("Enter Details below to Forecast Next Week's Sales")
    
    # Simple Inputs
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        store_id = st.number_input("Enter Store ID (1 to 45):", min_value=1, max_value=45, value=1)
    with col_in2:
        dept_id = st.number_input("Enter Department ID (1 to 99):", min_value=1, max_value=99, value=1)
        
    holiday_choice = st.radio("Is there any Holiday/Festival in that upcoming week?", ["No, Regular Week", "Yes, Holiday Week"])
    is_holiday = 1 if holiday_choice == "Yes, Holiday Week" else 0
    
    st.markdown("---")
    st.markdown("#### 📊 Past Sales Data (In US Dollars $)")
    
    lag_1 = st.number_input("Last Week's Sales ($):", min_value=0.0, value=20000.0)
    lag_52 = st.number_input("Sales exactly 1 Year Ago in the same week ($):", min_value=0.0, value=45000.0)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Prediction Button
    if st.button("🔮 Calculate Next Week's Sales", type="primary", use_container_width=True):
        
        # Simple Calculation Logic
        if lag_1 == 0 and lag_52 == 0:
            predicted_usd = 0.0
        else:
            base = (lag_52 * 0.55) + (lag_1 * 0.30)
            multiplier = 1.30 if is_holiday == 1 else 1.00
            predicted_usd = (base * multiplier) + (store_id * 30) + (dept_id * 20)
            
        predicted_inr = predicted_usd * 85.0
        
        # Display Results
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(f"### 🎯 Expected Sales Next Week: **${predicted_usd:,.2f}**")
        st.markdown(f"*(In Indian Rupees: approx ₹{predicted_inr:,.2f})*")
        
        st.markdown("---")
        st.markdown("#### 📦 Manager Strategy:")
        if predicted_usd > 40000:
            st.warning("⚠️ **Alert:** Sales zyada hone waali hai! Stock **25% badha lo** taaki saaman khatam na ho.")
        elif predicted_usd == 0:
            st.info("💤 **Alert:** Zero sales detected. Extra saaman mangwane ki zaroorat nahi hai.")
        else:
            st.success("✅ **Normal:** Sab theek chal raha hai. Standard stock maintain rakho.")
        st.markdown('</div>', unsafe_allow_html=True)
