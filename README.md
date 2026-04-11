# Quality & PMO Optimization

![Dashboard](docs/dashboard.png)

## Overview

This project simulates a real-world maritime operations analytics system designed to improve operational efficiency, reduce delays, and optimize profitability through data-driven insights.

It is built as an end-to-end **data analytics and decision-support system** that processes ship performance data and transforms it into actionable business recommendations.

### Key objectives:
- Analyze profitability across ship types  
- Identify operational inefficiencies  
- Detect delay patterns across routes  
- Support data-driven decision-making  

---

## Key Features

### KPI Engine
- Profit calculation per voyage  
- Efficiency measurement (nm per kWh)  
- Delay detection and tracking  

### Analytics & Insights
- Profit comparison across ship types  
- Delay analysis by route type  
- Efficiency evaluation by engine type  

### Automated Insights
- Best and worst performing ship categories  
- Most delayed routes  
- Most efficient engine configurations  

### Optimization Engine
- Generates actionable recommendations:
  - Improve low-performing ship types  
  - Reduce delays on inefficient routes  
  - Optimize engine selection  

### Interactive Dashboard
Built using **Streamlit**:
- Real-time KPI monitoring  
- Interactive visualizations  
- Filtering by ship, route, and engine type  
- Business-oriented insights and recommendations  

---

## Tech Stack

- Python  
- Pandas  
- Plotly  
- Streamlit  
- Scikit-learn (for extensibility)  

---

## Project Structure

```
quality-pmo-optimization-system/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample_shipping_data.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_kpi_analysis.ipynb
│   ├── 03_process_analysis.ipynb
│
├── src/
│   ├── data/
│   │   ├── load_data.py
│   │   ├── preprocess.py
│   │
│   ├── analytics/
│   │   ├── kpi_tracker.py
│   │   ├── delay_analysis.py
│   │   ├── root_cause.py
│   │
│   ├── pmo/
│   │   ├── project_tracker.py
│   │   ├── milestone_manager.py
│   │   ├── stakeholder_simulation.py
│   │
│   ├── process/
│   │   ├── current_state.py
│   │   ├── future_state.py
│   │   ├── optimization.py
│   │
│   └── utils/
│       ├── config.py
│       ├── logger.py
│
├── dashboard/
│   ├── app.py
│   └── components/
│
├── reports/
│   ├── project_status_report.md
│   ├── process_improvement_report.md
│
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   ├── stakeholder_map.md
│
└── tests/
    ├── test_kpi.py
    ├── test_pipeline.py
```

---

## How to Run

### 1. Create a virtual environment
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the dashboard
```bash
streamlit run dashboard/app.py
```

---

## Example Insights

- Fish Carrier shows the highest profitability  
- Tanker demonstrates comparatively lower performance  
- Long-haul routes experience the highest delays  
- Steam Turbine engines provide the best efficiency  

---

## Future Improvements

- Integration with real-world maritime datasets  
- Machine learning for predictive analytics  
- Automated reporting using LLMs  
- Deployment with live data pipelines  

---

## Author

**Md Abrar Fahim**  
B.Sc. Information Engineering — HAW Hamburg
