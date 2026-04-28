# Final Load Preparation Summary

## Purpose

This document summarizes the final datasets prepared for Tableau dashboard development.

## Source Dataset

- Cleaned input file: `data/processed/cleaned_yellow_taxi_jan_2024.parquet`
- Cleaned rows: 2,868,035
- Cleaned columns: 47

## Main Tableau File

- `data/processed/tableau_taxi_trips_sample.csv`
- Rows: 300,000
- Purpose: Main row-level file for Tableau Public dashboard development.

## Files Created

| file_name                           |   rows |   columns |
|:------------------------------------|-------:|----------:|
| tableau_taxi_trips_sample.csv       | 300000 |        39 |
| tableau_executive_kpi_summary.csv   |     13 |         3 |
| tableau_daily_summary.csv           |     31 |        10 |
| tableau_hourly_summary.csv          |     24 |        10 |
| tableau_weekday_summary.csv         |      7 |        12 |
| tableau_pickup_borough_summary.csv  |      7 |        12 |
| tableau_dropoff_borough_summary.csv |      7 |        12 |
| tableau_pickup_zone_summary.csv     |    257 |        11 |
| tableau_dropoff_zone_summary.csv    |    260 |        11 |
| tableau_borough_flow_summary.csv    |     46 |         9 |
| tableau_zone_flow_summary.csv       |   3885 |        10 |
| tableau_payment_type_summary.csv    |      5 |        13 |
| tableau_distance_bucket_summary.csv |      6 |        11 |
| tableau_duration_bucket_summary.csv |      6 |        10 |
| tableau_hour_weekday_heatmap.csv    |    168 |         8 |
| tableau_outlier_flag_summary.csv    |      3 |         3 |
| instructor_preview_sample_10000.csv |  10000 |        39 |
| final_tableau_data_dictionary.csv   |     28 |         4 |

## Recommended Tableau Dashboard Sections

1. Executive KPI Overview
2. Demand by Hour and Day
3. Revenue and Fare Analysis
4. Pickup and Drop-off Borough Analysis
5. Zone-Level Demand Analysis
6. Payment and Tip Behavior
7. Trip Distance and Duration Efficiency
8. Business Recommendation View

## Notes

The final Tableau files are exported in CSV format for compatibility and easy inspection. Aggregated files are provided to improve Tableau performance and simplify dashboard building.
