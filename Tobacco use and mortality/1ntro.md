# Tobacco Use and Mortality Analysis

## Project Overview
This data science project analyzes the relationship between tobacco use and mortality rates, exploring trends in smoking prevalence, hospital admissions, fatalities, and the impact of economic factors and cessation interventions over a 40-year period (1974-2014).

## Objective
Analyze and predict the impact of tobacco use on public health by examining:
- Smoking prevalence trends over time
- Hospital admissions attributable to smoking
- Smoking-related deaths and fatalities
- Economic factors (tobacco affordability)
- Effectiveness of cessation interventions (pharmacotherapy prescriptions)

## Dataset Description

The project uses five CSV datasets:

1. **admissions.csv** (2079 records, 7 columns)
   - Hospital admissions data related to smoking-attributable diseases
   - Includes metrics by year, sex, diagnosis type, and age groups

2. **fatalities.csv** (1749 records, 7 columns)
   - Mortality data for smoking-related deaths
   - Categorized by diagnosis type, sex, and year

3. **metrics.csv** (36 records, 9 columns)
   - Economic and policy metrics including tobacco affordability index
   - Tracks tobacco pricing and accessibility over time

4. **prescriptions.csv** (11 records, 9 columns)
   - Pharmacotherapy prescription data for smoking cessation
   - Includes various cessation medication types

5. **smokers.csv** (84 records, 9 columns)
   - Smoking prevalence data by age groups and demographics
   - Tracks percentage of population that smokes (16 and over)

## Key Features

### Data Processing
- **Data Cleaning**: Standardizes column names, converts year formats, handles missing values
- **Feature Engineering**: Aggregates data by year to create a master dataset with key metrics
- **Data Integration**: Merges multiple datasets on year to create comprehensive analysis dataset

### Analysis Components
1. **Trend Analysis**: Examines smoking prevalence decline over 40 years
2. **Health Impact Assessment**: Correlates smoking rates with hospital admissions and deaths
3. **Economic Analysis**: Studies tobacco affordability and its relationship to smoking rates
4. **Intervention Effectiveness**: Evaluates impact of cessation prescriptions on smoking prevalence

### Machine Learning Models
The project implements three regression models to predict smoking-related outcomes:
- **Linear Regression**: Baseline model for trend analysis
- **Random Forest Regressor**: Ensemble method for non-linear relationships
- **Gradient Boosting Regressor**: Advanced ensemble technique for improved predictions

### Evaluation Metrics
- R² Score (coefficient of determination)
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)

## Technical Stack

- **Python 3.8+**
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning models and preprocessing
- **scipy**: Statistical analysis
- **jupyter**: Interactive notebook environment

## Installation

1. Clone the repository or navigate to the project directory
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Ensure all CSV files are in the same directory as the notebook
2. Launch Jupyter Notebook:
```bash
jupyter notebook
```
3. Open `Tobacco_Use_and_Mortality_Analysis.ipynb`
4. Run cells sequentially to:
   - Load and clean data
   - Perform exploratory data analysis
   - Generate visualizations
   - Train and evaluate machine learning models
   - Generate insights and predictions

## Project Structure

```
Tobacco use and mortality/
│
├── admissions.csv                              # Hospital admissions data
├── fatalities.csv                              # Mortality data
├── metrics.csv                                 # Economic metrics
├── prescriptions.csv                           # Cessation prescriptions
├── smokers.csv                                 # Smoking prevalence data
├── Tobacco_Use_and_Mortality_Analysis.ipynb   # Main analysis notebook
├── requirements.txt                            # Python dependencies
└── 1ntro.md                                   # Project documentation
```

## Code Functionality

### 1. Setup and Data Loading
- Imports necessary libraries for data analysis and machine learning
- Configures visualization settings
- Loads all five CSV datasets into pandas DataFrames
- Validates data loading with shape information

### 2. Data Cleaning and Preprocessing
- Cleans column names (removes newlines, extra spaces)
- Standardizes year formats across datasets
- Converts value columns to numeric types
- Handles missing data appropriately

### 3. Feature Engineering
- **Smoking Trend Aggregation**: Extracts overall smoking prevalence by year
- **Admissions Aggregation**: Sums smoking-attributable hospital admissions annually
- **Fatalities Aggregation**: Totals smoking-related deaths by year
- **Master Dataset Creation**: Merges all metrics into single time-series dataset
- Creates comprehensive feature set for modeling

### 4. Exploratory Data Analysis (EDA)
- Visualizes trends in smoking prevalence over time
- Analyzes correlation between smoking rates and health outcomes
- Examines impact of economic factors on smoking behavior
- Studies effectiveness of cessation interventions

### 5. Machine Learning Pipeline
- **Data Splitting**: Separates data into training and testing sets
- **Feature Scaling**: Standardizes features using StandardScaler
- **Model Training**: Trains multiple regression models
- **Model Evaluation**: Compares model performance using multiple metrics
- **Prediction**: Generates forecasts for future trends

## Key Insights

The analysis reveals:
- Significant decline in smoking prevalence from 46% (1974) to lower rates (2014)
- Strong correlation between smoking rates and health outcomes
- Impact of economic policies on tobacco consumption
- Effectiveness of pharmacotherapy interventions in reducing smoking rates

## Future Enhancements

- Time series forecasting using ARIMA or Prophet
- Deep learning models for complex pattern recognition
- Geographic analysis if regional data becomes available
- Cost-benefit analysis of intervention programs
- Interactive dashboard for real-time insights

**This project is for educational and analytical purposes.*
