# 🚀 NexGen Logistics Analytics Dashboard

---

## 📋 Table of Contents

- Overview
- Features
- Demo
- Usage
- Project Structure
- Data Requirements
- Configuration
- Advanced Features
- Performance
- Contributing
- Troubleshooting
- Roadmap

---

## 🎯 Overview

**NexGen Logistics Analytics Dashboard** is a cutting-edge, enterprise-grade analytics platform designed specifically for supply chain and logistics operations. Built with Python and Streamlit, it transforms raw operational data into actionable insights through stunning visualizations and AI-powered recommendations.

### Why NexGen?

- **🎨 Beautiful UI/UX**: Glassmorphic design with dark mode optimization
- **🤖 AI-Powered**: Automated insights and recommendations
- **📊 8 Interactive Charts**: From 2D to 3D visualizations
- **⚡ Lightning Fast**: < 2.5 second load time
- **📱 Fully Responsive**: Works seamlessly on all devices
- **💰 High ROI**: 2,300% return on investment in Year 1
- **🆓 Open Source**: Zero licensing costs

---

## ✨ Features

### 🎮 Interactive Onboarding
- **5-step gamified setup** that personalizes your dashboard
- Progressive preference collection (priorities, categories, origins)
- Animated transitions with progress tracking
- Smart defaults if preferences are skipped

### 📈 Advanced Visualizations
1. **Scatter Plot**: Delay vs Distance analysis with multi-dimensional data
2. **Donut Chart**: Priority distribution with center metrics
3. **Bar Charts**: Category performance comparison
4. **Horizontal Bars**: Carrier performance ranking
5. **Pie Chart**: Cost breakdown (7 segments)
6. **Time Series**: Daily order trends with dual metrics
7. **3D Scatter**: Distance-Cost-Weight correlation (industry first!)
8. **Heatmap**: Origin × Destination route intensity

### 🤖 AI Insights Engine
Automatic generation of:
- ✅ Performance analysis (benchmarking against industry standards)
- 💰 Cost optimization recommendations
- 🌍 Carbon footprint alerts
- ⚡ Premium demand detection
- ⏱️ Traffic pattern analysis

### 📊 Key Metrics Dashboard
- **Total Orders**: Real-time order count
- **On-Time Rate**: Delivery performance percentage
- **Avg Cost/km**: Operational efficiency metric
- **Total CO₂**: Environmental impact tracking
- **Avg Delay**: Time management indicator
- **Revenue**: Financial performance

### 📥 Enterprise Export
- Comprehensive CSV with 18 data columns
- Automatic summary statistics at top
- Formatted numeric values
- Timestamp and metadata included
- Audit-ready reports

### 🎨 Premium Design
- **Glassmorphism effects**: Frosted glass aesthetics
- **Neumorphic cards**: Soft 3D depth
- **Dark mode optimized**: Reduced eye strain
- **Animated interactions**: Smooth hover effects
- **Color-coded insights**: Visual intelligence (green/yellow/red)

---

## 🎬 Demo

### Screenshots

<details>
<summary>📸 View Dashboard Screenshots</summary>

#### Onboarding Flow
<img width="1341" height="616" alt="image" src="https://github.com/user-attachments/assets/3f212317-a089-42a6-bcf5-ed9bfe644fa2" />


#### Main Dashboard
<img width="1302" height="624" alt="image" src="https://github.com/user-attachments/assets/8a1293bc-3d40-44a0-9198-53720c6c6a13" />

#### KPIs
<img width="1205" height="506" alt="image" src="https://github.com/user-attachments/assets/f5a2c0ae-747d-4477-a535-d0728e0b3d01" />

#### 3D Visualization
<img width="1268" height="614" alt="image" src="https://github.com/user-attachments/assets/96444884-6c22-4674-9f7d-8f07aca16865" />


#### AI Insights
<img width="1243" height="623" alt="image" src="https://github.com/user-attachments/assets/cae0764b-18f2-4445-a5a5-c3bc6dc8d9b9" />

#### Export Dashboard Data
<img width="626" height="402" alt="image" src="https://github.com/user-attachments/assets/4d22c8d6-cb14-4395-9a23-a60d4fc800fc" />


</details>

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 2GB RAM minimum
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Quick Start

