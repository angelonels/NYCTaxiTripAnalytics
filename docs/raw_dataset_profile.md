# Raw Dataset Profile

## Dataset

NYC Yellow Taxi Trip Records — January 2024

## Source Files

- yellow_tripdata_2024-01.parquet
- taxi_zone_lookup.csv

## Shape

- Taxi trip rows: 2,964,624
- Taxi trip columns: 19
- Taxi zone lookup rows: 265
- Taxi zone lookup columns: 4

## Duplicate Rows

- Duplicate taxi trip rows: 0
- Duplicate row percentage: 0.0000%

## Pickup Date Range

- Minimum pickup datetime: 2002-12-31 22:59:39
- Maximum pickup datetime: 2024-02-01 00:01:15

## Dropoff Date Range

- Minimum dropoff datetime: 2002-12-31 23:05:41
- Maximum dropoff datetime: 2024-02-02 13:56:52

## Notes

This profile is generated before cleaning. The cleaning notebook will handle invalid dates, duplicate rows, missing values, impossible trip values, and feature engineering.
