# Statistical Analysis Findings

## 1. Correlation Analysis

The strongest Spearman relationship with total trip amount was found for `fare_amount`.

- Spearman correlation: 0.9636
- P-value: 0.000000
- Result: Statistically significant

## 2. Weekday vs Weekend Behavior

For total trip amount:

- Weekday average: $27.77
- Weekend average: $26.12
- Difference: $-1.66
- Mann-Whitney result: Statistically significant

For trip distance:

- Weekday average: 3.62 miles
- Weekend average: 3.75 miles
- Difference: 0.13 miles
- Mann-Whitney result: Statistically significant

## 3. Pickup Borough Differences

The pickup borough with the highest average total amount was:

- Borough: Queens
- Average total amount: $72.22

## 4. Payment Type and Distance

The chi-square test between payment type and distance bucket showed:

- Result: Statistically significant
- Cramér's V: 0.0444

## 5. Tip Behavior

The comparison between credit card and cash recorded tip percentage showed:

- Credit card average: 25.51%
- Cash average: 0.00%
- Result: Statistically significant

## 6. Regression Analysis

- R-squared: 0.9296
- Adjusted R-squared: 0.9296

## 7. Revenue Efficiency

The distance bucket with the highest median revenue per mile was:

- Distance bucket: 0-1 miles
- Median revenue per mile: $19.32
