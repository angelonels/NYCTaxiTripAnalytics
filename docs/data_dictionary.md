# Data Dictionary

## Project

NYC Taxi Trip Analytics

## Main Tableau Dataset

`data/processed/tableau_taxi_trips_sample.csv`

## Field Descriptions

| Column Name | Data Type | Description | Example Use |
|---|---|---|---|
| pickup_datetime | datetime | Date and time when the taxi trip started. | Time trend analysis and filtering. |
| dropoff_datetime | datetime | Date and time when the taxi trip ended. | Trip duration calculation. |
| pickup_date | date | Date of taxi pickup. | Daily demand and revenue trend analysis. |
| pickup_hour | integer | Hour of day when the trip started, from 0 to 23. | Peak demand hour analysis. |
| pickup_day_name | categorical | Day name of trip pickup. | Weekday demand comparison. |
| is_weekend | boolean | Boolean flag identifying Saturday and Sunday trips. | Weekday vs weekend comparison. |
| vendor_name | categorical | Readable taxi technology vendor name. | Vendor-level trip comparison. |
| rate_code_label | categorical | Readable rate category such as Standard rate, JFK, Newark, or Negotiated fare. | Fare type analysis. |
| payment_type_label | categorical | Readable payment type such as Credit card or Cash. | Payment and tipping behavior analysis. |
| passenger_count_clean | integer | Cleaned passenger count field. | Passenger group analysis. |
| passenger_count_group | categorical | Passenger count grouped as Solo, Small group, Large group, Unknown, or Zero reported. | Segmented demand analysis. |
| trip_distance | numeric | Trip distance in miles. | Distance and revenue efficiency analysis. |
| trip_duration_minutes | numeric | Trip duration in minutes. | Duration and congestion-related analysis. |
| fare_amount | numeric | Base fare charged for the taxi trip. | Fare analysis. |
| tip_amount | numeric | Recorded tip amount for the trip. | Tip behavior analysis. |
| total_amount | numeric | Total amount charged to passengers including fare, tips, taxes, surcharges, tolls, and fees. | Revenue analysis. |
| revenue_per_mile | numeric | Total amount divided by trip distance. | Trip revenue efficiency analysis. |
| fare_per_minute | numeric | Fare amount divided by trip duration in minutes. | Trip time efficiency analysis. |
| tip_percentage | numeric | Tip amount divided by fare amount, expressed as a percentage. | Tip behavior analysis. |
| distance_bucket | categorical | Categorical grouping of trip distance. | Short, medium, and long trip analysis. |
| duration_bucket | categorical | Categorical grouping of trip duration. | Duration segment analysis. |
| pickup_borough | categorical | NYC borough where the trip started. | Origin demand analysis. |
| pickup_zone | categorical | Taxi zone where the trip started. | High-demand pickup zone analysis. |
| dropoff_borough | categorical | NYC borough where the trip ended. | Destination demand analysis. |
| dropoff_zone | categorical | Taxi zone where the trip ended. | High-demand destination zone analysis. |
| is_high_value_trip | boolean | Flag for trips above the 99th percentile of total amount. | Outlier and premium trip analysis. |
| is_long_distance_trip | boolean | Flag for trips above the 99th percentile of trip distance. | Long-distance trip analysis. |
| is_long_duration_trip | boolean | Flag for trips above the 99th percentile of trip duration. | Long-duration trip analysis. |

## Notes

The dataset was prepared from NYC Yellow Taxi Trip Records for January 2024. The raw file was not modified. Cleaning, feature engineering, and Tableau preparation were completed using Python notebooks.
