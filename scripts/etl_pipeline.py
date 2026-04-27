from pathlib import Path
import pandas as pd
import numpy as np


def get_project_root() -> Path:
    current_path = Path.cwd()
    if current_path.name in {"notebooks", "scripts"}:
        return current_path.parent
    return current_path


def load_raw_data(project_root: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    raw_data_dir = project_root / "data" / "raw"

    trip_data_path = raw_data_dir / "yellow_tripdata_2024-01.parquet"
    zone_lookup_path = raw_data_dir / "taxi_zone_lookup.csv"

    taxi_trips = pd.read_parquet(trip_data_path)
    taxi_zones = pd.read_csv(zone_lookup_path)

    return taxi_trips, taxi_zones


def standardize_columns(taxi_trips: pd.DataFrame, taxi_zones: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    trip_column_mapping = {
        "VendorID": "vendor_id",
        "tpep_pickup_datetime": "pickup_datetime",
        "tpep_dropoff_datetime": "dropoff_datetime",
        "passenger_count": "passenger_count",
        "trip_distance": "trip_distance",
        "RatecodeID": "rate_code_id",
        "store_and_fwd_flag": "store_and_fwd_flag",
        "PULocationID": "pickup_location_id",
        "DOLocationID": "dropoff_location_id",
        "payment_type": "payment_type",
        "fare_amount": "fare_amount",
        "extra": "extra",
        "mta_tax": "mta_tax",
        "tip_amount": "tip_amount",
        "tolls_amount": "tolls_amount",
        "improvement_surcharge": "improvement_surcharge",
        "total_amount": "total_amount",
        "congestion_surcharge": "congestion_surcharge",
        "Airport_fee": "airport_fee",
    }

    zone_column_mapping = {
        "LocationID": "location_id",
        "Borough": "borough",
        "Zone": "zone",
        "service_zone": "service_zone",
    }

    return taxi_trips.rename(columns=trip_column_mapping), taxi_zones.rename(columns=zone_column_mapping)


def clean_taxi_trips(taxi_trips: pd.DataFrame, taxi_zones: pd.DataFrame) -> pd.DataFrame:
    taxi_trips = taxi_trips.drop_duplicates().copy()

    taxi_trips["pickup_datetime"] = pd.to_datetime(taxi_trips["pickup_datetime"], errors="coerce")
    taxi_trips["dropoff_datetime"] = pd.to_datetime(taxi_trips["dropoff_datetime"], errors="coerce")

    taxi_trips = taxi_trips[
        taxi_trips["pickup_datetime"].notna()
        & taxi_trips["dropoff_datetime"].notna()
        & (taxi_trips["dropoff_datetime"] > taxi_trips["pickup_datetime"])
    ].copy()

    taxi_trips = taxi_trips[
        (taxi_trips["pickup_datetime"] >= pd.Timestamp("2024-01-01"))
        & (taxi_trips["pickup_datetime"] < pd.Timestamp("2024-02-01"))
    ].copy()

    taxi_trips["trip_duration_minutes"] = (
        taxi_trips["dropoff_datetime"] - taxi_trips["pickup_datetime"]
    ).dt.total_seconds() / 60

    taxi_trips = taxi_trips[
        (taxi_trips["trip_distance"] > 0)
        & (taxi_trips["trip_duration_minutes"] > 0)
        & (taxi_trips["trip_duration_minutes"] <= 180)
        & (taxi_trips["fare_amount"] >= 0)
        & (taxi_trips["total_amount"] >= 0)
    ].copy()

    taxi_trips["passenger_count_clean"] = taxi_trips["passenger_count"]
    taxi_trips.loc[
        (taxi_trips["passenger_count_clean"] < 0) | (taxi_trips["passenger_count_clean"] > 6),
        "passenger_count_clean",
    ] = np.nan

    taxi_trips["passenger_count_group"] = np.select(
        [
            taxi_trips["passenger_count_clean"].isna(),
            taxi_trips["passenger_count_clean"] == 0,
            taxi_trips["passenger_count_clean"] == 1,
            taxi_trips["passenger_count_clean"].between(2, 3),
            taxi_trips["passenger_count_clean"].between(4, 6),
        ],
        [
            "Unknown",
            "Zero reported",
            "Solo",
            "Small group",
            "Large group",
        ],
        default="Unknown",
    )

    taxi_trips["passenger_count_clean"] = taxi_trips["passenger_count_clean"].fillna(0).astype(int)

    vendor_mapping = {
        1: "Creative Mobile Technologies",
        2: "VeriFone Inc.",
    }

    rate_code_mapping = {
        1: "Standard rate",
        2: "JFK",
        3: "Newark",
        4: "Nassau or Westchester",
        5: "Negotiated fare",
        6: "Group ride",
        99: "Unknown",
    }

    payment_type_mapping = {
        0: "Unknown",
        1: "Credit card",
        2: "Cash",
        3: "No charge",
        4: "Dispute",
        5: "Unknown",
        6: "Voided trip",
    }

    taxi_trips["vendor_name"] = taxi_trips["vendor_id"].map(vendor_mapping).fillna("Unknown")
    taxi_trips["rate_code_label"] = taxi_trips["rate_code_id"].map(rate_code_mapping).fillna("Unknown")
    taxi_trips["payment_type_label"] = taxi_trips["payment_type"].map(payment_type_mapping).fillna("Unknown")
    taxi_trips["store_and_fwd_flag"] = taxi_trips["store_and_fwd_flag"].fillna("Unknown")

    taxi_trips["pickup_date"] = taxi_trips["pickup_datetime"].dt.date
    taxi_trips["pickup_year"] = taxi_trips["pickup_datetime"].dt.year
    taxi_trips["pickup_month"] = taxi_trips["pickup_datetime"].dt.month
    taxi_trips["pickup_day"] = taxi_trips["pickup_datetime"].dt.day
    taxi_trips["pickup_hour"] = taxi_trips["pickup_datetime"].dt.hour
    taxi_trips["pickup_day_name"] = taxi_trips["pickup_datetime"].dt.day_name()
    taxi_trips["pickup_day_of_week"] = taxi_trips["pickup_datetime"].dt.dayofweek
    taxi_trips["is_weekend"] = taxi_trips["pickup_day_of_week"].isin([5, 6])

    taxi_trips["revenue_per_mile"] = np.where(
        taxi_trips["trip_distance"] > 0,
        taxi_trips["total_amount"] / taxi_trips["trip_distance"],
        np.nan,
    )

    taxi_trips["fare_per_minute"] = np.where(
        taxi_trips["trip_duration_minutes"] > 0,
        taxi_trips["fare_amount"] / taxi_trips["trip_duration_minutes"],
        np.nan,
    )

    taxi_trips["tip_percentage"] = np.where(
        taxi_trips["fare_amount"] > 0,
        taxi_trips["tip_amount"] / taxi_trips["fare_amount"] * 100,
        0,
    )

    taxi_trips["distance_bucket"] = pd.cut(
        taxi_trips["trip_distance"],
        bins=[0, 1, 3, 5, 10, 20, np.inf],
        labels=["0-1 miles", "1-3 miles", "3-5 miles", "5-10 miles", "10-20 miles", "20+ miles"],
        include_lowest=True,
    )

    taxi_trips["duration_bucket"] = pd.cut(
        taxi_trips["trip_duration_minutes"],
        bins=[0, 5, 10, 20, 30, 60, np.inf],
        labels=["0-5 min", "5-10 min", "10-20 min", "20-30 min", "30-60 min", "60+ min"],
        include_lowest=True,
    )

    pickup_zones = taxi_zones.rename(columns={
        "location_id": "pickup_location_id",
        "borough": "pickup_borough",
        "zone": "pickup_zone",
        "service_zone": "pickup_service_zone",
    })

    dropoff_zones = taxi_zones.rename(columns={
        "location_id": "dropoff_location_id",
        "borough": "dropoff_borough",
        "zone": "dropoff_zone",
        "service_zone": "dropoff_service_zone",
    })

    taxi_trips = taxi_trips.merge(pickup_zones, on="pickup_location_id", how="left")
    taxi_trips = taxi_trips.merge(dropoff_zones, on="dropoff_location_id", how="left")

    location_label_columns = [
        "pickup_borough",
        "pickup_zone",
        "pickup_service_zone",
        "dropoff_borough",
        "dropoff_zone",
        "dropoff_service_zone",
    ]

    for column_name in location_label_columns:
        taxi_trips[column_name] = taxi_trips[column_name].fillna("Unknown")

    taxi_trips["is_high_value_trip"] = taxi_trips["total_amount"] > taxi_trips["total_amount"].quantile(0.99)
    taxi_trips["is_long_distance_trip"] = taxi_trips["trip_distance"] > taxi_trips["trip_distance"].quantile(0.99)
    taxi_trips["is_long_duration_trip"] = taxi_trips["trip_duration_minutes"] > taxi_trips["trip_duration_minutes"].quantile(0.99)

    return taxi_trips


def main() -> None:
    project_root = get_project_root()
    processed_data_dir = project_root / "data" / "processed"
    processed_data_dir.mkdir(parents=True, exist_ok=True)

    taxi_trips, taxi_zones = load_raw_data(project_root)
    taxi_trips, taxi_zones = standardize_columns(taxi_trips, taxi_zones)
    cleaned_taxi_trips = clean_taxi_trips(taxi_trips, taxi_zones)

    output_path = processed_data_dir / "cleaned_yellow_taxi_jan_2024.parquet"
    cleaned_taxi_trips.to_parquet(output_path, index=False)

    print(f"Cleaned dataset saved to: {output_path}")
    print(f"Cleaned shape: {cleaned_taxi_trips.shape[0]:,} rows and {cleaned_taxi_trips.shape[1]:,} columns")


if __name__ == "__main__":
    main()
