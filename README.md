
# 🚦 Traffic Accident Analysis & Bayesian Simulation - 3rd Place in 2025 Rutgers Barclays Hackathon

This project explores traffic accident trends using real-world data and visualizes the effectiveness of safety interventions using Bayesian Monte Carlo simulations.

---

## 📁 Dataset
- **`traffic_accidents.csv`** (included, ~209k rows): real crash records with date, traffic-control device, weather, lighting, crash type, trafficway, alignment, and injury fields. Used by both the Python and R analyses.

> This repository combines the full Barclays datathon submission: the Python analysis + Bayesian simulations and the R datathon/visualization scripts (previously split across two repos) now live together with the dataset.

---

## 📊 Python Data Analysis

### Time-Based Crash Patterns
- **Hourly Analysis**: Extracts hour of crash and visualizes frequency using seaborn.
- **Period Bucketing**: Groups hours into: `12AM–6AM`, `6AM–12PM`, `12PM–6PM`, `6PM–12AM`.
- **Day of Week**: Uses `day_name()` to analyze weekday distribution.
- **Month of Year**: Uses `month_name()` to find seasonal trends.

### Weather & Lighting Analysis (Optional)
- Visualizes crashes by `weather_condition` and `light_condition` if columns exist.

---

## 🧠 Bayesian Monte Carlo Simulation (Python)

### Goal
Model how safety interventions could impact the probability of accidents caused by **failure to yield right of way**.

### Approach
- **Beta Distribution (Prior)**: Based on historical data (`mean ≈ 0.39`)
- **Simulated Intervention**: 20% reduction applied to each sample.
- **Visualization**: Histogram showing pre- and post-intervention distributions.
- **Insights**: Posterior mean shifts left, suggesting lowered risk after policy change.

---

## 🔁 Alternate Simulation

Uses different Beta parameters to simulate prior and posterior:
- **Before**: `Beta(35, 65)`
- **After**: `Beta(28, 72)`
- Compares mean probabilities using histograms and vertical lines.

---

## 📊 R Scripts

Two R analyses are included:

- **`datathon.R`** — the main datathon exploration (tidyverse / `viridis` / `gridExtra`): data cleaning and the visual storytelling produced during the hackathon.
- **`fatal_injuries_by_group.R`** — fatal-injury breakdown described below.

### `fatal_injuries_by_group.R`
**Libraries:** `ggplot2`, `dplyr`, `tidyr`, `patchwork`
- Groups `injuries_fatal` by:
  - `weather_condition`
  - `first_crash_type`
  - `alignment`
  - `intersection_related_i`
- Displays top 15 most impactful categories in a 2x2 layout of bar plots.

---

## 📦 Setup Instructions

### Python
```bash
pip install pandas matplotlib seaborn scipy
```
Ensure your CSV file is correctly named or update the script.

### R
```r
install.packages(c("ggplot2", "dplyr", "tidyr", "patchwork"))
```
Run the `.R` script in RStudio or an R terminal with `traffic_accidents_3.csv` loaded.

---

## 📌 Summary
This project combines exploratory data visualization and statistical inference to:
- Reveal temporal and environmental crash patterns.
- Quantify how much interventions can shift risk probabilities.
- Communicate insights through clear visual storytelling.
