# OCD Patient Dataset Analysis

## Project Overview
Comprehensive machine learning analysis of Obsessive-Compulsive Disorder (OCD) patient data to understand symptom patterns, predict severity levels, and identify factors associated with comorbid conditions.

## Dataset Summary
- **Total Patients**: 1,500
- **Features**: 17 clinical and demographic variables
- **Time Period**: 2013-2022 (diagnosis dates)
- **Data Quality**: Complete data with minimal missing values (16.5% in Previous Diagnoses, 25.7% in Medications)

## Key Features

### Demographic Information
- **Age**: 18-75 years (Mean: 46.8 years)
- **Gender**: Male/Female distribution
- **Ethnicity**: African, Asian, Caucasian, Hispanic
- **Marital Status**: Single, Married, Divorced
- **Education Level**: High School, Some College, College Degree, Graduate Degree

### Clinical Measurements
- **Y-BOCS Scores**: Yale-Brown Obsessive Compulsive Scale
  - Obsessions Score: 0-40 (Mean: 20.0)
  - Compulsions Score: 0-40 (Mean: 19.6)
  - Total Score: 0-80 (Mean: 39.7)
- **Duration of Symptoms**: 6-240 months (Mean: 121.7 months)
- **Family History of OCD**: Yes/No

### Symptom Profiles
- **Obsession Types**: Contamination, Harm-related, Hoarding, Religious, Symmetry
- **Compulsion Types**: Checking, Counting, Ordering, Praying, Washing

### Comorbidities
- **Depression Diagnosis**: ~50% prevalence
- **Anxiety Diagnosis**: ~50% prevalence
- **Previous Diagnoses**: MDD, GAD, PTSD, Panic Disorder

### Treatment
- **Medications**: SSRI, SNRI, Benzodiazepine
- **Medication Coverage**: 74.3% of patients on medication

## Analysis Objectives

### 1. Severity Classification
- Predict OCD severity levels based on Y-BOCS scores:
  - **Subclinical**: < 8
  - **Mild**: 8-15
  - **Moderate**: 16-23
  - **Severe**: 24-31
  - **Extreme**: ≥ 32

### 2. Comorbidity Prediction
- Identify patients at risk for depression and anxiety
- Analyze relationship between OCD severity and comorbid conditions

### 3. Y-BOCS Score Prediction
- Develop regression models to predict symptom severity
- Identify key predictive factors

### 4. Pattern Analysis
- Demographic factors influencing OCD severity
- Family history impact on symptom presentation
- Treatment patterns across different patient groups
- Obsession-compulsion type correlations

## Machine Learning Models

### Classification Models
- **Random Forest Classifier**: Severity level prediction
- **Logistic Regression**: Comorbidity risk assessment

### Regression Models
- **Gradient Boosting Regressor**: Y-BOCS score prediction

### Model Evaluation Metrics
- Accuracy, Precision, Recall, F1-Score
- Confusion Matrix Analysis
- Feature Importance Rankings
- R² Score and RMSE for regression

## Key Insights

### Clinical Findings
1. **Severity Distribution**: Patients span all severity levels with significant representation in moderate-severe categories
2. **Comorbidity Correlation**: Strong association between higher Y-BOCS scores and presence of depression/anxiety
3. **Family History**: Positive family history present in ~50% of cases
4. **Symptom Duration**: Average symptom duration of 10+ years before diagnosis

### Demographic Patterns
1. **Age Distribution**: OCD affects all age groups with peak prevalence in middle age
2. **Gender Balance**: Relatively equal distribution between males and females
3. **Education Impact**: Varied education levels across all severity categories

### Treatment Insights
1. **Medication Usage**: SSRIs most commonly prescribed (primary treatment)
2. **Treatment Gaps**: ~26% of patients not on medication
3. **Medication by Severity**: Higher severity correlates with medication use

## Technical Implementation

### Technologies Used
- **Python 3.x**
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Machine Learning**: Scikit-learn
- **Environment**: Jupyter Notebook

### Analysis Pipeline
1. Data loading and preprocessing
2. Exploratory data analysis with visualizations
3. Feature engineering (severity categories, comorbidity flags)
4. Model training and evaluation
5. Feature importance analysis
6. Results interpretation and insights

## Files in This Project

- **OCD_dataset.csv**: Raw patient data (1,500 records)
- **OCD_Analysis_upgraded.ipynb**: Complete analysis notebook with models
- **requirements.txt**: Python dependencies
- **1ntro.md**: This documentation file

## Clinical Relevance

This analysis provides valuable insights for:
- **Early Intervention**: Identifying high-risk patients for comorbid conditions
- **Treatment Planning**: Understanding factors that influence severity
- **Resource Allocation**: Targeting patients who need intensive treatment
- **Research**: Contributing to understanding of OCD patterns and predictors

## Future Enhancements

- Longitudinal analysis of treatment outcomes
- Deep learning models for complex pattern recognition
- Integration with treatment response data
- Subgroup analysis by demographic factors
- Predictive modeling for treatment efficacy

## Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Run the analysis
jupyter notebook OCD_Analysis_upgraded.ipynb
```

## Notes

- Y-BOCS (Yale-Brown Obsessive Compulsive Scale) is the gold standard for measuring OCD severity
- Missing data handled appropriately in analysis
- Models validated using train-test split and cross-validation
- Results should be interpreted in clinical context

---

**Disclaimer**: This analysis is for educational and research purposes. Clinical decisions should be made by qualified healthcare professionals.
