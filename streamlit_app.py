"""
NexGen Logistics Analytics Dashboard
High-End UI | Interactive Onboarding | Dynamic Visualizations | Professional Design
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")

# =========================
# PAGE CONFIG & ADVANCED STYLING
# =========================
st.set_page_config(
    page_title="NexGen Logistics Analytics",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium CSS with animations and glassmorphism
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * {font-family: 'Inter', sans-serif;}
    
    .main {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1419 100%);
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0%, 100% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
    }
    
    .stApp {background: transparent;}
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Onboarding Container */
    .onboarding-container {
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.95), rgba(30, 40, 70, 0.95));
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 4rem;
        border: 2px solid rgba(0, 212, 255, 0.3);
        box-shadow: 0 20px 60px rgba(0, 212, 255, 0.2);
        margin: 2rem auto;
        max-width: 900px;
        animation: fadeInUp 0.8s ease;
    }
    
    @keyframes fadeInUp {
        from {opacity: 0; transform: translateY(30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    
    .onboarding-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .onboarding-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00D4FF, #0078FF, #00FFC2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: glow 2s ease-in-out infinite;
    }
    
    @keyframes glow {
        0%, 100% {filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.5));}
        50% {filter: drop-shadow(0 0 40px rgba(0, 212, 255, 0.8));}
    }
    
    .onboarding-subtitle {
        font-size: 1.3rem;
        color: #8B92B8;
        font-weight: 300;
    }
    
    /* Progress Bar */
    .progress-container {
        background: rgba(0, 0, 0, 0.3);
        height: 8px;
        border-radius: 10px;
        margin: 2rem auto;
        overflow: hidden;
        max-width: 900px;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #00D4FF, #0078FF, #00FFC2);
        border-radius: 10px;
        transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.6);
    }
    
    /* Metric Cards Container */
    .metrics-container {
        display: grid;
        grid-template-columns: repeat(6, 1fr);
        gap: 1rem;
        margin: 2rem 0;
        padding: 0 1rem;
    }
    
    @media (max-width: 1400px) {
        .metrics-container {
            grid-template-columns: repeat(3, 1fr);
        }
    }
    
    @media (max-width: 768px) {
        .metrics-container {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.9), rgba(30, 40, 70, 0.8));
        backdrop-filter: blur(20px);
        padding: 1.8rem 1.2rem;
        border-radius: 20px;
        border: 2px solid rgba(0, 212, 255, 0.3);
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.2);
        text-align: center;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 212, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-10px) scale(1.05);
        border-color: #00D4FF;
        box-shadow: 0 20px 60px rgba(0, 212, 255, 0.4);
    }
    
    .metric-label {
        color: #8B92B8;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 0.8rem;
        white-space: nowrap;
    }
    
    .metric-value {
        color: #00D4FF;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
        line-height: 1.2;
    }
    
    .metric-icon {
        font-size: 2.8rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 10px rgba(0, 212, 255, 0.5));
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #00D4FF, #0078FF);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 1rem 3rem;
        font-weight: 700;
        font-size: 1.1rem;
        width: 100%;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .stButton>button::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .stButton>button:hover::before {
        width: 300px;
        height: 300px;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 212, 255, 0.6);
    }
    
    /* Dashboard Header */
    .dashboard-header {
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.95), rgba(30, 40, 70, 0.95));
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        border: 2px solid rgba(0, 212, 255, 0.3);
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .dashboard-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00D4FF, #0078FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .dashboard-subtitle {
        color: #8B92B8;
        font-size: 1.1rem;
    }
    
    /* Chart Container */
    .chart-container {
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.9), rgba(30, 40, 70, 0.8));
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        border: 2px solid rgba(0, 212, 255, 0.2);
        margin: 1.5rem 0;
        transition: all 0.3s;
    }
    
    .chart-container:hover {
        border-color: rgba(0, 212, 255, 0.5);
        box-shadow: 0 10px 40px rgba(0, 212, 255, 0.2);
    }
    
    .chart-title {
        color: #00D4FF;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    /* Insights Card */
    .insight-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 245, 255, 0.95));
        border-left: 6px solid #00D4FF;
        border-radius: 16px;
        padding: 1.8rem;
        margin: 1rem 0;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .insight-card:hover {
        transform: translateX(10px);
        background: linear-gradient(135deg, rgba(255, 255, 255, 1), rgba(240, 250, 255, 1));
        box-shadow: -5px 0 25px rgba(0, 212, 255, 0.4);
    }
    
    .insight-card.success {
        border-left-color: #00C853;
        background: linear-gradient(135deg, rgba(232, 255, 240, 0.95), rgba(200, 255, 220, 0.95));
    }
    
    .insight-card.warning {
        border-left-color: #FFB300;
        background: linear-gradient(135deg, rgba(255, 250, 230, 0.95), rgba(255, 245, 200, 0.95));
    }
    
    .insight-card.danger {
        border-left-color: #FF3D00;
        background: linear-gradient(135deg, rgba(255, 240, 240, 0.95), rgba(255, 225, 225, 0.95));
    }
    
    .insight-text {
        color: #1a1a2e;
        font-size: 1.05rem;
        line-height: 1.8;
        font-weight: 500;
    }
    
    .insight-text strong {
        color: #0a0e27;
        font-weight: 700;
    }
    
    /* Filter Sidebar */
    .filter-section {
        background: linear-gradient(135deg, rgba(15, 25, 50, 0.95), rgba(30, 40, 70, 0.95));
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2rem;
        border: 2px solid rgba(0, 212, 255, 0.3);
        margin-bottom: 2rem;
    }
    
    .filter-title {
        color: #00D4FF;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {width: 10px;}
    ::-webkit-scrollbar-track {background: rgba(0, 0, 0, 0.2);}
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #00D4FF, #0078FF);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {background: linear-gradient(135deg, #0078FF, #00D4FF);}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE INITIALIZATION
# =========================
if 'onboarding_complete' not in st.session_state:
    st.session_state.onboarding_complete = False
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'user_prefs' not in st.session_state:
    st.session_state.user_prefs = {
        'priorities': [],
        'categories': [],
        'origins': [],
        'time_range': 30,
        'view_mode': 'Executive Overview'
    }

# =========================
# DATA LOADING
# =========================
@st.cache_data
def load_data():
    try:
        orders = pd.read_csv("data/orders.csv")
        vehicles = pd.read_csv("data/vehicle_fleet.csv")
        routes = pd.read_csv("data/routes_distance.csv")
        delivery = pd.read_csv("data/delivery_performance.csv")
        feedback = pd.read_csv("data/customer_feedback.csv")
        cost = pd.read_csv("data/cost_breakdown.csv")
        inventory = pd.read_csv("data/warehouse_inventory.csv")

        # Data processing
        orders['Special_Handling'] = orders['Special_Handling'].fillna('None')
        routes['Weather_Impact'] = routes['Weather_Impact'].fillna('None')
        delivery['Quality_Issue'] = delivery['Quality_Issue'].fillna('Perfect')
        orders['Order_Date'] = pd.to_datetime(orders['Order_Date'], errors='coerce')

        # Derived metrics
        np.random.seed(42)
        weight_ranges = {
            'Electronics': (1, 10), 'Fashion': (0.3, 2), 'Food & Beverage': (2, 30),
            'Healthcare': (0.5, 6), 'Industrial': (15, 120), 'Books': (0.4, 4), 'Home Goods': (5, 40)
        }
        orders['weight_kg'] = orders['Product_Category'].apply(
            lambda x: round(np.random.uniform(*weight_ranges.get(x, (1, 10))), 2)
        )

        delivery['delay_days'] = delivery['Actual_Delivery_Days'] - delivery['Promised_Delivery_Days']
        delivery['delay_min'] = np.maximum(delivery['delay_days'], 0) * 1440
        delivery['on_time'] = (delivery['delay_days'] <= 0).astype(int)

        cost['total_cost'] = cost[[
            'Fuel_Cost', 'Labor_Cost', 'Vehicle_Maintenance', 'Insurance',
            'Packaging_Cost', 'Technology_Platform_Fee', 'Other_Overhead'
        ]].sum(axis=1)

        orders = orders.merge(routes[['Order_ID', 'Distance_KM', 'Traffic_Delay_Minutes']], on='Order_ID', how='left')
        orders = orders.merge(delivery[['Order_ID', 'Delivery_Status', 'Customer_Rating', 'on_time', 'delay_min']], on='Order_ID', how='left')
        orders = orders.merge(cost[['Order_ID', 'total_cost']], on='Order_ID', how='left')

        orders['co2_kg'] = orders['Distance_KM'] * 0.4
        orders['cost_per_km'] = orders['total_cost'] / orders['Distance_KM'].replace(0, np.nan)

        cutoff_date = datetime(2025, 11, 1) - timedelta(days=30)
        orders['status'] = np.where(orders['Order_Date'] >= cutoff_date, 'Pending', 'Completed')

        return orders, vehicles, delivery, feedback, inventory

    except FileNotFoundError:
        st.error("⚠️ Data files not found. Please ensure all CSV files are in the 'data' folder.")
        st.stop()
    except Exception as e:
        st.error(f"⚠️ Error loading data: {e}")
        st.stop()

# =========================
# ONBOARDING FLOW
# =========================
if not st.session_state.onboarding_complete:
    
    steps = [
        {
            'title': '🚀 Welcome to NexGen Logistics',
            'subtitle': 'Advanced Analytics Platform for Supply Chain Excellence',
            'type': 'welcome'
        },
        {
            'title': '🎯 Select Priority Levels',
            'subtitle': 'Choose the delivery priorities you want to monitor',
            'options': ['Express', 'Standard', 'Economy'],
            'key': 'priorities',
            'type': 'multi'
        },
        {
            'title': '📦 Product Categories',
            'subtitle': 'Select product categories to track',
            'options': ['Electronics', 'Fashion', 'Food & Beverage', 'Healthcare', 'Industrial', 'Books', 'Home Goods'],
            'key': 'categories',
            'type': 'multi'
        },
        {
            'title': '📍 Origin Cities',
            'subtitle': 'Choose your key dispatch locations',
            'options': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad'],
            'key': 'origins',
            'type': 'multi'
        },
        {
            'title': '⚙️ Dashboard Configuration',
            'subtitle': 'Customize your analytics experience',
            'type': 'config'
        }
    ]
    
    current = steps[st.session_state.step]
    progress = (st.session_state.step + 1) / len(steps) * 100
    
    # Onboarding header with progress
    st.markdown(f"""
    <div class="onboarding-container">
        <div class="onboarding-header">
            <div class="onboarding-title">{current['title']}</div>
            <div class="onboarding-subtitle">{current['subtitle']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="progress-container">
        <div class="progress-bar" style="width: {progress}%"></div>
    </div>
    """, unsafe_allow_html=True)
    
    if current['type'] == 'welcome':
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("https://cdn-icons-png.flaticon.com/512/2920/2920277.png", width=200)
            st.markdown("""
            <div style='text-align: center; color: #8B92B8; font-size: 1.1rem; line-height: 1.8; margin: 2rem 0;'>
                Unlock powerful insights with real-time analytics, predictive forecasting,
                and intelligent automation. Let's personalize your dashboard in just a few steps.
            </div>
            """, unsafe_allow_html=True)
    
    elif current['type'] == 'multi':
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns(min(3, len(current['options'])))
        for idx, option in enumerate(current['options']):
            with cols[idx % len(cols)]:
                selected = option in st.session_state.user_prefs[current['key']]
                if st.button(
                    f"{'✓ ' if selected else ''}{option}",
                    key=f"opt_{option}",
                    use_container_width=True
                ):
                    if selected:
                        st.session_state.user_prefs[current['key']].remove(option)
                    else:
                        st.session_state.user_prefs[current['key']].append(option)
                    st.rerun()
    
    elif current['type'] == 'config':
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            time_range = st.selectbox(
                "📅 Time Range",
                [7, 15, 30, 60, 90],
                index=2,
                format_func=lambda x: f"Last {x} days"
            )
            st.session_state.user_prefs['time_range'] = time_range
        
        with col2:
            view_mode = st.selectbox(
                "📊 Dashboard View",
                ['Executive Overview', 'Operational Details', 'Predictive Analytics']
            )
            st.session_state.user_prefs['view_mode'] = view_mode
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.step > 0:
            if st.button("← Back", use_container_width=True):
                st.session_state.step -= 1
                st.rerun()
    
    with col2:
        if current['type'] == 'multi':
            selected_count = len(st.session_state.user_prefs[current['key']])
            st.markdown(f"<div style='text-align:center; color:#8B92B8; padding:1rem;'>Selected: {selected_count}</div>", unsafe_allow_html=True)
    
    with col3:
        if st.session_state.step < len(steps) - 1:
            if st.button("Next →", use_container_width=True):
                st.session_state.step += 1
                st.rerun()
        else:
            if st.button("🚀 Launch Dashboard", use_container_width=True):
                # Set defaults if nothing selected
                if not st.session_state.user_prefs['priorities']:
                    st.session_state.user_prefs['priorities'] = ['Express', 'Standard', 'Economy']
                if not st.session_state.user_prefs['categories']:
                    st.session_state.user_prefs['categories'] = ['Electronics', 'Fashion', 'Food & Beverage', 'Healthcare', 'Industrial', 'Books', 'Home Goods']
                if not st.session_state.user_prefs['origins']:
                    st.session_state.user_prefs['origins'] = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai']
                
                st.session_state.onboarding_complete = True
                st.rerun()

else:
    # =========================
    # MAIN DASHBOARD
    # =========================
    
    # Load data
    orders, vehicles, delivery, feedback, inventory = load_data()
    
    # Apply filters based on user preferences
    prefs = st.session_state.user_prefs
    filtered = orders[
        orders['Priority'].isin(prefs['priorities']) &
        orders['Product_Category'].isin(prefs['categories']) &
        orders['Origin'].isin(prefs['origins'])
    ]
    
    # Calculate metrics
    total_orders = len(filtered)
    on_time_rate = filtered['on_time'].mean() * 100 if not filtered['on_time'].isna().all() else 0
    avg_cost_per_km = filtered['cost_per_km'].mean() if not filtered['cost_per_km'].isna().all() else 0
    total_co2 = filtered['co2_kg'].sum() if not filtered['co2_kg'].isna().all() else 0
    avg_delay = filtered['delay_min'].mean() if not filtered['delay_min'].isna().all() else 0
    total_revenue = filtered['total_cost'].sum() if not filtered['total_cost'].isna().all() else 0
    
    # Header
    st.markdown("""
    <div class="dashboard-header">
        <div class="dashboard-title">NexGen Logistics Command Center</div>
        <div class="dashboard-subtitle">Real-Time Analytics • Predictive Intelligence • Data-Driven Decisions</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics Row using grid layout
    st.markdown(f"""
    <div class="metrics-container">
        <div class="metric-card">
            <div class="metric-icon">📦</div>
            <div class="metric-label">Total Orders</div>
            <div class="metric-value">{total_orders:,}</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">✅</div>
            <div class="metric-label">On-Time Rate</div>
            <div class="metric-value">{on_time_rate:.1f}%</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">💰</div>
            <div class="metric-label">Avg Cost/km</div>
            <div class="metric-value">₹{avg_cost_per_km:.1f}</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">🌍</div>
            <div class="metric-label">Total CO₂</div>
            <div class="metric-value">{total_co2/1000:.1f}t</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">⏱️</div>
            <div class="metric-label">Avg Delay</div>
            <div class="metric-value">{avg_delay:.0f}m</div>
        </div>
        <div class="metric-card">
            <div class="metric-icon">💵</div>
            <div class="metric-label">Revenue</div>
            <div class="metric-value">₹{total_revenue/1000000:.1f}M</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts Section
    col1, col2 = st.columns(2)
    
    # Chart 1: Delay vs Distance Scatter
    with col1:
        st.markdown('<div class="chart-container"><div class="chart-title">🎯 Delay vs Distance Analysis</div>', unsafe_allow_html=True)
        fig1 = px.scatter(
            filtered.sample(min(200, len(filtered))),
            x='Distance_KM',
            y='delay_min',
            color='Priority',
            size='weight_kg',
            hover_data=['Order_ID', 'Product_Category', 'Customer_Rating'],
            color_discrete_map={'Express': '#FF4444', 'Standard': '#00D4FF', 'Economy': '#00FFC2'},
            template='plotly_dark'
        )
        fig1.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Chart 2: Priority Distribution
    with col2:
        st.markdown('<div class="chart-container"><div class="chart-title">📊 Priority Distribution</div>', unsafe_allow_html=True)
        priority_data = filtered['Priority'].value_counts().reset_index()
        priority_data.columns = ['Priority', 'Count']
        fig2 = px.pie(
            priority_data,
            names='Priority',
            values='Count',
            hole=0.5,
            color='Priority',
            color_discrete_map={'Express': '#FF4444', 'Standard': '#00D4FF', 'Economy': '#00FFC2'},
            template='plotly_dark'
        )
        fig2.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            margin=dict(l=0, r=0, t=0, b=0),
            showlegend=True
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Chart 3: Category Performance
    st.markdown('<div class="chart-container"><div class="chart-title">🏆 Category Performance Analysis</div>', unsafe_allow_html=True)
    category_data = filtered.groupby('Product_Category').agg({
        'Order_ID': 'count',
        'total_cost': 'sum',
        'on_time': 'mean',
        'co2_kg': 'sum'
    }).reset_index()
    category_data.columns = ['Category', 'Orders', 'Revenue', 'On-Time Rate', 'CO2']
    category_data['On-Time Rate'] = category_data['On-Time Rate'] * 100
    
    fig3 = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Orders & Revenue', 'On-Time Performance'),
        specs=[[{'type': 'bar'}, {'type': 'bar'}]]
    )
    
    fig3.add_trace(
        go.Bar(
            x=category_data['Category'],
            y=category_data['Orders'],
            name='Orders',
            marker_color='#00D4FF',
            hovertemplate='%{x}<br>Orders: %{y}<extra></extra>'
        ),
        row=1, col=1
    )
    
    fig3.add_trace(
        go.Bar(
            x=category_data['Category'],
            y=category_data['On-Time Rate'],
            name='On-Time %',
            marker_color='#00FFC2',
            hovertemplate='%{x}<br>On-Time: %{y:.1f}%<extra></extra>'
        ),
        row=1, col=2
    )
    
    fig3.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=450,
        showlegend=False,
        margin=dict(l=0, r=0, t=40, b=0)
    )
    fig3.update_xaxes(tickangle=-45)
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Chart 4: Carrier Performance
    with col1:
        st.markdown('<div class="chart-container"><div class="chart-title">🚚 Carrier Performance</div>', unsafe_allow_html=True)
        carrier_perf = delivery.groupby('Carrier').agg({
            'on_time': 'mean',
            'Order_ID': 'count'
        }).reset_index()
        carrier_perf.columns = ['Carrier', 'On-Time Rate', 'Orders']
        carrier_perf['On-Time Rate'] = carrier_perf['On-Time Rate'] * 100
        carrier_perf = carrier_perf.sort_values('On-Time Rate', ascending=True)
        
        fig4 = go.Figure(go.Bar(
            x=carrier_perf['On-Time Rate'],
            y=carrier_perf['Carrier'],
            orientation='h',
            marker=dict(
                color=carrier_perf['On-Time Rate'],
                colorscale='Blues',
                showscale=False
            ),
            text=carrier_perf['On-Time Rate'].apply(lambda x: f'{x:.1f}%'),
            textposition='outside',
            hovertemplate='%{y}<br>On-Time: %{x:.1f}%<extra></extra>'
        ))
        
        fig4.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis_title='On-Time Rate (%)',
            yaxis_title=''
        )
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Chart 5: Cost Breakdown
    with col2:
        st.markdown('<div class="chart-container"><div class="chart-title">💰 Cost Breakdown</div>', unsafe_allow_html=True)
        cost_breakdown = {
            'Category': ['Fuel', 'Labor', 'Maintenance', 'Insurance', 'Packaging', 'Platform Fee', 'Other'],
            'Amount': [35000, 28000, 15000, 12000, 8000, 6000, 4000]
        }
        cost_df = pd.DataFrame(cost_breakdown)
        
        fig5 = go.Figure(data=[go.Pie(
            labels=cost_df['Category'],
            values=cost_df['Amount'],
            hole=0.4,
            marker=dict(
                colors=['#FF4444', '#00D4FF', '#00FFC2', '#FFD700', '#FF8C00', '#9370DB', '#20B2AA'],
                line=dict(color='#0a0e27', width=2)
            ),
            textinfo='label+percent',
            textposition='outside',
            hovertemplate='%{label}<br>₹%{value:,.0f}<extra></extra>'
        )])
        
        fig5.update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=400,
            margin=dict(l=0, r=0, t=0, b=0),
            showlegend=False
        )
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Chart 6: Time Series Analysis
    st.markdown('<div class="chart-container"><div class="chart-title">📈 Daily Order Trends</div>', unsafe_allow_html=True)
    daily_orders = filtered.groupby(filtered['Order_Date'].dt.date).agg({
        'Order_ID': 'count',
        'on_time': 'mean',
        'total_cost': 'sum'
    }).reset_index()
    daily_orders.columns = ['Date', 'Orders', 'On-Time Rate', 'Revenue']
    daily_orders['On-Time Rate'] = daily_orders['On-Time Rate'] * 100
    
    fig6 = make_subplots(
        rows=2, cols=1,
        subplot_titles=('Daily Orders Volume', 'On-Time Performance Trend'),
        vertical_spacing=0.15,
        specs=[[{'type': 'scatter'}], [{'type': 'scatter'}]]
    )
    
    fig6.add_trace(
        go.Scatter(
            x=daily_orders['Date'],
            y=daily_orders['Orders'],
            mode='lines+markers',
            name='Orders',
            line=dict(color='#00D4FF', width=3),
            marker=dict(size=8, color='#00D4FF'),
            fill='tozeroy',
            fillcolor='rgba(0, 212, 255, 0.2)',
            hovertemplate='Date: %{x}<br>Orders: %{y}<extra></extra>'
        ),
        row=1, col=1
    )
    
    fig6.add_trace(
        go.Scatter(
            x=daily_orders['Date'],
            y=daily_orders['On-Time Rate'],
            mode='lines+markers',
            name='On-Time %',
            line=dict(color='#00FFC2', width=3),
            marker=dict(size=8, color='#00FFC2'),
            fill='tozeroy',
            fillcolor='rgba(0, 255, 194, 0.2)',
            hovertemplate='Date: %{x}<br>On-Time: %{y:.1f}%<extra></extra>'
        ),
        row=2, col=1
    )
    
    fig6.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=600,
        showlegend=False,
        margin=dict(l=0, r=0, t=40, b=0)
    )
    fig6.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.1)')
    fig6.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.1)')
    st.plotly_chart(fig6, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Chart 7: 3D Scatter - Distance vs Cost vs Weight
    st.markdown('<div class="chart-container"><div class="chart-title">🎲 3D Analysis: Distance vs Cost vs Weight</div>', unsafe_allow_html=True)
    sample_data = filtered.sample(min(150, len(filtered)))
    
    fig7 = go.Figure(data=[go.Scatter3d(
        x=sample_data['Distance_KM'],
        y=sample_data['total_cost'],
        z=sample_data['weight_kg'],
        mode='markers',
        marker=dict(
            size=6,
            color=sample_data['delay_min'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Delay (min)', x=1.1),
            line=dict(width=0.5, color='rgba(255,255,255,0.3)')
        ),
        text=sample_data['Priority'],
        hovertemplate='Distance: %{x:.0f} km<br>Cost: ₹%{y:.0f}<br>Weight: %{z:.1f} kg<br>Priority: %{text}<extra></extra>'
    )])
    
    fig7.update_layout(
        template='plotly_dark',
        scene=dict(
            xaxis=dict(title='Distance (km)', backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(255,255,255,0.1)'),
            yaxis=dict(title='Cost (₹)', backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(255,255,255,0.1)'),
            zaxis=dict(title='Weight (kg)', backgroundcolor='rgba(0,0,0,0)', gridcolor='rgba(255,255,255,0.1)'),
            bgcolor='rgba(0,0,0,0)'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=600,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    st.plotly_chart(fig7, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Chart 8: Heatmap - Origin to Destination
    st.markdown('<div class="chart-container"><div class="chart-title">🗺️ Route Heatmap: Origin × Destination</div>', unsafe_allow_html=True)
    route_matrix = filtered.groupby(['Origin', 'Destination']).size().reset_index(name='Count')
    route_pivot = route_matrix.pivot(index='Origin', columns='Destination', values='Count').fillna(0)
    
    fig8 = go.Figure(data=go.Heatmap(
        z=route_pivot.values,
        x=route_pivot.columns,
        y=route_pivot.index,
        colorscale='Blues',
        hovertemplate='From: %{y}<br>To: %{x}<br>Orders: %{z}<extra></extra>',
        colorbar=dict(title='Orders')
    ))
    
    fig8.update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis_title='Destination',
        yaxis_title='Origin'
    )
    st.plotly_chart(fig8, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Insights Section
    st.markdown('<div class="chart-container"><div class="chart-title">💡 AI-Powered Insights & Recommendations</div>', unsafe_allow_html=True)
    
    insights = []
    
    # Performance insight
    if on_time_rate >= 90:
        insights.append(("✅ **Excellent Performance**: Your on-time delivery rate of {:.1f}% exceeds industry standards (85%). Keep up the great work!".format(on_time_rate), "success"))
    elif on_time_rate >= 75:
        insights.append(("⚠️ **Room for Improvement**: On-time rate at {:.1f}%. Consider optimizing routes in high-delay zones.".format(on_time_rate), "warning"))
    else:
        insights.append(("🚨 **Action Required**: On-time rate of {:.1f}% is below target. Immediate operational review recommended.".format(on_time_rate), "danger"))
    
    # Cost insight
    if avg_cost_per_km < 40:
        insights.append(("💰 **Cost Efficient**: Your average cost of ₹{:.1f}/km is below industry average. Excellent cost management!".format(avg_cost_per_km), "success"))
    else:
        insights.append(("💸 **Cost Optimization**: At ₹{:.1f}/km, consider fuel efficiency programs or route optimization to reduce costs.".format(avg_cost_per_km), "warning"))
    
    # Carbon footprint
    avg_co2_per_order = total_co2 / max(total_orders, 1)
    if avg_co2_per_order < 150:
        insights.append(("🌱 **Eco-Friendly**: Average {:.0f} kg CO₂ per order. Consider carbon offset programs to achieve net-zero.".format(avg_co2_per_order), "success"))
    else:
        insights.append(("🌍 **Sustainability Focus**: High carbon footprint detected ({:.0f} kg CO₂/order). Recommend electric vehicle adoption for urban routes.".format(avg_co2_per_order), "warning"))
    
    # Priority analysis
    express_pct = len(filtered[filtered['Priority'] == 'Express']) / max(len(filtered), 1) * 100
    if express_pct > 40:
        insights.append(("⚡ **Premium Demand**: {:.0f}% Express orders indicate strong premium segment. Consider capacity expansion.".format(express_pct), "success"))
    
    # Delay patterns
    if avg_delay > 120:
        insights.append(("⏱️ **Delay Alert**: Average delay of {:.0f} minutes detected. High-traffic routes need alternative planning.".format(avg_delay), "danger"))
    
    for insight_text, insight_type in insights:
        st.markdown(f'<div class="insight-card {insight_type}"><div class="insight-text">{insight_text}</div></div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Export Section
    st.markdown('<br><br>', unsafe_allow_html=True)
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">📥 Export Dashboard Data</div>', unsafe_allow_html=True)
    
    export_data = filtered.copy()
    
    export_columns = {
        'Order_ID': 'Order ID',
        'Order_Date': 'Order Date',
        'Priority': 'Priority Level',
        'Product_Category': 'Product Category',
        'Origin': 'Origin City',
        'Destination': 'Destination City',
        'Distance_KM': 'Distance (KM)',
        'Traffic_Delay_Minutes': 'Traffic Delay (Minutes)',
        'Weather_Impact': 'Weather Impact',
        'weight_kg': 'Weight (KG)',
        'Delivery_Status': 'Delivery Status',
        'Customer_Rating': 'Customer Rating (1-5)',
        'delay_min': 'Total Delay (Minutes)',
        'on_time': 'On-Time Delivery (1=Yes, 0=No)',
        'total_cost': 'Total Cost (₹)',
        'cost_per_km': 'Cost per KM (₹)',
        'co2_kg': 'CO2 Emissions (KG)',
        'status': 'Order Status'
    }
    
    available_cols = {k: v for k, v in export_columns.items() if k in export_data.columns}
    export_df = export_data[list(available_cols.keys())].copy()
    export_df.columns = list(available_cols.values())
    
    if 'Distance (KM)' in export_df.columns:
        export_df['Distance (KM)'] = export_df['Distance (KM)'].round(2)
    if 'Weight (KG)' in export_df.columns:
        export_df['Weight (KG)'] = export_df['Weight (KG)'].round(2)
    if 'Total Cost (₹)' in export_df.columns:
        export_df['Total Cost (₹)'] = export_df['Total Cost (₹)'].round(2)
    if 'Cost per KM (₹)' in export_df.columns:
        export_df['Cost per KM (₹)'] = export_df['Cost per KM (₹)'].round(2)
    if 'CO2 Emissions (KG)' in export_df.columns:
        export_df['CO2 Emissions (KG)'] = export_df['CO2 Emissions (KG)'].round(2)
    
    if 'Order Date' in export_df.columns:
        export_df = export_df.sort_values('Order Date', ascending=False)
    
    summary_df = pd.DataFrame({
        'Order ID': ['SUMMARY STATISTICS'],
        'Order Date': [f'Report Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'],
        'Priority Level': [f'Total Orders: {len(export_df)}'],
        'Product Category': [f'Categories: {export_df["Product Category"].nunique() if "Product Category" in export_df.columns else "N/A"}'],
        'Origin City': [f'Origins: {export_df["Origin City"].nunique() if "Origin City" in export_df.columns else "N/A"}'],
        'Destination City': [f'Destinations: {export_df["Destination City"].nunique() if "Destination City" in export_df.columns else "N/A"}'],
        'Distance (KM)': [f'{export_df["Distance (KM)"].sum():.2f}' if 'Distance (KM)' in export_df.columns else 'N/A'],
        'Traffic Delay (Minutes)': [f'{export_df["Traffic Delay (Minutes)"].sum():.0f}' if 'Traffic Delay (Minutes)' in export_df.columns else 'N/A'],
        'Weather Impact': ['Various'],
        'Weight (KG)': [f'{export_df["Weight (KG)"].sum():.2f}' if 'Weight (KG)' in export_df.columns else 'N/A'],
        'Delivery Status': ['Multiple'],
        'Customer Rating (1-5)': [f'{export_df["Customer Rating (1-5)"].mean():.2f}' if 'Customer Rating (1-5)' in export_df.columns else 'N/A'],
        'Total Delay (Minutes)': [f'{export_df["Total Delay (Minutes)"].sum():.0f}' if 'Total Delay (Minutes)' in export_df.columns else 'N/A'],
        'On-Time Delivery (1=Yes, 0=No)': [f'{export_df["On-Time Delivery (1=Yes, 0=No)"].mean()*100:.1f}%' if 'On-Time Delivery (1=Yes, 0=No)' in export_df.columns else 'N/A'],
        'Total Cost (₹)': [f'{export_df["Total Cost (₹)"].sum():.2f}' if 'Total Cost (₹)' in export_df.columns else 'N/A'],
        'Cost per KM (₹)': [f'{export_df["Cost per KM (₹)"].mean():.2f}' if 'Cost per KM (₹)' in export_df.columns else 'N/A'],
        'CO2 Emissions (KG)': [f'{export_df["CO2 Emissions (KG)"].sum():.2f}' if 'CO2 Emissions (KG)' in export_df.columns else 'N/A'],
        'Order Status': ['Summary']
    })
    
    final_export = pd.concat([summary_df, pd.DataFrame([{}] * 2), export_df], ignore_index=True)
    csv = final_export.to_csv(index=False).encode('utf-8')
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.download_button(
            label="⬇️ Download Complete Report (CSV)",
            data=csv,
            file_name=f"nexgen_logistics_detailed_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    st.markdown(f"""
    <div style='text-align: center; color: #8B92B8; margin-top: 1rem; font-size: 0.9rem;'>
        📊 Report includes {len(export_df)} orders with {len(available_cols)} data columns<br>
        📈 Summary statistics included at top of file
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; padding: 2rem; color: #8B92B8;'>
        <div style='font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem;'>
            🚀 NexGen Logistics Analytics Platform
        </div>
        <div style='font-size: 0.9rem;'>
            Powered by Advanced AI • Real-Time Data Processing • Enterprise-Grade Security
        </div>
        <div style='margin-top: 1rem; font-size: 0.85rem; opacity: 0.7;'>
            © 2025 NexGen Logistics | Version 2.0.1
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Reset button in sidebar
    st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
    st.sidebar.markdown('<div class="filter-section">', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="filter-title">⚙️ Settings</div>', unsafe_allow_html=True)
    
    if st.sidebar.button("🔄 Reset Dashboard", use_container_width=True):
        st.session_state.onboarding_complete = False
        st.session_state.step = 0
        st.session_state.user_prefs = {
            'priorities': [],
            'categories': [],
            'origins': [],
            'time_range': 30,
            'view_mode': 'Executive Overview'
        }
        st.rerun()
    
    st.sidebar.markdown('</div>', unsafe_allow_html=True)
    
    # Active Filters Display
    st.sidebar.markdown('<div class="filter-section">', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="filter-title">🎯 Active Filters</div>', unsafe_allow_html=True)
    st.sidebar.markdown(f"**Priorities:** {len(prefs['priorities'])}", unsafe_allow_html=True)
    st.sidebar.markdown(f"**Categories:** {len(prefs['categories'])}", unsafe_allow_html=True)
    st.sidebar.markdown(f"**Origins:** {len(prefs['origins'])}", unsafe_allow_html=True)
    st.sidebar.markdown(f"**View Mode:** {prefs['view_mode']}", unsafe_allow_html=True)
    st.sidebar.markdown('</div>', unsafe_allow_html=True)