import streamlit as st

# 1. Page Settings (Clean & Professional)
st.set_page_config(
    page_title="Walmart Demand Control Center", 
    page_icon="🛒", 
    layout="wide"
)

# 2. Eye-Friendly Light Theme UI (Custom CSS)
st.markdown("""
    <style>
    /* Light Mode Gray Background to remove eye strain */
    .stApp {
        background-color: #F4F6F8;
        color: #041E42 !important;
    }
    
    /* Elegant Dark Blue Header */
    .walmart-header {
        background-color: #0071CE;
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Specific styles to force header text to Yellow, bypassing global rules */
    .walmart-header h1 {
        color: #FFC220 !important;
        margin: 0;
        font-size: 2.2rem;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    .walmart-header p {
        color: #FFC220 !important;
        margin: 5px 0 0 0;
        font-size: 1rem;
        font-weight: bold;
        letter-spacing: 0.5px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* Clean White Cards for Metrics and Results */
    .dashboard-card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 12px;
        border-left: 5px solid #0071CE;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* Specific styling for the final forecast output */
    .output-card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        border: 2px solid #FFC220; /* Soft Walmart Yellow Border */
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        margin-top: 20px;
    }
    
    /* Global Text Fixes for Visibility (Targets everything outside the header) */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: #041E42;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* Tab Font Tweaks */
    .stTabs [data-baseweb="tab"] {
        color: #041E42 !important;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        color: #0071CE !important;
        border-bottom-color: #0071CE !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. App Banner (Yellow text inside classic Blue header)
st.markdown("""
    <div class="walmart-header">
        <h1>Walmart Supply Chain Control Center</h1>
        <p>INVENTORY REPLENISHMENT & DEMAND FORECASTING SYSTEM</p>
    </div>
""", unsafe_allow_html=True)

# 4. Multipage View (Tabs)
tab1, tab2 = st.tabs(["🏢 1. System Infrastructure Guide", "🔮 2. Stock Replenishment Engine"])

# ==============================================================================
# TAB 1: SYSTEM INFRASTRUCTURE GUIDE (Super Clean Reference)
# ==============================================================================
with tab1:
    st.markdown("<div class=\"dashboard-card\">", unsafe_allow_html=True)
    st.subheader("Regional Architecture Mapping")
    st.markdown("Verify regional node profiles and inventory turnover patterns before executing your replenishment models.")
    
    col_dir1, col_dir2 = st.columns(2)
    with col_dir1:
        st.markdown("#### 📍 Location Classifications (Store IDs)")
        st.markdown("""
        * **Store IDs 01 - 10:** East Coast Supercenters *(High volume markets)*
        * **Store IDs 11 - 20:** Southern Distribution Zones *(Highly seasonal footprints)*
        * **Store IDs 21 - 30:** Midwest Logistical Hubs *(Stable baseline demand profiles)*
        * **Store IDs 31 - 45:** West Coast Urban Footprints *(Densely populated metropolitan clusters)*
        """)
        
    with col_dir2:
        st.markdown("#### 📦 Product Classifications (Department IDs)")
        st.markdown("""
        * **Department ID #01:** Consumer Electronics & Home Media
        * **Department ID #02:** Apparel, Footwear & Accessories
        * **Department ID #03:** Fresh Grocery & Consumables
        * **Department ID #04:** Home Improvement, Hardlines & Patio
        * **All Other Department IDs:** Seasonal, Promotional & Specialized SKU categories
        """)
    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# TAB 2: REPLENISHMENT ENGINE (Cleaned, Streamlined & Pure Value Calculations)
# ==============================================================================
with tab2:
    st.markdown("<div class=\"dashboard-card\">", unsafe_allow_html=True)
    st.subheader("Operational Parameter Inputs")
    st.markdown("Provide structural constraints and volume history to calculate supply chain requirements.")
    
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1:
        store_id = st.number_input("Target Store ID (1 - 45):", min_value=1, max_value=45, value=1)
    with col_in2:
        dept_id = st.number_input("Target Department ID (1 - 99):", min_value=1, max_value=99, value=1)
    with col_in3:
        holiday_choice = st.selectbox("Calendar Holiday Status:", ["Standard Operational Week", "National Holiday Peak Window"])
        is_holiday = 1 if holiday_choice == "National Holiday Peak Window" else 0

    st.markdown("---")
    
    # Simple, clear historical metrics
    st.markdown("#### Historical Sales Metrics")
    col_data1, col_data2 = st.columns(2)
    with col_data1:
        lag_1 = st.number_input("Total Sales From Prior Week ($ USD):", min_value=0.0, value=25000.0)
    with col_data2:
        lag_52 = st.number_input("Symmetric Historical Sales From 1 Year Ago ($ USD):", min_value=0.0, value=55000.0)
        
    st.markdown("---")
    
    # Real warehouse values to dynamically drive stock orders
    st.markdown("#### Current Logistics Constraints")
    col_stock1, col_stock2 = st.columns(2)
    with col_stock1:
        current_inventory = st.number_input("Current Warehouse Stock On-Hand ($ USD Equivalent):", min_value=0.0, value=30000.0)
    with col_stock2:
        safety_buffer = st.number_input("Required Safety Stock Padding ($ USD Level):", min_value=0.0, value=5000.0)
    st.markdown("</div>", unsafe_allow_html=True)

    # Execution Flow Trigger
    if st.button("🚀 RUN REPLENISHMENT ANALYSIS", type="primary", use_container_width=True):
        
        if lag_1 == 0 and lag_52 == 0:
            predicted_demand = 0.0
            order_recommendation = 0.0
            status_flag = "ZERO_DEMAND"
        else:
            # High-variance system patterns (Trained weights emulation)
            base_calc = (lag_52 * 0.58) + (lag_1 * 0.38)
            holiday_scaler = 1.315 if is_holiday == 1 else 1.00
            node_adjustments = (store_id * 35) + (dept_id * 15)
            
            predicted_demand = (base_calc * holiday_scaler) + node_adjustments
            if predicted_demand < 0: predicted_demand = 0.0
            
            # The Clear Logic: Target Stock Level = Forecasted Sales + Mandatory Safety Buffer
            target_stock_level = predicted_demand + safety_buffer
            
            if current_inventory < target_stock_level:
                order_recommendation = target_stock_level - current_inventory
                status_flag = "REORDER"
            elif current_inventory > (predicted_demand * 1.5):
                order_recommendation = 0.0
                status_flag = "OVERSTOCK"
            else:
                order_recommendation = 0.0
                status_flag = "STABLE"
                
        predicted_inr = predicted_demand * 85.0

        # Output Interface Construction
        st.markdown('<div class="output-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='color: #0071CE !important; margin-top:0;'>📊 Supply Chain Analytics Output</h3>", unsafe_allow_html=True)
        
        col_res1, col_res2, col_res3 = st.columns(3)
        with col_res1:
            st.metric(label="Forecasted Sales Demand (USD)", value=f"${predicted_demand:,.2f}")
            st.caption(f"Benchmark Valuation: ₹{predicted_inr:,.2f}")
        with col_res2:
            st.metric(label="Active On-Hand Stocks (USD)", value=f"${current_inventory:,.2f}")
        with col_res3:
            st.metric(label="Recommended Procurement Order ($)", value=f"${order_recommendation:,.2f}")
            
        st.markdown("<hr style='border: 0.5px solid #E2E8F0;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #041E42 !important;'>📋 Actionable Logistics Recommendation</h4>", unsafe_allow_html=True)
        
        # Simple, non-confusing clear action banners based on your parameters
        if status_flag == "ZERO_DEMAND":
            st.info("System indicates zero active commercial velocity. Keep automated stock replenishment paused.")
        elif status_flag == "REORDER":
            st.markdown(f"🔴 <span style='color: #FF4B4B; font-weight: bold;'>DEFICIT DETECTED — TRIGGER REORDER PROFILE</span>", unsafe_allow_html=True)
            st.markdown(f"**Action Plan:** Current inventory levels are insufficient to cover upcoming demand requirements along with your safety buffers. Place an immediate procurement batch order valued at **${order_recommendation:,.2f}** to mitigate potential stockout vulnerabilities.")
        elif status_flag == "OVERSTOCK":
            st.markdown(f"🟡 <span style='color: #FFC220; font-weight: bold;'>SURPLUS DETECTED — OVERSTOCK MITIGATION REQUIRED</span>", unsafe_allow_html=True)
            st.markdown(f"**Action Plan:** Current warehouse stock significantly exceeds anticipated consumption vectors. Freeze all pending inbound transfers for this sector immediately to limit overhead carry costs.")
        else:
            st.markdown(f"🟢 <span style='color: #4CAF50; font-weight: bold;'>OPTIMAL BALANCED EQUILIBRIUM</span>", unsafe_allow_html=True)
            st.markdown("**Action Plan:** Stock parameters are in perfect sync with upcoming consumption metrics. Maintain existing pipeline configuration without structural adjustments.")
            
        st.markdown('</div>', unsafe_allow_html=True)
