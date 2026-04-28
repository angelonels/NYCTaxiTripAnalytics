# Tableau Data Files

Final datasets for Tableau dashboard development.

## Recommended Main File

### `tableau_taxi_trips_sample.csv`

Use this row-level sample for Tableau Public dashboards with filters, KPIs, maps, time views, payment analysis, and trip behavior analysis.

## Aggregated Summary Files

### `tableau_executive_kpi_summary.csv`

Used for executive KPI cards.

### `tableau_daily_summary.csv`

Used for daily demand and revenue trend charts.

### `tableau_hourly_summary.csv`

Used for peak-hour analysis.

### `tableau_weekday_summary.csv`

Used for weekday and weekend comparison.

### `tableau_pickup_borough_summary.csv`

Used for origin borough analysis.

### `tableau_dropoff_borough_summary.csv`

Used for destination borough analysis.

### `tableau_pickup_zone_summary.csv`

Used for detailed pickup zone analysis.

### `tableau_dropoff_zone_summary.csv`

Used for detailed destination zone analysis.

### `tableau_borough_flow_summary.csv`

Used for pickup borough to drop-off borough movement analysis.

### `tableau_zone_flow_summary.csv`

Used for pickup zone to drop-off zone flow analysis. Only flows with at least 50 trips are included.

### `tableau_payment_type_summary.csv`

Used for payment and tip behavior analysis.

### `tableau_distance_bucket_summary.csv`

Used for trip distance segment analysis.

### `tableau_duration_bucket_summary.csv`

Used for trip duration segment analysis.

### `tableau_hour_weekday_heatmap.csv`

Used for demand heatmaps by pickup hour and day of week.

### `tableau_outlier_flag_summary.csv`

Used for high-value, long-distance, and long-duration trip flag summaries.

## Instructor Preview File

### `instructor_preview_sample_10000.csv`

Small row-level sample for quick manual inspection.

## Notes

- Raw data remains unchanged in `data/raw/`.
- Tableau-ready files are stored in `data/processed/`.
- The main dashboard file is `tableau_taxi_trips_sample.csv`.
