# NYC Taxi Trip Analytics — Final Project Report

---

## 10. Tableau Dashboard Design

*Reference: `tableau/screenshots/` and `tableau/dashboard_links.md`*

### Dashboard Objective

The Tableau dashboard answers one central business question: **"Where, when, and how should NYC Yellow Taxi operators deploy their fleet to maximize revenue?"** It supports both strategic decision-making (borough and zone targeting) and operational decisions (hour-of-day and day-of-week positioning).

### Dashboard: NYC Taxi Operations — 2024 Performance Overview

The published dashboard contains a single comprehensive executive view with multiple chart panels and interactive filters.

#### KPI Banner (Top)

Five headline KPIs are displayed at the top:

| KPI | Value Displayed |
|---|---|
| Total Trips | 90B (aggregated display) |
| Total Revenue | $2,462B (aggregated display) |
| Avg Total Amount | $27 |
| Avg Trip Distance | 3.65 mi |
| Avg Trip Duration | 14.96 min |

#### Chart Panels Included

| Panel | Chart Type | Decision It Supports |
|---|---|---|
| Daily Revenue Trend | Line chart | Identifies revenue fluctuation by day for staffing decisions |
| Trips by Pickup Hour | Bar chart | Identifies peak demand hours for fleet deployment |
| Trips by Day of Week | Bar chart | Guides weekly shift scheduling |
| Pickup Borough Demand | Horizontal bar | Shows which boroughs generate most volume |
| Top 10 Pickup Zones | Horizontal bar | Zone-level hotspot identification |
| Distance vs Total Amount | Scatter plot | Visualizes the distance-revenue relationship |
| Payment Type Distribution | Bar chart | Shows credit card vs cash split by volume |

#### Dashboard Tabs (Bottom Navigation)

The dashboard includes the following tab views for drill-down:
- Pickup Borough Demand
- Drop-off Borough Demand
- Top 10 Pickup Zones
- Payment Type Distribution
- Tip % by Payment Type
- Trips by Distance Bucket
- Revenue per Mile by Distance Bucket
- Distance vs Total Amount

#### Interactive Filters

The dashboard includes interactive filters allowing users to:
- Filter by **Pickup Borough**
- Filter by **Day of Week**
- Filter by **Payment Type**
- Filter by **Distance Bucket**
- Filter by **Pickup Hour**

#### Tableau Public URL

```
To be added after publishing the dashboard.
See: tableau/dashboard_links.md
```

> **Built by:** Deepesh Dey & Rohit Nair P

---

## 11. Insights Summary

The following 10 insights are written in decision language — each states what the data means for the business, not just what it shows.

1. **Manhattan is high-volume but low-value; Queens is low-volume but high-value.** With 89.7% of pickups but average fares of only $22.76, Manhattan generates volume at modest revenue. Queens, with 9% of pickups and $72.22 average fare, is the premium revenue corridor. Fleet operators should treat Queens airport zones as a deliberate target, not an afterthought.

2. **JFK Airport is the single most valuable origin zone in NYC, not just in Queens.** At $80.86 average fare per trip and 138,311 pickups in January alone, JFK generates more revenue per pickup than any other top-10 zone. A dedicated JFK positioning strategy during airport surge windows can meaningfully raise per-driver daily earnings.

3. **The evening rush (18:00) is the single most critical operational window.** Hour 18 commands the highest trip volume in the dataset. Operators who are not actively positioned in Midtown, Penn Station, and Times Square between 17:00–19:00 are missing the highest-demand window of the day.

4. **Short trips are revenue-efficient per mile; long trips are revenue-efficient per absolute amount.** Trips of 0–1 miles earn $19.32/mile median, while 10–20 mile trips earn only $5.54/mile but deliver $81.50 per trip. A mixed fleet strategy — optimizing for throughput in Manhattan and absolute value in Queens — maximizes both dimensions simultaneously.

5. **Credit card users generate 26.28% tip rates; cash users generate effectively zero recorded tips.** This is not simply a preference difference — it is a structural revenue capture gap. Every shift in payment from cash to card directly increases verifiable per-trip earnings. The $4.16 average tip from card users vs $0.00 from cash users represents real income.

6. **Weekday trips generate $1.65 more per trip than weekend trips, despite being shorter in distance.** Congestion surcharges, congestion pricing, and metered time components make weekday urban trips more valuable per mile than weekend trips. This is statistically significant and economically meaningful for shift planning.

7. **Wednesday is the highest-revenue day of the week ($13.2M in January).** Mid-week business travel — corporate commutes, airport business travel, and medical appointments — drives a volume and revenue peak. Wednesday morning through Thursday evening is the golden operating window.

8. **The regression model explains 92.96% of fare variation using only trip characteristics.** This means taxi revenue is highly systematic — it is not random. Distance, duration, rate code, and borough together nearly fully determine what a trip will earn, which means positioning decisions can be modeled and optimized with high confidence.

9. **Brooklyn and the Bronx are statistically underserved relative to their revenue potential.** Brooklyn trips average $33.19 and Bronx trips $35.44 — both exceeding Manhattan's $22.76 — yet they represent only 0.97% of total pickups combined. These boroughs represent an underexplored market with above-average revenue per trip.

