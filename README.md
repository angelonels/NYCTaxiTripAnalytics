<p align="center">
  <img src="assets/logo.png" alt="NYC Taxi Trip Analytics Logo" width="400">
</p>

# NYC Taxi Trip Analytics

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![uv](https://img.shields.io/badge/managed%20by-uv-arc.svg)](https://github.com/astral-sh/uv)
[![Tableau](https://img.shields.io/badge/Visualization-Tableau-orange.svg)](https://public.tableau.com/)

---

## Project Overview

> [!NOTE]
> This project analyzes New York City Yellow Taxi trip records to understand taxi demand, revenue patterns, trip efficiency, payment behavior, and pickup/drop-off location trends.

The project uses **Python** for data extraction, cleaning, exploratory data analysis, statistical analysis, and final dataset preparation. **Tableau** will be used later for dashboarding and business insight presentation.

### Sector
Urban Mobility / Transportation Analytics

### Problem Statement
Taxi operators and urban mobility planners need to understand when, where, and how taxi demand is generated in order to improve fleet positioning, revenue planning, and service efficiency.

This project uses NYC Yellow Taxi trip-level data to analyze:
- Demand patterns & Revenue behavior
- Trip distance & Duration
- Payment methods & Tipping behavior
- Location-based trends

**Goal:** Create a clean analytical dataset, generate business insights, and build a decision-focused Tableau dashboard.

---

## Dataset Information

| Feature | Primary Dataset | Supporting Dataset |
| :--- | :--- | :--- |
| **Name** | NYC TLC Yellow Taxi Trip Records | NYC Taxi Zone Lookup Table |
| **Period** | January 2024 | N/A |
| **Format** | Parquet | CSV |
| **Source** | NYC Taxi & Limousine Commission | NYC Taxi & Limousine Commission |
| **Purpose** | Core trip record data | Mapping location IDs to Boroughs/Zones |

### Dataset Links
- [Primary Dataset Link](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet)
- [Official Dataset Page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [Official Data Dictionary](https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf)
- [Zone Lookup Table Link](https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv)

---

## Main Data Fields

<details>
<summary><b>Click to expand Yellow Taxi Trip Fields</b></summary>

- `VendorID`
- `tpep_pickup_datetime`
- `tpep_dropoff_datetime`
- `passenger_count`
- `trip_distance`
- `RatecodeID`
- `PULocationID`
- `DOLocationID`
- `payment_type`
- `fare_amount`
- `extra`
- `mta_tax`
- `tip_amount`
- `tolls_amount`
- `improvement_surcharge`
- `total_amount`
- `congestion_surcharge`
- `Airport_fee`
</details>

<details>
<summary><b>Click to expand Taxi Zone Lookup Fields</b></summary>

- `LocationID`
- `Borough`
- `Zone`
- `service_zone`
</details>

---

## Tools and Technologies

| Category | Tools |
| :--- | :--- |
| **Runtime** | Python 3.12, uv |
| **Environment** | Jupyter Notebook / JupyterLab |
| **Data Processing** | pandas, NumPy, PyArrow |
| **Analysis** | SciPy, Scikit-learn, Statsmodels |
| **Visualization** | Matplotlib, Tableau Public |
| **Version Control** | GitHub |

---

## Repository Structure

```text
NYCTaxiTripAnalytics/
├── assets/                       # Branding and logo files
├── data/
│   ├── raw/                      # Raw parquet + zone csv (not tracked)
│   └── processed/                # Cleaned CSVs and summary tables for analysis
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
├── scripts/
│   └── etl_pipeline.py               # Standalone cleaning pipeline
├── docs/
│   ├── raw_dataset_profile.md
│   ├── cleaning_summary.md
│   ├── data_dictionary.md
│   ├── final_load_summary.md
│   └── tableau_data_files.md
├── reports/
│   ├── project_report.md
│   ├── eda_initial_findings.md
│   ├── statistical_analysis_findings.md
│   └── figures/                      # Chart PNGs from EDA
└── tableau/
    ├── Final2.twbx                   # Tableau workbook file
    ├── dashboard_links.md
    └── screenshots/
```

---

## Local Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/angelonels/NYCTaxiTripAnalytics.git
cd NYCTaxiTripAnalytics
```

### 2. Install uv
If `uv` is not already installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
exec $SHELL
```

### 3. Setup Environment
```bash
uv sync
```

### 4. Download Raw Dataset
```bash
curl -L "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet" -o data/raw/yellow_tripdata_2024-01.parquet
curl -L "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv" -o data/raw/taxi_zone_lookup.csv
```

### 5. Start JupyterLab
```bash
uv run jupyter lab
```

---

## Project Workflow

```diff
+ 01. Dataset Sourcing & Extraction
+ 02. Data Cleaning & Preprocessing
+ 03. Feature Engineering
+ 04. Exploratory Data Analysis (EDA)
+ 05. Statistical Analysis
+ 06. Tableau Dashboard Preparation
+ 07. Business Insights & Recommendations
```

### Notebook Execution Order:
1. `01_extraction.ipynb`
2. `02_cleaning.ipynb`
3. `03_eda.ipynb`
4. `04_statistical_analysis.ipynb`
5. `05_final_load_prep.ipynb`

---

## Key Performance Indicators

- Total Trips
- Total Revenue
- Average Fare Amount
- Average Trip Distance
- Average Trip Duration
- Revenue per Mile
- Average Tip Amount
- Tip Percentage
- Peak Demand Hour
- Top Pickup Borough
- Top Drop-off Borough
- Payment Type Distribution

---

## Notes

- The raw dataset should remain unchanged inside `data/raw/`.
- Cleaned and transformed files should be saved only inside `data/processed/`.
- All notebooks should be run in order.
- The project uses `uv` instead of `pip` for dependency and environment management.