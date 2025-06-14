Python

# Exploratory Data Analysis and Predictive Modeling of OCD Patient Data

## 1. Introduction

This project explores a dataset of Obsessive-Compulsive Disorder (OCD) patients, focusing on both exploratory data analysis (EDA) and predictive modeling. The primary objectives are to uncover relationships between demographic and clinical factors and to build a baseline model for predicting OCD symptom severity.

---

## 2. Data Overview

- **Dataset:** `OCD Patient Dataset_ Demographics & Clinical Data.csv`
- **Records:** 1,500
- **Attributes:** 17 (demographics, clinical features, symptom scores, comorbidities)
- **Completeness:** No missing values

---

## 3. Exploratory Data Analysis (EDA)

### Demographic Insights

- **Gender:** Nearly balanced, slightly more males.
- **Ethnicity:** Largest groups are Caucasian and Hispanic, followed by African and Asian.
- **Age:** Ranges from 18 to 75 years, evenly distributed.
- **Marital Status & Education:** Most are single; common education levels are "Some College" and "High School".

### Clinical Outcomes

- **Y-BOCS Scores:** Quantify severity of obsessions and compulsions.
- **Gender vs. Y-BOCS:** Females show slightly higher median scores.
- **Ethnicity vs. Y-BOCS:** No single group consistently higher; Asians slightly lower medians.
- **Family History:** Associated with higher median Y-BOCS scores.
- **Comorbidities:** Depression/Anxiety diagnoses linked to higher Y-BOCS scores.
- **Age & Duration:** Weak or negligible correlation with symptom severity.

### Symptom Types

- **Obsessions:** Most common are "Harm-related" and "Contamination".
- **Compulsions:** Most common are "Washing" and "Checking".

### Correlation Analysis

- **Obsessions & Compulsions:** Moderately positive correlation (r ≈ 0.51).
- **Age/Symptom Duration:** Very weak correlation with severity.

---

## 4. Data Preprocessing & Feature Engineering

- **Feature Engineering:** Created `Y_BOCS_Total` (sum of obsession and compulsion scores).
- **Preprocessing:** One-hot encoding for categorical variables; excluded irrelevant columns.

---

## 5. Predictive Modeling

- **Objective:** Predict `Y-BOCS Score (Obsessions)` using demographic and clinical features.
- **Model:** Linear Regression (baseline)
- **Data Split:** 80% training, 20% testing

### Results

- **Mean Squared Error (MSE):** 149.41
- **Root Mean Squared Error (RMSE):** 12.22
- **R-squared (R2):** -0.02

> **Interpretation:**  
> The negative R-squared indicates the linear model does not explain the variance in the target variable and performs worse than predicting the mean. This suggests non-linear relationships or complex interactions not captured by a simple linear model.

### Top Features (by absolute coefficient)

1. Obsession Type: Hoarding
2. Marital Status: Single
3. Ethnicity: Asian
4. Education Level: Some College
5. Previous Diagnoses: MDD
6. Medications: SNRI
7. Education Level: High School
8. Ethnicity: Caucasian
9. Compulsion Type: Washing
10. Obsession Type: Harm-related

*Note: Due to poor model performance, interpret coefficients with caution.*

---

## 6. Conclusion & Future Work

- **EDA** revealed key demographic and clinical patterns, including the impact of family history and comorbidities on symptom severity.
- **Predictive modeling** with linear regression was not effective, indicating the need for more advanced approaches.

### Future Directions

- Explore advanced models (Random Forest, Gradient Boosting, Neural Networks)
- Refine feature engineering and selection
- Tune model hyperparameters
- Consider alternative targets (e.g., total Y-BOCS, severity categories)
- Integrate external data if available
- Investigate causal relationships

By following these steps, the project aims to develop more robust models and deeper insights into OCD patient data.