10. **Payment type and distance bucket are statistically associated, but practically weakly (Cramér's V = 0.044).** Short-trip cash dominance is real but small in magnitude. The most effective intervention is not to enforce card payment on short trips, but to use in-app tipping prompts for card users across all distance categories, where the 26% average tip rate already demonstrates strong willingness to tip.

---

## 12. Recommendations

### Recommendation 1: Establish a Dedicated Queens Airport Positioning Strategy

**Insight → Recommendation:** Queens trips average $72.22 per trip (vs Manhattan's $22.76), driven by JFK ($80.86) and LaGuardia ($66.36) airport demand. A deliberate positioning policy — routing available drivers to airport zones during flight arrival windows (6–9 AM, 3–6 PM, 10 PM–1 AM) — can increase per-driver daily revenue by an estimated 15–25%.

**Expected Impact:** If 5% of Manhattan-idle drivers (≈128,600 trips/month) shift to Queens airport zones, and average revenue increases from $22.76 to $70 per trip, the revenue uplift is approximately **$6.1M per month** at the fleet level.

**Feasibility:** Requires dispatcher coordination or app-level zone incentives. No infrastructure investment needed. Can be piloted in 30 days.

---

### Recommendation 2: Implement Credit Card Adoption Incentives for Short-Trip Passengers

**Insight → Recommendation:** Card users tip 26.28% vs ~0% for cash users on recorded data. The bulk of cash trips are in the 0–3 mile bracket. Offering a small card-payment incentive (e.g., $1 fare discount for first card payment) can shift payment behavior in the highest-volume segment.

**Expected Impact:** If 10% of the 422,295 monthly cash trips convert to card, and card users generate $4.16 more per trip in tips, the incremental tip revenue is approximately **$175,700 per month** at current volume.

**Feasibility:** Requires TLC or fleet operator app modification. Low cost, moderate change management effort. Pilots can be validated within one billing cycle.

---

### Recommendation 3: Shift Fleet Supply to Match the 17:00–19:00 Evening Peak

**Insight → Recommendation:** Hour 18 is the peak demand hour. Current supply likely under-meets demand in this window, leading to surge wait times that reduce customer satisfaction and push riders toward app-based alternatives. Actively rostering drivers for 16:00–20:00 shifts maximizes revenue-per-active-hour.

**Expected Impact:** Closing a conservative 5% supply gap during peak hours (≈5,000 trips/day) at $27 average adds **$135,000/day** or approximately **$4.05M/month** in recoverable revenue across the fleet.

**Feasibility:** Requires shift scheduling changes and driver incentive alignment. Moderate implementation complexity.

---

### Recommendation 4: Develop an Outer Borough Demand Growth Programme

**Insight → Recommendation:** Brooklyn and the Bronx generate above-Manhattan per-trip revenue ($33–$35 average) but receive fewer than 1% of total taxi supply. A targeted awareness or dispatch incentive program for outer borough trips can unlock a structurally underserved market.

**Expected Impact:** Even a doubling of Brooklyn and Bronx trip volume (from 28,000 to 56,000 per month) at $34 average adds **$952,000/month** in additional revenue.

**Feasibility:** Requires zone-based dispatch incentives. Medium effort, significant upside given the currently near-zero positioning in these markets.

---

### Recommendation 5: Use Wednesday as the Benchmarking Baseline for Operational Efficiency

**Insight → Recommendation:** Wednesday consistently generates the highest trip volume and revenue. Operational KPIs (trips per driver, revenue per shift, wait time) should be measured against Wednesday performance as the peak-efficiency benchmark, not averages.

**Expected Impact:** Better benchmarking improves driver performance coaching, shift allocation, and revenue target-setting. Non-monetary benefit with high analytical value.

**Feasibility:** Requires reporting system configuration only. Low effort, high impact on management decision quality.

---

## 13. Impact Estimation

| Recommendation | Monthly Impact Estimate | Confidence | Time to Implement |
|---|---|---|---|
| Queens Airport Positioning Strategy | +$6.1M revenue | Medium-High | 30 days |
| Credit Card Adoption Incentives | +$175,700 tip revenue | Medium | 60 days |
| Evening Peak Fleet Deployment | +$4.05M recoverable revenue | Medium | 30 days |
| Outer Borough Demand Growth | +$952,000 revenue | Low-Medium | 90 days |
| Benchmarking Realignment | Non-monetary | High | 14 days |

**Why act now?** January 2024 represents a post-holiday demand trough. If these structural patterns hold in higher-demand months (May–October), the uplift potential is proportionally larger. Early implementation allows the fleet to enter the spring and summer peak season with optimized positioning already in place.

---

## 14. Limitations

1. **Single-month snapshot.** January 2024 is one of the lowest-demand months of the year (post-holiday lull, winter weather effects). Seasonal patterns in spring and summer may differ materially. Generalizing these findings to the full year requires caution.

2. **Cash tip under-recording.** The analysis of tip behavior is limited to electronically recorded tips. Cash tips — which may be substantial — are entirely absent from the dataset. The 0% average cash tip rate is a data artifact, not a behavioral fact.

3. **No driver-level data.** The dataset contains no medallion, driver, or vehicle identifiers. Revenue and efficiency findings represent trip-level averages across the entire fleet, not individual driver performance.

4. **External factors excluded.** Weather events, public transit disruptions, major events (concerts, sports, political events), and holiday effects in January were not controlled for. These can materially shift demand patterns.

5. **Zone mapping completeness.** 10,316 trips (0.36%) could not be mapped to a named borough. These are labeled "Unknown" and excluded from borough-level analysis. If these are systematically from specific areas, the analysis may undercount certain zones.

6. **Regression does not imply causation.** The OLS model explaining 92.96% of revenue variance is a descriptive model, not a causal one. Rate code and distance are the dominant drivers because they are mechanical inputs to the metered fare formula — not independent business levers.

---

## 15. Future Scope

1. **Multi-month trend analysis.** Extending the dataset to cover a full year (all 12 months of 2024) would reveal seasonal demand cycles, holiday effects, and year-over-year comparison opportunities. This would allow proper time-series forecasting.

2. **Real-time demand prediction model.** Using historical hourly demand patterns by zone, a machine learning model (e.g., XGBoost or LSTM) could predict demand 1–2 hours ahead, enabling proactive dispatch recommendations.

3. **Weather data integration.** Joining hourly weather data (temperature, precipitation, visibility) from NOAA or Open-Meteo with trip records would quantify how weather affects demand, allowing weather-triggered dispatch strategies.

4. **Competitive benchmarking.** Integrating Uber/Lyft (HVFHV) data from the same TLC dataset would allow direct comparison of taxi vs. ride-hailing demand by zone and hour — quantifying where taxis are gaining or losing market share.

5. **Driver-level earnings simulation.** If driver/medallion IDs were available, a simulation model could estimate individual earnings uplift from each of the four positioning recommendations, allowing personalized driver coaching.

6. **Live Tableau dashboard.** The current dashboard uses a static January 2024 extract. A pipeline connecting to TLC's real-time data feed (monthly Parquet releases) could automate refresh and enable ongoing monitoring.

---

## 16. Conclusion

NYC Yellow Taxis generated 2.87 million trips and $78.4 million in revenue in January 2024 alone — yet the data reveals substantial, addressable inefficiencies in how that revenue is distributed across time, geography, and payment channels. Manhattan's dominance masks the superior per-trip revenue potential of Queens airport routes. The 6 PM evening peak is underutilized relative to its volume. Credit card tipping creates a verifiable 26% tip capture rate that cash transactions cannot match.

This project built a complete, reproducible Python ETL and statistical analysis pipeline — from raw Parquet data to Tableau-ready exports — and delivered seven statistically validated findings using correlation testing, Mann-Whitney U, ANOVA, chi-square, and OLS regression. The evidence consistently points to the same strategic direction: move supply toward where revenue per trip is highest, not just where volume is highest.

The recommended actions — airport zone positioning, card adoption incentives, evening peak deployment, and outer borough expansion — are estimated to recover over $10M in monthly fleet revenue with low-to-medium implementation complexity and 30–90 day timelines.

---

## 17. Appendix

### A. Data Dictionary

See: `docs/data_dictionary.md` (full column definitions for all 47 fields in the cleaned dataset).

### B. Cleaning Log

| Step | Rows Before | Rows After | Removed | % |
|---|---|---|---|---|
| Remove exact duplicates | 2,964,624 | 2,964,624 | 0 | 0.00% |
| Remove invalid timestamps | 2,964,624 | 2,963,754 | 870 | 0.03% |
| Restrict to January 2024 | 2,963,754 | 2,963,736 | 18 | <0.01% |
| Remove impossible values | 2,963,736 | 2,868,035 | 95,701 | 3.23% |

### C. Additional EDA Outputs

All chart PNGs are committed to `reports/figures/`:
- `daily_taxi_trip_demand.png`
- `hourly_taxi_demand.png`
- `hourly_revenue.png`
- `pickup_borough_trips.png`
- `dropoff_borough_trips.png`
- `top_pickup_zones.png`
- `trip_distance_distribution.png`
- `trip_duration_distribution.png`
- `payment_type_distribution.png`
- `distance_bucket_trips.png`
- `distance_vs_total_amount.png`
- `tip_percentage_by_payment_type.png`
- `weekday_taxi_demand.png`
- `weekday_vs_weekend_average_total_amount.png`
- `average_total_amount_by_pickup_borough.png`
- `payment_type_share_by_distance_bucket.png`
- `median_revenue_per_mile_by_distance_bucket.png`
- `actual_vs_predicted_total_amount.png`

### D. Processed Statistical Outputs

All statistical summary CSVs are committed to `data/processed/`:
- `statistical_pearson_correlation_matrix.csv`
- `statistical_spearman_correlation_matrix.csv`
- `statistical_correlation_test_results.csv`
- `weekday_vs_weekend_statistical_tests.csv`
- `pickup_borough_group_comparison_tests.csv`
- `pickup_borough_statistical_summary.csv`
- `payment_distance_chi_square_test.csv`
- `payment_distance_distribution_percentages.csv`
- `tip_behavior_statistical_test.csv`
- `payment_tip_statistical_summary.csv`
- `distance_efficiency_summary.csv`
- `ols_revenue_driver_coefficients.csv`
- `ols_revenue_driver_model_summary.csv`
- `sklearn_revenue_model_performance.csv`

---

## 18. Contribution Matrix

| Phase | Ayush Kumar Singh | Angelo Nelson | Isha Singh | Deepesh Dey | Rohit Nair P |
|---|---|---|---|---|---|
| **Dataset & Sourcing** | | ✅ Primary | | | |
| **ETL & Cleaning** | | ✅ Primary | | | |
| **EDA & Analysis** | | ✅ Primary | | | |
| **Statistical Analysis** | ✅ Primary | | | | |
| **Final Load Prep** | | | ✅ Primary | | |
| **Tableau Dashboard** | | | | ✅ 50% | ✅ 50% |
| **Report Writing** | | | ✅ Contributed | | |
| **PPT & Viva Prep** | | | | | |

### Contribution Notes (Based on GitHub Commit History)

**Angelo Nelson (`angelonels`):**
Commits: Initial project setup, folder structure with `uv`, raw data extraction notebook (`01_extraction.ipynb`), full ETL and cleaning pipeline (`02_cleaning.ipynb`, `scripts/etl_pipeline.py`), EDA notebook (`03_eda.ipynb`), processed summary CSVs, dataset profile and cleaning documentation, README updates.
*Primary contributor for Dataset Sourcing, ETL, and Exploratory Data Analysis.*

**Ayush Kumar Singh (`AyushCoder9`):**
Commits: All 52 commits comprising the complete statistical analysis notebook (`04_statistical_analysis.ipynb`) — covering correlation analysis, weekday/weekend hypothesis testing, borough group comparison, chi-square test for payment behavior, tip behavior analysis, OLS regression, Scikit-learn model evaluation, revenue efficiency analysis, statistical findings report, visualization plots, and processed statistical datasets.
*Primary contributor for Statistical Analysis.*

**Isha Singh (`Ishiezz`):**
Commits: Final load preparation notebook (`05_final_load_prep.ipynb`), all 13 Tableau-ready processed CSV files, data dictionary (`docs/data_dictionary.md`), Tableau data guide documentation, final load summary documentation, Tableau dashboard placeholder link.
*Primary contributor for Final Load Preparation and Documentation.*

**Deepesh Dey:**
Built and published the Tableau Public dashboard — executive KPI view, daily revenue trend, hourly demand chart, borough demand visualization, top 10 pickup zones, payment distribution, distance vs total amount scatter, and all interactive filters. Responsible for 50% of dashboard design and layout decisions.

**Rohit Nair P:**
Co-built the Tableau Public dashboard — drop-off borough demand, tip percentage by payment type, trips by distance bucket, revenue per mile by distance bucket, day-of-week analysis, and tab navigation structure. Responsible for 50% of dashboard design and drill-down view construction.

**Data Visualization & Analytics | Capstone 2**

---

## 1. Cover Page

| Field | Details |
|---|---|
| **Project Title** | NYC Taxi Trip Analytics: Demand, Revenue, and Efficiency Insights |
| **Sector** | Urban Mobility / Transportation Analytics |
| **Institute** | Newton School of Technology |
| **GitHub Repository** | https://github.com/angelonels/NYCTaxiTripAnalytics |
| **Tableau Public Dashboard** | *(To be added after publishing)* |
| **Submission Date** | April 2026 |

### Team Members & Roles

| Name | Role |
|---|---|
| Ayush Kumar Singh | Statistical Analysis & Data Science Lead |
| Angelo Nelson | Data Engineering & ETL Lead |
| Isha Singh | Final Load Preparation & Documentation Lead |
| Deepesh Dey | Tableau Dashboard Designer |
| Rohit Nair P | Tableau Dashboard Designer |

---

## 2. Executive Summary

**Problem:** NYC Yellow Taxi operators and urban transport planners lack a consolidated, data-driven view of when and where taxi demand peaks, what drives revenue, and how trip efficiency varies across boroughs, time slots, and distance categories. Without this understanding, fleet positioning is reactive rather than strategic, and pricing opportunities are left uncaptured.

**Approach:** The team sourced 2.96 million January 2024 NYC Yellow Taxi trip records from the NYC Taxi & Limousine Commission. A Python-based ETL pipeline was built across five Jupyter notebooks — handling data extraction, cleaning, feature engineering, exploratory analysis, statistical testing, and Tableau-ready export. The Tableau Public dashboard translates the analysis into interactive decision views.

**Key Insights:**

1. **Manhattan dominates demand but Queens drives revenue per trip.** Over 89% of all pickups originate in Manhattan, but Queens trips average $72.22 per trip — more than three times Manhattan's $22.76 — primarily driven by JFK Airport demand.
2. **The evening rush (6 PM) is the single most critical operational window.** Hour 18 records the highest trip volume, making it the peak window for fleet deployment decisions.
3. **Short trips (0–1 miles) are the most revenue-efficient per mile at $19.32/mile**, but long trips (10–20 miles) generate the highest absolute revenue per trip at $81.50, creating a strategic tension in fleet targeting.
4. **Credit card payers tip on average 26.28%** compared to effectively zero for cash trips, making payment method a strong proxy for customer value.

**Key Recommendations:**

1. Shift 15–20% of Manhattan fleet to Queens during peak airport hours to capture high-revenue ($72+ per trip) JFK and LaGuardia demand.
2. Incentivize credit card adoption to improve tip capture rates and increase verifiable revenue data quality.
3. Optimize fleet positioning around the top 10 pickup zones (Midtown Center, Upper East Side South, JFK Airport) during the 6–9 PM evening window.

---

## 3. Sector & Business Context

### Sector Overview

Urban mobility and taxi services form a critical pillar of city transport infrastructure. The NYC Yellow Taxi market operates in an increasingly competitive environment, with ride-hailing platforms like Uber and Lyft eroding traditional taxi market share since 2014. NYC's TLC-regulated Yellow Taxis continue to serve approximately 2.87 million trips per month in January 2024.

Key industry challenges include:
- **Dynamic demand uncertainty**: Operators struggle to predict demand spikes by hour, location, and day.
- **Revenue leakage**: Cash transactions reduce tip capture and revenue traceability.
- **Inefficient fleet positioning**: Drivers self-select pickup zones without data-backed guidance, leading to oversupply in low-revenue areas and undersupply in high-revenue zones.
- **Airport surge opportunity**: Airport trips (JFK, LaGuardia) command significantly higher fares but require deliberate positioning.

### Decision-Maker

This project serves two primary decision-makers:
- **Taxi fleet operators and dispatchers**: Who need zone-level and time-of-day guidance for positioning.
- **NYC TLC policy analysts**: Who require borough-level demand and revenue equity insights for infrastructure and regulatory decisions.

### Why This Problem Was Chosen

The NYC TLC dataset is one of the richest publicly available urban mobility datasets in the world, with trip-level detail across 2.96 million records in a single month. The problem directly maps to real-world operational decisions with measurable financial outcomes — making it ideal for a decision-oriented analytics project.

### Business Value

- **Fleet operators** can increase per-driver revenue by 15–25% through data-guided zone positioning.
- **TLC planners** can identify underserved boroughs (Bronx, Staten Island) and design incentive structures accordingly.
- **Payment policy makers** can build the case for credit card incentives using the 26% vs. 0% tip rate differential.

---

## 4. Problem Statement & Objectives

### Formal Problem Definition

*NYC Yellow Taxi operators lack data-backed insight into the spatial, temporal, and behavioral patterns that drive trip demand and revenue. This project uses January 2024 trip-level data to identify when, where, and how taxi demand is generated — and to translate those findings into specific, actionable fleet and business recommendations.*

### Project Scope

**In Scope:**
- NYC Yellow Taxi trip records for January 2024 only
- Pickup and drop-off borough and zone analysis
- Hourly, daily, and weekday/weekend demand analysis
- Fare, tip, revenue, and distance analysis
- Payment method behavior
- Statistical testing of demand and revenue differences across segments
- Tableau dashboard for interactive exploration

**Out of Scope:**
- Other vehicle types (Green Taxi, FHV, HVFHV)
- Real-time or multi-month trend forecasting
- Driver-level or medallion-level analysis
- External factors (weather, events, public transit disruptions)

### Success Criteria

1. A clean, reproducible Python pipeline that reduces raw 2.96M records to a validated 2.87M-record analytical dataset.
2. Statistical evidence confirming or rejecting hypotheses about demand and revenue differences across boroughs, time, and payment type.
3. A Tableau dashboard with at least one interactive filter that enables operational decision-making.
4. 3–5 specific, data-backed business recommendations with quantified impact estimates.

---

## 5. Data Description

### Dataset Source

| Field | Details |
|---|---|
| **Dataset Name** | NYC TLC Yellow Taxi Trip Records — January 2024 |
| **Format** | Apache Parquet |
| **Source** | NYC Taxi & Limousine Commission |
| **Direct Download** | https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet |
| **Official Page** | https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page |
| **Supporting Dataset** | NYC Taxi Zone Lookup Table (CSV) — https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv |

### Data Structure

| Metric | Value |
|---|---|
| Raw rows | 2,964,624 |
| Columns | 19 (raw) → 47 (after feature engineering) |
| Time period | January 1–31, 2024 |
| Final cleaned rows | 2,868,035 |
| Data removed | 96,589 records (3.26%) |

### Key Field Descriptions

| Column | Type | Description |
|---|---|---|
| `pickup_datetime` | datetime | Trip start timestamp |
| `dropoff_datetime` | datetime | Trip end timestamp |
| `trip_distance` | numeric | Distance in miles |
| `fare_amount` | numeric | Base metered fare |
| `tip_amount` | numeric | Recorded tip (card transactions only) |
| `total_amount` | numeric | Full charge including surcharges and tolls |
| `payment_type` | integer | Encoded payment method (1=Card, 2=Cash, etc.) |
| `PULocationID` | integer | Pickup taxi zone ID (mapped to borough via lookup) |
| `DOLocationID` | integer | Drop-off taxi zone ID |
| `RatecodeID` | integer | Rate category (1=Standard, 2=JFK, 3=Newark, etc.) |
| `passenger_count` | integer | Number of passengers reported |
| `congestion_surcharge` | numeric | NYC congestion pricing surcharge |
| `Airport_fee` | numeric | Airport-specific fee |

### Data Limitations and Known Biases

- **Cash tip under-recording**: Cash tips are not captured in electronic records. The average cash tip percentage (0.00%) reflects data absence, not actual customer behavior.
- **Single-month snapshot**: January 2024 may not represent seasonal demand patterns. January is typically a slower month post-New Year.
- **Passenger count gaps**: 4.02% of records had null or zero passenger counts and were imputed as Unknown.
- **Zone coverage**: 10,316 trips (0.36%) could not be mapped to a named NYC borough and are labeled "Unknown."
- **Airport fee field**: Introduced in 2022; some older vendor systems may not report this consistently.

---

## 6. Data Cleaning & ETL Pipeline

All data cleaning was performed in Python using `pandas` and `pyarrow`. The pipeline is fully documented in `notebooks/02_cleaning.ipynb`. A standalone version exists at `scripts/etl_pipeline.py`.

### Cleaning Steps Log

| Step | Rows Before | Rows After | Rows Removed | % Removed | Reason |
|---|---|---|---|---|---|
| Remove exact duplicates | 2,964,624 | 2,964,624 | 0 | 0.00% | No exact duplicate records found |
| Remove invalid timestamps | 2,964,624 | 2,963,754 | 870 | 0.03% | Null timestamps or drop-off before pickup |
| Restrict to January 2024 | 2,963,754 | 2,963,736 | 18 | <0.01% | Records with pickup outside Jan 2024 |
| Remove impossible values | 2,963,736 | 2,868,035 | 95,701 | 3.23% | Zero/negative distance, duration >180 min, negative fares |

**Total records removed: 96,589 (3.26% of raw dataset)**

### Missing Value Treatment

| Column | Issue | Treatment |
|---|---|---|
| `passenger_count` | 4.02% null or zero | Imputed as 0, grouped as "Unknown" or "Zero reported" |
| `store_and_fwd_flag` | Some nulls | Filled with "Unknown" |
| `rate_code_id` | Code 99 appeared | Mapped to "Unknown" label |
| `airport_fee` | Sparse | Retained as-is; used in total_amount |

### Outlier Treatment

- Trip duration capped at **180 minutes** (upper business logic bound)
- Trip distance, fare, and total amount: values below zero removed as impossible
- For regression modeling only: 99th percentile cap applied to `total_amount`, `trip_distance`, `trip_duration_minutes` to prevent extreme values from dominating coefficient estimates

### Feature Engineering

19 new columns were created from the raw fields:

| Feature | Formula / Source |
|---|---|
| `trip_duration_minutes` | `(dropoff_datetime - pickup_datetime).total_seconds() / 60` |
| `pickup_date` | Date extracted from `pickup_datetime` |
| `pickup_hour` | Hour extracted from `pickup_datetime` |
| `pickup_day_name` | Day name from `pickup_datetime` |
| `is_weekend` | True if Saturday or Sunday |
| `revenue_per_mile` | `total_amount / trip_distance` |
| `fare_per_minute` | `fare_amount / trip_duration_minutes` |
| `tip_percentage` | `(tip_amount / fare_amount) × 100` |
| `distance_bucket` | Categorical: 0-1, 1-3, 3-5, 5-10, 10-20, 20+ miles |
| `duration_bucket` | Categorical: 0-5, 5-15, 15-30, 30-60, 60+ minutes |
| `vendor_name` | Mapped from `vendor_id` |
| `rate_code_label` | Mapped from `rate_code_id` |
| `payment_type_label` | Mapped from `payment_type` |
| `pickup_borough` / `pickup_zone` | Joined from taxi zone lookup CSV |
| `dropoff_borough` / `dropoff_zone` | Joined from taxi zone lookup CSV |
| `is_high_value_trip` | Flag: `total_amount > 99th percentile` |
| `is_long_distance_trip` | Flag: `trip_distance > 99th percentile` |
| `is_long_duration_trip` | Flag: `trip_duration_minutes > 99th percentile` |

### Assumptions

1. Trips with duration above 180 minutes are considered data errors, not genuine long trips.
2. Cash tip amounts of zero represent the recorded value, not necessarily the actual amount paid.
3. Trips with `total_amount = 0` that are not "No charge" type are treated as invalid.

---

## 7. KPI & Metric Framework

| KPI | Formula | Why It Matters |
|---|---|---|
| **Total Trips** | Count of all cleaned records | Primary demand volume indicator |
| **Total Revenue** | Sum of `total_amount` | Absolute market size measure |
| **Average Total Amount** | Mean of `total_amount` | Per-trip revenue benchmark |
| **Average Fare Amount** | Mean of `fare_amount` | Core metered price indicator |
| **Average Trip Distance** | Mean of `trip_distance` | Service footprint measure |
| **Average Trip Duration** | Mean of `trip_duration_minutes` | Efficiency and congestion indicator |
| **Revenue per Mile** | `total_amount / trip_distance` | Trip revenue efficiency |
| **Fare per Minute** | `fare_amount / trip_duration_minutes` | Time-based efficiency |
| **Average Tip Amount** | Mean of `tip_amount` | Customer satisfaction proxy |
| **Tip Percentage** | `(tip_amount / fare_amount) × 100` | Normalized generosity measure |
| **Credit Card Share** | % of trips with `payment_type = 1` | Digital adoption and tip capture quality |
| **Peak Demand Hour** | Hour with max trip count | Fleet positioning input |

### Observed KPI Values (January 2024)

| KPI | Value |
|---|---|
| Total Trips | 2,868,035 |
| Total Revenue | $78,407,817 |
| Average Total Amount | $27.34 |
| Average Fare Amount | $18.49 |
| Average Trip Distance | 3.73 miles |
| Average Trip Duration | 14.96 minutes |
| Average Revenue per Mile | $17.49 |
| Average Tip Amount | $3.40 |
| Average Tip Percentage | 21.42% |
| Credit Card Share | 80.09% |
| Peak Demand Hour | 18:00 (6 PM) |
| Top Pickup Borough | Manhattan |

---

## 8. Exploratory Data Analysis

*Reference: `notebooks/03_eda.ipynb`*

### 8.1 Trend Analysis — Daily Demand

Daily trip volume in January 2024 showed a consistent mid-week peak pattern, with Wednesdays recording the highest trip count (480,554 trips, $13.2M revenue) and Sundays the lowest (326,488 trips). This reflects the standard urban commuter pattern where Monday through Thursday drives professional demand, while Sunday represents a recovery day with lighter leisure travel.

**Business implication:** Fleet supply should peak on Tuesday–Thursday. Sunday afternoon, not Monday morning, may be the optimal maintenance window.

| Day | Trips | Revenue | Avg Amount |
|---|---|---|---|
| Monday | 393,005 | $11,331,302 | $28.83 |
| Tuesday | 448,879 | $12,404,110 | $27.63 |
| Wednesday | 480,554 | $13,220,799 | $27.51 |
| Thursday | 416,030 | $11,532,275 | $27.72 |
| Friday | 396,156 | $10,767,101 | $27.18 |
| Saturday | 406,923 | $10,254,988 | $25.20 |
| Sunday | 326,488 | $8,897,239 | $27.25 |

### 8.2 Hourly Demand Pattern

The single peak hour by trip volume is **18:00 (6 PM)**, corresponding to the evening commute. Secondary peaks appear at 8–9 AM (morning commute) and midnight–1 AM (nightlife). The 4–5 AM window records the lowest volume but the highest average fare per trip ($37.56 at 5 AM), likely driven by airport runs and early-morning executive travel.

**Business implication:** The 5–7 AM window offers the best fare-per-trip efficiency. Positioning available drivers near business hotel clusters and JFK/LaGuardia access points at 4:30 AM can capture these high-value trips before the volume rush begins.

### 8.3 Borough Demand Distribution

Manhattan is the dominant origin borough, generating 2,572,024 pickups (89.7% of all trips). However, Queens trips yield an average of **$72.22 per trip** — more than three times Manhattan's $22.76. This is driven primarily by JFK Airport (80.86 avg) and LaGuardia Airport ($66.36 avg) trips.

| Borough | Trips | Avg Amount | Avg Distance | Avg Duration |
|---|---|---|---|---|
| Manhattan | 2,572,024 | $22.76 | 2.72 miles | 13.01 min |
| Queens | 257,603 | $72.22 | 12.81 miles | 32.40 min |
| Brooklyn | 22,254 | $33.19 | 14.82 miles | 31.64 min |
| Bronx | 5,742 | $35.44 | 7.73 miles | 38.17 min |
| Staten Island | 46 | $61.03 | 9.99 miles | 20.18 min |

**Business implication:** Queens generates only 9% of trips but significantly higher revenue per trip. A deliberate shift of even 5–10% of Manhattan fleet capacity toward Queens airport zones during peak hours can materially improve per-driver revenue.

### 8.4 Top 10 Pickup Zones

| Zone | Borough | Trips | Avg Amount |
|---|---|---|---|
| Midtown Center | Manhattan | 140,074 | $23.95 |
| Upper East Side South | Manhattan | 140,069 | $19.78 |
| JFK Airport | Queens | 138,311 | $80.86 |
| Upper East Side North | Manhattan | 133,901 | $20.26 |
| Midtown East | Manhattan | 104,298 | $23.33 |
| Times Sq/Theatre District | Manhattan | 102,890 | $26.86 |
| Penn Station/Madison Sq | Manhattan | 102,099 | $24.11 |
| Lincoln Square East | Manhattan | 101,706 | $21.33 |
| LaGuardia Airport | Queens | 87,658 | $66.36 |
| Upper West Side South | Manhattan | 86,432 | $21.22 |

### 8.5 Distance Distribution

The majority of NYC taxi trips are short: 49% fall in the 0–3 mile range (1-3 miles: 1,402,648 trips). The revenue-per-mile curve is strongly inverse — the shorter the trip, the higher the revenue efficiency per mile.

| Distance Bucket | Trips | Avg Total Amount | Avg Revenue/Mile |
|---|---|---|---|
| 0–1 miles | 704,747 | $14.28 | $39.75 |
| 1–3 miles | 1,402,648 | $20.42 | $12.05 |
| 3–5 miles | 305,453 | $30.90 | $8.21 |
| 5–10 miles | 230,426 | $47.72 | $6.58 |
| 10–20 miles | 195,889 | $81.50 | $5.54 |
| 20+ miles | 28,872 | $114.16 | $4.69 |

### 8.6 Payment Type Distribution

| Payment Type | Trips | Trip Share | Avg Total | Avg Tip % |
|---|---|---|---|---|
| Credit Card | 2,296,991 | 80.09% | $28.07 | 26.28% |
| Cash | 422,295 | 14.72% | $23.83 | ~0% (recorded) |
| Unknown | 115,237 | 4.02% | $26.51 | 9.14% |
| Dispute | 22,874 | 0.80% | $25.00 | ~0% |
| No Charge | 10,638 | 0.37% | $22.13 | ~0% |

### 8.7 Correlation Analysis

A Pearson and Spearman correlation analysis identified `fare_amount` as the strongest predictor of `total_amount` (Spearman r = 0.9636, p < 0.001). Trip distance and duration are moderately correlated with total amount, confirming that the metered fare structure behaves consistently with distance and time.

---

## 9. Statistical Analysis

*Reference: `notebooks/04_statistical_analysis.ipynb`*

### 9.1 Weekday vs Weekend: Hypothesis Testing

**Null Hypothesis:** There is no difference in trip metrics between weekday and weekend trips.

Two tests were used: Welch's t-test (for means) and Mann-Whitney U (for distributions, more robust under skew).

| Metric | Weekday Mean | Weekend Mean | Difference | Mann-Whitney Result |
|---|---|---|---|---|
| Total Amount | $27.77 | $26.12 | **-$1.66** | Statistically significant |
| Trip Distance | 3.62 miles | 3.75 miles | **+0.13 miles** | Statistically significant |
| Trip Duration | 15.40 min | 13.70 min | **-1.69 min** | Statistically significant |
| Revenue per Mile | $17.61 | $16.45 | **-$1.16** | Statistically significant |

**Finding:** Weekday trips generate higher revenue per trip ($27.77 vs $26.12) despite shorter distances, reflecting congestion-driven duration charges. Weekend trips are slightly longer but faster (lower congestion) and yield less per trip. Cohen's d values are small (<0.15), indicating the differences are statistically real but modest in practical magnitude.

**Business implication:** Weekday pricing — particularly during morning and evening rush — is inherently more favorable. Weekend operators should target longer-distance routes (airport transfers, outer-borough trips) to compensate for lower per-trip urban revenue.

### 9.2 Borough Revenue Differences: ANOVA & Kruskal-Wallis

**Null Hypothesis:** Average total amount is the same across all pickup boroughs.

Both the one-way ANOVA and Kruskal-Wallis test rejected the null hypothesis (p < 0.001), confirming that pickup borough is a statistically significant determinant of trip revenue.

| Borough | Avg Total Amount | Median Total Amount | Avg Distance |
|---|---|---|---|
| Queens | $72.22 | $72.78 | 12.81 miles |
| Bronx | $35.44 | $34.00 | 7.73 miles |
| Brooklyn | $33.19 | $29.00 | 14.82 miles |
| Manhattan | $22.76 | $19.25 | 2.72 miles |

**Finding:** Borough of pickup is a statistically significant and practically large determinant of trip revenue. Queens trips generate 3.2× the revenue of Manhattan trips on average. The difference is primarily structural (airport rate codes vs standard metered fares), not random variation.

### 9.3 Payment Type and Distance: Chi-Square Test

**Null Hypothesis:** Payment type (Credit Card vs Cash) is independent of distance bucket.

Chi-square statistic: Statistically significant (p < 0.001). Cramér's V = 0.044, indicating a statistically real but practically weak association. Credit card payments become more dominant as trip distance increases, while cash is slightly more prevalent in short trips.

**Business implication:** Short-trip cash dominance is a structural challenge for tip capture. Operator incentives for card-on-file or in-app payment could shift behavior at the segment most resistant to card adoption.

### 9.4 Tip Behavior: Credit Card vs Cash

| Payment | Avg Tip % | Median Tip % |
|---|---|---|
| Credit Card | 26.28% | 26.25% |
| Cash | ~0.00% (recorded) | 0.00% |

Mann-Whitney U test result: Statistically significant (p < 0.001). Cohen's d: large effect size, confirming the difference is practically meaningful — not just a statistical artifact.

**Important caveat:** Cash tips are not recorded in TLC electronic systems. The near-zero cash tip rate reflects recording absence, not actual customer behavior. Analysis of recorded tips only.

### 9.5 Regression Analysis: Revenue Drivers

An OLS regression model (Statsmodels) was fitted to explain total trip amount using operational variables only — excluding fare components to avoid data leakage.

**Model: `total_amount ~ trip_distance + trip_duration_minutes + pickup_hour + is_weekend + passenger_count + C(pickup_borough) + C(payment_type_label) + C(rate_code_label)`**

| Metric | Value |
|---|---|
| R-squared | **0.9296** |
| Adjusted R-squared | **0.9296** |
| Observations | 300,000 (sampled) |

**Scikit-learn validation (80/20 split):**

| Metric | Value |
|---|---|
| Mean Absolute Error | $2.36 |
| Root Mean Squared Error | $4.49 |
| R-squared | 0.9289 |

**Finding:** Trip distance, trip duration, and rate code category (particularly JFK and Newark codes) are the dominant revenue drivers. The model explains 92.96% of variance in total trip amount using only operational trip characteristics — confirming that the revenue structure is highly systematic and predictable.

### 9.6 Revenue Efficiency by Distance

Short trips (0–1 miles) generate **$19.32 median revenue per mile**, nearly 4× the efficiency of 20+ mile trips ($4.59/mile). However, volume-adjusted total revenue is highest in the 1–3 mile segment ($28.6M across January), driven by sheer trip count (1.4M trips).

**Business implication:** A portfolio approach is optimal: maximize short-trip throughput in Manhattan for revenue efficiency, while positioning selectively for long-distance airport trips for absolute revenue size.
