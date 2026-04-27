# Cleaning Summary

## Input Dataset

- Raw file: yellow_tripdata_2024-01.parquet
- Initial rows: 2,964,624

## Output Dataset

- Cleaned file: cleaned_yellow_taxi_jan_2024.parquet
- Final rows: 2,868,035
- Final columns: 47

## Cleaning Steps

| step_name                        |   rows_before |   rows_after |   rows_removed |   removal_percentage | description                                                                          |
|:---------------------------------|--------------:|-------------:|---------------:|---------------------:|:-------------------------------------------------------------------------------------|
| remove_exact_duplicates          |       2964624 |      2964624 |              0 |               0      | Removed exact duplicate trip records.                                                |
| remove_invalid_timestamps        |       2964624 |      2963754 |            870 |               0.0293 | Removed records with missing timestamps or drop-off times earlier than pickup times. |
| restrict_to_january_2024_pickups |       2963754 |      2963736 |             18 |               0.0006 | Kept only trips with pickup timestamps in January 2024.                              |
| remove_impossible_trip_values    |       2963736 |      2868035 |          95701 |               3.2291 | Removed trips with impossible distance, duration, fare, or total amount values.      |

## Major Features Created

- trip_duration_minutes
- pickup_date
- pickup_hour
- pickup_day_name
- is_weekend
- revenue_per_mile
- fare_per_minute
- tip_percentage
- distance_bucket
- duration_bucket
- vendor_name
- rate_code_label
- payment_type_label
- pickup_borough
- pickup_zone
- dropoff_borough
- dropoff_zone
- is_high_value_trip
- is_long_distance_trip
- is_long_duration_trip

## Notes

The raw dataset was not modified. All cleaning was performed through a reproducible Python workflow.
