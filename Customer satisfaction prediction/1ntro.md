# Customer Satisfaction Prediction

## Project Overview
This data science project predicts customer satisfaction levels based on support ticket data using machine learning. The model classifies customers as satisfied (rating ≥ 4) or unsatisfied (rating < 4).

## Dataset
- **File**: `customer_support_tickets.csv`
- **Records**: 2,769 (after cleaning)
- **Features**: 18 original columns
- **Target**: Customer Satisfaction Rating (binary: satisfied/unsatisfied)

## Project Structure

```
Customer satisfaction prediction/
├── customer satisfaction prediction.ipynb  # Main notebook
├── customer_support_tickets.csv            # Dataset
└── README.md                               # This file
```

## Workflow

### 1. Data Loading & Exploration
- Load customer support tickets dataset
- Examine data shape, columns, and missing values
- Understand data distribution

### 2. Data Cleaning & Feature Engineering
- Drop rows with missing satisfaction ratings
- Create binary target variable (satisfied: rating ≥ 4)
- Convert datetime columns and engineer time-based features:
  - `time_to_resolution_hours`: Time from first response to resolution
  - `first_response_time_hours`: Time from purchase to first response
- Create age group categories: 18-29, 30-44, 45-59, 60+
- Handle missing values through imputation

### 3. Feature Preparation
- Select relevant features (drop ID, name, email, descriptions)
- Identify numerical features: Customer Age, time_to_resolution_hours, first_response_time_hours
- Identify categorical features: Customer Gender, Product Purchased, Ticket Type, Ticket Status, Ticket Priority, Ticket Channel

### 4. Data Visualization
- **Distribution Analysis**:
  - Customer age, time to resolution, first response time histograms
  - Categorical feature distributions (ticket type, priority, channel, status, gender, age groups)
  - Target variable distribution (count and percentage)
- **Correlation Analysis**:
  - Heatmap showing correlations between numerical features and satisfaction
- **Satisfaction Rate Analysis**:
  - Satisfaction rates by ticket priority, type, channel, and age group
- **Box Plot Comparisons**:
  - Time to resolution, first response time, and customer age by satisfaction level

### 5. Model Training
- **Train-Test Split**: 80-20 split with stratification
- **Preprocessing Pipeline**:
  - StandardScaler for numerical features
  - OneHotEncoder for categorical features
- **Class Imbalance Handling**: SMOTE (Synthetic Minority Over-sampling Technique)
- **Algorithm**: Random Forest Classifier
- **Hyperparameter Tuning**: GridSearchCV with 3-fold cross-validation

### 6. Model Evaluation
- Accuracy score
- Classification report (precision, recall, F1-score)
- Confusion matrix heatmap
- Model performance metrics visualization
- **Feature Importance Analysis**:
  - Top 15 most important features from Random Forest
- **Prediction Analysis**:
  - Actual vs predicted distribution comparison
  - Prediction probability distribution with decision threshold

## Key Findings

- **Class Distribution**: 60.7% unsatisfied, 39.3% satisfied (imbalanced)
- **Features Used**: 3 numerical + 6 categorical
- **Model**: Random Forest with SMOTE
- **Best Parameters**: Tuned via GridSearchCV

## Model Performance

The model is evaluated on a held-out test set using:
- Accuracy
- Precision & Recall
- F1-Score
- Confusion Matrix

## How to Run

1. Ensure all dependencies are installed
2. Open `customer satisfaction prediction.ipynb` in Jupyter Notebook
3. Run cells sequentially from top to bottom
4. The trained model is saved as `best_model.pkl`

## Dependencies

- pandas
- numpy
- scikit-learn
- imbalanced-learn
- matplotlib
- seaborn
- joblib

## Visualizations Included

1. **Exploratory Data Analysis**:
   - Numerical feature distributions
   - Categorical feature distributions
   - Target variable distribution

2. **Advanced Analytics**:
   - Correlation heatmap
   - Satisfaction rates across different categories
   - Box plots for numerical features by satisfaction

3. **Model Insights**:
   - Confusion matrix
   - Performance metrics bar chart
   - Feature importance ranking
   - Actual vs predicted comparison
   - Prediction probability distribution

## Future Improvements

1. Try alternative algorithms (XGBoost, LightGBM)
3. Experiment with different SMOTE strategies
4. Use ROC-AUC or F1-score as primary metric for imbalanced data
5. Cross-validation with different random states
6. Feature selection techniques (RFE, SelectKBest)

