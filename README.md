# U.S. Inflation Forecasting Using SARIMAX and Macroeconomic Indicators

This project builds a time series model to forecast U.S. year-over-year inflation using CPI data, as well as exogenous macroeconomic indicators like the the federal funds rate and unemployement rate. The project uses a SARIMAX model with automatic order selection.

## Project Overview

- **Goal:** Forecast the next 24 months of U.S. inflation.
- **Approach:** 
  - Transform CPI data to YoY inflation.
  - Perform seasonal decomposition to understand trend, seasonality, and noise.
  - Fit a SARIMAX model using exogenous variables.
  - Generate future forecasts.

## Key Features

- **Time Series Decomposition** using python's statsmodels
- **Multivariate Forecasting** with macroeconomic variables:
  - Federal Funds Rate
  - Unemployment Rate
  - Calendar Month
- **Automatic Model Selection**
- **Visualizations** of trends, seasonality, and residuals

## Technologies Used

- Python
- pandas and numpy for data handling
- matplotlib` for visualization
- statsmodels for time series decomposition
- pmdarima for SARIMAX modeling and forecasting

## Data Sources

- FRED (Federal Reserve Economic Data)(https://fred.stlouisfed.org/)
  - CPI: `CPIAUCSL.csv`
  - Federal Funds Rate: `FEDFUNDS.csv`
  - Unemployment Rate: `UNRATE.csv`
  - Future macro data: `FORECAST.csv`
- IMF (International Monetary Fund) (https://www.imf.org/external/datamapper)
- Econ Forecasting (https://econforecasting.com/forecast/ffr)

## 📊 Sample Forecast Output

The model outputs a 24-month forecast of inflation rates, shown in InflationPrediction.csv.

## 📌 How to Run

1. Download the required CSV files from [FRED](https://fred.stlouisfed.org/).
2. Update the file paths in the script if needed.
3. Run the script using Python 3.

## 💡 What I Learned

- How to preprocess and transform economic time series data.
- How to model seasonal patterns and integrate exogenous regressors into forecasting models.
- The importance of choosing appropriate evaluation metrics and decomposition techniques when dealing with non-stationary data.
- How to present technical analysis clearly with key visualization.
