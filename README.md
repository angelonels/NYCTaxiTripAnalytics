# NYC Taxi Trip Analytics

## Project Overview

This project analyzes New York City Yellow Taxi trip records to understand taxi demand, revenue patterns, trip efficiency, payment behavior, and pickup/drop-off location trends.

The project uses Python for data extraction, cleaning, exploratory data analysis, statistical analysis, and final dataset preparation. Tableau will be used later for dashboarding and business insight presentation.

## Sector

Urban Mobility / Transportation Analytics

## Problem Statement

Taxi operators and urban mobility planners need to understand when, where, and how taxi demand is generated in order to improve fleet positioning, revenue planning, and service efficiency.

This project uses NYC Yellow Taxi trip-level data to analyze demand patterns, revenue behavior, trip distance, trip duration, payment methods, tipping behavior, and location-based trends. The final goal is to create a clean analytical dataset, generate business insights, and build a decision-focused Tableau dashboard.

## Dataset Information

### Primary Dataset

**Dataset Name:** NYC TLC Yellow Taxi Trip Records — January 2024  
**Format:** Parquet  
**Source:** NYC Taxi & Limousine Commission Trip Record Data

Dataset link:

```text
https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet
```

Official dataset page:

```text
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
```

Official data dictionary:

```text
https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
```

### Supporting Dataset

**Dataset Name:** NYC Taxi Zone Lookup Table  
**Format:** CSV  
**Purpose:** Used to map pickup and drop-off location IDs to boroughs and zone names.

Dataset link:

```text
https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
```

## Main Data Fields

The Yellow Taxi trip dataset includes fields such as:

- VendorID
- tpep_pickup_datetime
- tpep_dropoff_datetime
- passenger_count
- trip_distance
- RatecodeID
- PULocationID
- DOLocationID
- payment_type
- fare_amount
- extra
- mta_tax
- tip_amount
- tolls_amount
- improvement_surcharge
- total_amount
- congestion_surcharge
- Airport_fee

The Taxi Zone Lookup Table includes:

- LocationID
- Borough
- Zone
- service_zone

## Tools and Technologies

- Python 3.12
- uv
- Jupyter Notebook / JupyterLab
- pandas
- NumPy
- Matplotlib
- SciPy
- Scikit-learn
- Statsmodels
- PyArrow
- Tableau Public
- GitHub

## Repository Structure

```text
NYCTaxiTripAnalytics/
│
├── README.md
├── pyproject.toml
├── uv.lock
│
├── data/
│   ├── raw/                          # raw parquet + zone csv (not tracked)
│   └── processed/                    # cleaned csvs and summary tables
│       ├── cleaning_log.csv
│       ├── daily_demand_summary.csv
│       ├── hourly_demand_summary.csv
│       ├── weekday_demand_summary.csv
│       ├── pickup_borough_summary.csv
│       ├── dropoff_borough_summary.csv
│       ├── top_pickup_zones.csv
│       ├── payment_type_summary.csv
│       ├── distance_bucket_summary.csv
│       ├── eda_kpi_summary.csv
│       ├── eda_correlation_matrix.csv
│       └── ...                       # additional profiling csvs
│
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
│
├── scripts/
│   └── etl_pipeline.py               # standalone cleaning pipeline
│
├── docs/
│   ├── raw_dataset_profile.md
│   └── cleaning_summary.md
│
├── reports/
│   ├── eda_initial_findings.md
│   └── figures/                      # chart pngs from EDA
│
└── tableau/
    ├── screenshots/
    └── dashboard_links.md
```

## Local Project Setup

These instructions explain how to run the project after cloning the repository.

### 1. Clone the Repository

```bash
git clone https://github.com/angelonels/NYCTaxiTripAnalytics.git
cd NYCTaxiTripAnalytics
```

### 2. Install uv

If `uv` is not already installed, install it using:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart the terminal or run:

```bash
exec $SHELL
```

Check installation:

```bash
uv --version
```

### 3. Create and Sync the Python Environment

Run this from the project root:

```bash
uv sync
```

This will create the virtual environment and install all dependencies listed in `pyproject.toml` and `uv.lock`.

### 4. Download the Raw Dataset Files

If the raw dataset files are not already present inside `data/raw/`, download them using:

```bash
curl -L "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet" \
  -o data/raw/yellow_tripdata_2024-01.parquet

curl -L "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv" \
  -o data/raw/taxi_zone_lookup.csv
```

After downloading, the folder should look like this:

```text
data/
└── raw/
    ├── yellow_tripdata_2024-01.parquet
    └── taxi_zone_lookup.csv
```

### 5. Start JupyterLab

Run:

```bash
uv run jupyter lab
```

Open the notebooks from the `notebooks/` folder.

### 6. Run Notebooks in This Order

Run the notebooks in the following sequence:

```text
01_extraction.ipynb
02_cleaning.ipynb
03_eda.ipynb
04_statistical_analysis.ipynb
05_final_load_prep.ipynb
```

The expected workflow is:

1. Load and inspect raw data.
2. Clean and standardize the dataset.
3. Perform exploratory data analysis.
4. Run statistical analysis.
5. Prepare final processed files for Tableau.

### 7. Expected Data Outputs

After running the notebooks, processed summary CSVs and chart PNGs are saved to:

```text
data/processed/       # summary tables and cleaned csvs
reports/figures/      # chart outputs from EDA
docs/                 # dataset profile and cleaning log
reports/              # initial EDA findings
```

The cleaned parquet file is generated locally but excluded from git due to size (~100 MB).

## Project Workflow

The project follows this workflow:

1. Dataset sourcing
2. Data extraction
3. Data cleaning and preprocessing
4. Feature engineering
5. Exploratory data analysis
6. Statistical analysis
7. Tableau dashboard preparation
8. Business insights and recommendations

## Key Performance Indicators

The analysis covers the following KPIs:

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

## Notes

- The raw dataset should remain unchanged inside `data/raw/`.
- Cleaned and transformed files should be saved only inside `data/processed/`.
- All notebooks should be run in order.
- The project uses `uv` instead of `pip` for dependency and environment management.