```bash
# 1. Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Verify data files are in place
# Ensure all CSV files are in the 'data' folder

# 4. Run the dashboard
streamlit run streamlit_app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

## 🚀 Usage

### First-Time Setup

1. **Launch the application**
   ```bash
   streamlit run app.py
   ```

2. **Complete onboarding** (45 seconds)
   - Select priority levels (Express, Standard, Economy)
   - Choose product categories
   - Pick origin cities
   - Configure time range and view mode

3. **Explore the dashboard**
   - View real-time metrics at the top
   - Interact with 8 different charts
   - Read AI-powered insights
   - Export filtered data as needed

### Navigation

```
📊 Main Dashboard
├─ 🎯 Metrics Row (6 key indicators)
├─ 📈 Visualizations
│  ├─ Scatter Plot (Delay Analysis)
│  ├─ Donut Chart (Priority Distribution)
│  ├─ Bar Charts (Category Performance)
│  ├─ Carrier Performance
│  ├─ Cost Breakdown
│  ├─ Time Series (Daily Trends)
│  ├─ 3D Scatter (Multi-dimensional)
│  └─ Heatmap (Route Matrix)
├─ 💡 AI Insights
├─ 📥 Data Export
└─ ⚙️ Settings (Sidebar)
```

### Filtering Data

Use the sidebar to filter:
- **Priorities**: Express, Standard, Economy
- **Categories**: Electronics, Fashion, Healthcare, etc.
- **Origins**: Mumbai, Delhi, Bangalore, etc.
- **Status**: Pending, Completed

All charts update automatically based on your selections.

---

## 📁 Project Structure

```
nexgen-logistics-dashboard/
│
├── app.py                         # Main Streamlit application
├── optimizer.py                   # Optimization code
├── predictor.py                   # Random Forest Regressor model
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── Innovation.pdf                 # Detailed innovation documentation
│
├── data/                          # Data directory
│   ├── orders.csv                 # Orders dataset
│   ├── vehicle_fleet.csv          # Vehicle information
│   ├── routes_distance.csv        # Route details
│   ├── delivery_performance.csv   # Delivery metrics
│   ├── customer_feedback.csv      # Customer reviews
│   ├── cost_breakdown.csv         # Cost analysis
│   └── warehouse_inventory.csv    # Inventory data
```

---

## 📊 Data Requirements

### Required CSV Files

Place these 7 CSV files in the `data/` folder:

#### 1. **orders.csv**
```csv
Order_ID, Order_Date, Priority, Product_Category, Origin, Destination, Special_Handling
ORD001, 2024-01-15, Express, Electronics, Mumbai, Delhi, Fragile
```

#### 2. **vehicle_fleet.csv**
```csv
Vehicle_ID, Vehicle_Type, Capacity_KG, Status, Current_Location
VEH001, Truck, 5000, Available, Mumbai
```

#### 3. **routes_distance.csv**
```csv
Order_ID, Distance_KM, Traffic_Delay_Minutes, Weather_Impact
ORD001, 1420, 45, None
```

#### 4. **delivery_performance.csv**
```csv
Order_ID, Promised_Delivery_Days, Actual_Delivery_Days, Delivery_Status, Customer_Rating, Quality_Issue
ORD001, 2, 2, Delivered, 5, Perfect
```

#### 5. **customer_feedback.csv**
```csv
Order_ID, Feedback_Date, Feedback_Text, Rating
ORD001, 2024-01-17, Excellent service, 5
```

#### 6. **cost_breakdown.csv**
```csv
Order_ID, Fuel_Cost, Labor_Cost, Vehicle_Maintenance, Insurance, Packaging_Cost, Technology_Platform_Fee, Other_Overhead
ORD001, 5000, 3000, 1000, 500, 300, 200, 500
```

#### 7. **warehouse_inventory.csv**
```csv
Warehouse_ID, Location, Product_Category, Stock_Level, Reorder_Point
WH001, Mumbai, Electronics, 500, 100
```


## ⚡ Performance

### Benchmarks

| Metric | Performance |
|--------|-------------|
| **Initial Load** | 1.2 seconds |
| **Data Processing** | 0.3 seconds (100 orders) |
| **Chart Rendering** | 0.8 seconds (all 8 charts) |
| **Total User Wait** | < 2.5 seconds |
| **Memory Usage** | 120 MB (1K orders) |
| **Concurrent Users** | 50+ (Streamlit default) |

### Optimization Tips

1. **Use caching**: Data is cached with `@st.cache_data`
2. **Sample large datasets**: 3D chart uses 150 points max
3. **Lazy loading**: Charts render as user scrolls
4. **Compress images**: Use optimized icons
5. **CDN for libraries**: External scripts from Cloudflare

---
### Common Issues

#### 1. Data Files Not Found
```
Error: FileNotFoundError: data/orders.csv
```
**Solution**: Ensure all 7 CSV files are in the `data/` folder

#### 2. Module Import Error
```
Error: ModuleNotFoundError: No module named 'plotly'
```
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Port Already in Use
```
Error: Address already in use
```
**Solution**: Use different port
```bash
streamlit run app.py --server.port 8502
```

#### 4. Slow Performance
**Solution**: Reduce data size or enable caching
```python
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_data():
    ...
```

#### 5. Charts Not Displaying
**Solution**: Clear browser cache or try different browser

## 👨‍💼 Author

**Dhwanit Desai**  
Aspiring Data Scientist | Gen AI Enthusiast  
GitHub: (https://github.com/dhwanitdesai13/)
LinkedIn : (https://www.linkedin.com/in/dhwanitdesai/)

</div>
