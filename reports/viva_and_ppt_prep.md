# NYC Taxi Trip Analytics: Viva & PPT Preparation Guide

This guide is designed to help the team excel during the Final Presentation (PPT) and the technical Viva session. It breaks down the story, the technical details, and the likely questions from evaluators.

---

## Part 1: PPT Structure (10-12 Slides)

**Slide 1: Title Slide**
- **Title:** NYC Taxi Operations: Data-Driven Strategies for Revenue & Efficiency
- **Sector:** Urban Mobility
- **Team Names:** Ayush Kumar Singh, Angelo Nelson, Isha Singh, Deepesh Dey, Rohit Nair P
- **Key Visual:** A professional NYC taxi image or the project logo.

**Slide 2: Executive Summary (The "Hook")**
- **The Problem:** Fleet operators struggle with positioning and revenue leakage.
- **The Solution:** End-to-end Python + Tableau pipeline analyzing 2.87M trips.
- **Top Metric:** $78.4M Total Revenue across 2.87M trips.
- **Top Insight:** Queens trips yield 3.2x the revenue of Manhattan trips.

**Slide 3: Business Context & Sector Overview**
- Competition from Uber/Lyft makes efficiency a survival requirement.
- The decision-maker: Fleet Managers and TLC Policy Analysts.
- Goal: Shift from "Reactive Driving" to "Data-Driven Positioning."

**Slide 4: Data Description & Cleaning (The Foundation)**
- **Source:** NYC TLC January 2024 (Parquet).
- **Cleaning:** 96k records (3.2%) removed for impossible values (e.g., negative fares).
- **Tooling:** Python (Pandas/PyArrow).
- **Ref:** `notebooks/02_cleaning.ipynb`

**Slide 5: Feature Engineering & KPIs**
- **New Features:** `revenue_per_mile`, `trip_duration_minutes`, `distance_bucket`.
- **Top KPIs:** Total Revenue ($78.4M), Avg Fare ($18.49), Credit Card Share (80%).
- **Why it matters:** `revenue_per_mile` identifies the most profitable trip segments.

**Slide 6: Exploratory Analysis (EDA) — Spatial & Temporal**
- **Spatial:** 90% pickups in Manhattan, but Queens is the premium corridor.
- **Temporal:** Peak demand at 6:00 PM (18:00).
- **Heatmap Mention:** Demand vs. Day of Week.

**Slide 7: Statistical Analysis — Hypothesis Testing**
- **Test 1:** Weekday vs. Weekend (Welch's t-test). Weekdays are more valuable due to time-based fare components.
- **Test 2:** Borough Variance (ANOVA). Confirmed location is a primary revenue driver.
- **Test 3:** Tip Behavior (Mann-Whitney U). Card users tip significantly more than cash users.

**Slide 8: Statistical Analysis — Regression Modeling**
- **Model:** OLS Regression (R² = 0.93).
- **What it tells us:** 93% of revenue can be predicted by distance, duration, and rate code.
- **Validation:** Scikit-learn (MAE = $2.36).

**Slide 9: Tableau Dashboard (The Product)**
- Show the "Executive Overview" screenshot.
- Highlight the interactive filters (Borough, Hour, Payment).
- Demonstrate the "Distance vs Total Amount" scatter plot.

**Slide 10: Key Business Recommendations**
1. **Airport Surge Strategy:** Move 15% fleet to Queens/JFK during peak arrival windows.
2. **Card Adoption:** Incentivize digital payment for short trips to capture tip leakage.
3. **Peak Hour Shifts:** Maximize supply during the 5 PM - 8 PM window.

**Slide 11: Impact Estimation & Limitations**
- **Impact:** Estimated +$10M monthly revenue uplift.
- **Limitations:** Single-month snapshot (January); lack of driver-level data; cash tip data gaps.

**Slide 12: Conclusion**
- We transitioned from raw Parquet data to a decision-ready dashboard.
- Future Scope: Real-time prediction models and weather data integration.

---

## Part 2: Viva Preparation (Q&A)

### General Questions (For Everyone)
1. **"What was the most challenging part of the cleaning process?"**
   - *Answer:* Handling impossible values. We found trips with $0 distance but $50 fares, and vice versa. Deciding on the 180-minute cap for duration was a critical business assumption.
2. **"Why did you choose the January 2024 dataset?"**
   - *Answer:* It's the most recent full-month stable release from TLC, providing 2.9M+ records which is statistically robust for regression modeling.

### Role-Specific Deep Dives

#### Ayush (Statistical Analysis Lead)
- **"Why use Mann-Whitney U instead of just a t-test for tips?"**
  - *Answer:* Tip data is highly skewed (most are 0, some are large). T-tests assume normality; Mann-Whitney U is a non-parametric test that compares distributions, making it more robust for skewed taxi data.
- **"Explain your R-squared of 0.93. Isn't that too high?"**
  - *Answer:* It's high because the dependent variable (Total Amount) is mechanically calculated from distance and time. However, it validates that the pricing engine is consistent and that our "operational" features are good proxies for revenue.

#### Angelo (Data Engineering / ETL Lead)
- **"Why use Parquet format instead of CSV for raw data?"**
  - *Answer:* Performance and storage. 2.9M rows in Parquet is ~50MB; in CSV, it would be over 400MB. PyArrow makes reading Parquet much faster for Python.
- **"How did you handle the Taxi Zone join?"**
  - *Answer:* We performed a left join between the trip data (PULocationID) and the lookup table. We handled ~10k 'Unknown' zones by labeling them as such to preserve total revenue counts.

#### Isha (Final Load / Documentation Lead)
- **"How did you prepare data for Tableau? Why not just connect to the full parquet?"**
  - *Answer:* Tableau performance. Connecting to 2.9M rows is slow. We created 13 pre-aggregated CSVs (hourly, borough-level, KPIs) to make the dashboard fast and responsive for decision-makers.
- **"What's the difference between a Data Dictionary and a Cleaning Log?"**
  - *Answer:* The Data Dictionary defines what the fields *are*; the Cleaning Log documents how they *changed* (rows before/after, logic applied).

#### Deepesh & Rohit (Tableau Leads)
- **"Explain your choice of 'Distance vs. Total Amount' scatter plot."**
  - *Answer:* It helps identify outliers and confirms the linear relationship. It also shows "bands" representing different rate codes (e.g., the flat-rate JFK line).
- **"What does the interactive filter on 'Payment Type' reveal?"**
  - *Answer:* It shows that revenue per mile is relatively stable across types, but tip behavior is completely different (Card vs. Cash).

---

## Part 3: Golden Rules for the Viva
1. **Refer to specific files:** "As seen in `notebooks/04_statistical_analysis.ipynb`..."
2. **Quantify your answers:** Don't say "revenue went up." Say "average revenue in Queens is $72.22 vs $22.76 in Manhattan."
3. **Acknowledge limitations:** If asked about cash tips, say "We identified this as a data gap in Section 14 of our report and recommended card incentives to fix it."
4. **Speak the "Decision Language":** Always link a technical fact to a business action. "Because Hour 18 is the peak, we recommend shifting driver shifts to cover the 5-8 PM window."
