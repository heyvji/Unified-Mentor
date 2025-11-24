# Netflix Content Analysis & Prediction

## Project Overview
This project performs comprehensive data analysis on Netflix's content catalog and builds machine learning models to classify content types (Movies vs TV Shows). The analysis includes data cleaning, exploratory data analysis, feature engineering, and predictive modeling.

## Dataset
- **Source**: Netflix content catalog (Netflix.csv)
- **Size**: 8,790 entries
- **Features**: 10 columns including show_id, type, title, director, country, date_added, release_year, rating, duration, and listed_in

## Project Workflow

### 1. Library Imports
Essential Python libraries for data analysis and machine learning:
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Machine Learning**: scikit-learn (RandomForest, GradientBoosting, LogisticRegression)
- **Metrics**: classification_report, confusion_matrix, ROC-AUC

### 2. Data Loading
Loads the Netflix dataset and displays initial structure, shape, and sample records.

### 3. Data Cleaning
- Handles missing values in director, country, date_added, and rating columns
- Fills missing categorical data with appropriate defaults ('Unknown', 'Not Rated')
- Removes rows with missing critical information (duration, listed_in)

### 4. Exploratory Data Analysis (EDA)
Analyzes content distribution, trends, and patterns:
- Content type distribution (Movies vs TV Shows)
- Release year trends
- Country-wise content production
- Rating distributions
- Genre analysis

### 5. Feature Engineering
Creates new features from existing data to improve model performance:
- Extracts numeric duration values
- Processes date information
- Encodes categorical variables
- Creates derived features

### 6. Model Selection & Training
Implements multiple classification algorithms:
- **Random Forest Classifier**: Ensemble learning method
- **Gradient Boosting Classifier**: Boosting technique
- **Logistic Regression**: Baseline linear model

### 7. Model Evaluation
Evaluates model performance using:
- Accuracy scores
- Confusion matrices
- Classification reports (precision, recall, F1-score)
- ROC-AUC curves
- Cross-validation scores

### 8. Performance Analysis
Compares models and identifies the best performer for content type classification.

## Key Insights
The analysis reveals patterns in Netflix's content strategy, including content type preferences, regional production trends, and temporal patterns in content additions.

## Technologies Used
- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn

## Files
- `Netflix data science.ipynb`: Main Jupyter notebook with complete analysis
- `Netflix.csv`: Dataset file
- `1ntro.md`: Project documentation

## Usage
1. Ensure all required libraries are installed
2. Place Netflix.csv in the same directory as the notebook
3. Run cells sequentially in the Jupyter notebook
4. Review visualizations and model results

## Results
The project successfully builds predictive models to classify Netflix content types with detailed performance metrics and visualizations.
