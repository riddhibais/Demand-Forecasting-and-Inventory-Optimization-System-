import streamlit as st
import pandas as pd
import pickle
import numpy as np

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Retail Demand AI Explorer", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium dark/light layout adjustments
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #4F46E5;
        margin-bottom: 15px;
    }
    .predict-box {
        background-color: #EEF2F6;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #E2E8F0;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Sidebar Setup (Clean Input Controls)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3081/3081559.png", width=80)
st.sidebar.title("🎛️ Control Panel")
st.sidebar.markdown("Modify operational parameters to simulate demand.")

st.sidebar.subheader("📍 Location Details")
store = st.sidebar.number_input("Store ID", min_value=1, max_value=45, value=1, step=1)
dept = st.sidebar.number_input("Department ID", min_value=1, max_value=99, value=1, step=1)

st.sidebar.subheader("📅 Timeline Matrix")
year = st.sidebar.slider("Year Factor", min_value=2010, max_value=2030, value=2026)
month = st.sidebar.slider("Month", min_value=1, max_value=12, value=6)
week = st.sidebar.slider("Week of Year", min_value=1, max_value=52, value=26)
dayofweek = st.sidebar.select_slider("Day of Week", options=[0,1,2,3,4,5,6], format_func=lambda x: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][x])
is_holiday = st.sidebar.segmented_control("Holiday Window?", options=[0, 1], format_func=lambda x: "Yes 🎉" if x == 1 else "Regular Week 💼")

# 3. Main Dashboard Header
st.title("📈 Demand Forecasting & Inventory Optimization System")
st.markdown("##### Powered by an Enterprise Random Forest Pipeline (98.16% Variance Accuracy)")

# Load the trained model safely
@st.cache_resource
def load_model():
    with open('walmart_rf_model.pkl', 'rb') as file:
        return pickle.load(file)

try:
    model = load_model()
except FileNotFoundError:
    st.error("⚠️ 'walmart_rf_model.pkl' missing! Please upload it to your GitHub directory.")
    st.stop()

st.divider()

# 4. KPI Layout Grid (Simulated Live Environment)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(label="Selected Store Node", value=f"Node-{store}", delta="Active")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(label="Department Classification", value=f"Dept #{dept}", delta="Monitored")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric(label="System Target Accuracy", value="98.16%", delta="Production Ready", delta_color="inverse")
    st.markdown('</div>', unsafe_allow_html=True)

# 5. Advanced Historical Indicators (Inputs)
st.subheader("📊 Historical Context & Trend Analysis")
st.markdown("Configure the historical features engineered during the model training phase:")

c1, c2, c3 = st.columns(3)
with c1:
    lag_1 = st.number_input("Sales 1 Week Ago ($)", min_value=0.0, value=22500.0, step=500.0)
with c2:
    lag_2 = st.number_input("Sales 2 Weeks Ago ($)", min_value=0.0, value=21000.0, step=500.0)
with c3:
    lag_52 = st.number_input("Sales 52 Weeks Ago (Yearly Seasonality) ($)", min_value=0.0, value=48000.0, step=1000.0)

# Automatic feature translation
rolling_mean_4 = (lag_1 + lag_2) / 2

st.divider()

# 6. Prediction Logic Trigger
st.subheader("🔮 ML Inference Engine")

if st.button("🚀 Run Live Demand Forecast", type="primary", use_container_width=True):
    # Prepare payload
    input_data = pd.DataFrame([{
        'Store': store, 'Dept': dept, 'IsHoliday': is_holiday,
        'year': year, 'month': month, 'week': week, 'dayofweek': dayofweek,
        'lag_1': lag_1, 'lag_2': lag_2, 'lag_52': lag_52, 'rolling_mean_4': rolling_mean_4
    }])
    
    # Process
    with st.spinner("Analyzing historical trends and computing feature matrices..."):
        prediction_usd = model.predict(input_data)[0]
        prediction_inr = prediction_usd * 85.0
    
    # Elegant Output Presentation
    st.markdown('<div class="predict-box">', unsafe_allow_html=True)
    st.markdown("### 🎯 AI Forecast Results")
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric(label="Projected Revenue (USD)", value=f"${prediction_usd:,.2f}")
    with res_col2:
        st.metric(label="Projected Revenue (INR Value)", value=f"₹{prediction_inr:,.2f}")
        
    # Smart Inventory Advice
    st.markdown("---")
    st.markdown("#### 📦
