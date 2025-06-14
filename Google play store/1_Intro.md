# Google Play Store Data Analysis

## Project Overview

This project analyzes the characteristics of applications available on the Google Play Store. Using two primary datasets (`googleplaystore.csv` and `googleplaystore_user_reviews.csv`), the analysis identifies trends, outliers, and patterns within the app market, and builds a predictive model for app ratings.

---

## Objective

The main goals of this data science project are:

- **Explore and understand** the structure and content of the Google Play Store apps and user review datasets.
- **Perform thorough data cleaning and preprocessing** to ensure data quality.
- **Conduct Exploratory Data Analysis (EDA)** to uncover insights into app ratings, categories, types (free vs. paid), sizes, installation counts, and user sentiment.
- **Build and evaluate a machine learning model** to predict app ratings based on various app characteristics.

---

## Datasets

The project utilizes the following datasets:

- **`googleplaystore (1).csv`**: Contains details about various apps on the Google Play Store, including category, rating, reviews, size, installs, type, price, content rating, genres, and last updated date.
- **`googleplaystore_user_reviews (1).csv`**: Contains user reviews for various apps, along with sentiment polarity and sentiment subjectivity.

---

## Project Structure and Methodology

The project follows a standard data science pipeline:

### 1. Data Loading

- Both datasets are loaded into pandas DataFrames.

### 2. Initial Data Inspection

- Preliminary examination of both datasets to understand their shape, display the first few rows, check data types, and view descriptive statistics.
- Identify initial data quality issues.

### 3. Data Cleaning and Preprocessing

**For `df_apps` (Google Play Store Apps Data):**
- Remove a known problematic row (App: 'Life Made WI-FI Touchscreen Photo Frame') with corrupted 'Category' data.
- Drop missing values in the 'Rating' column.
- Impute missing values in 'Current Ver', 'Android Ver', 'Type', and 'Content Rating' using appropriate strategies.
- Clean and convert data types:
    - Convert 'Reviews', 'Installs', and 'Price' to numeric types.
    - Convert 'Size' to MB and handle 'Varies with device' entries.
    - Convert 'Last Updated' to datetime.

**For `df_reviews` (User Reviews Data):**
- Drop rows with missing 'Translated_Review'.

**Merging Datasets:**
- Merge cleaned `df_apps` and `df_reviews` on the 'App' column after standardizing app names.

### 4. Exploratory Data Analysis (EDA)

- Visualize and analyze:
    - Distribution of app ratings
    - Top categories by app count
    - Distribution of app types (free vs. paid)
    - Relationship between app size and installs
    - Impact of content rating on app ratings
    - Sentiment analysis of user reviews
    - Average sentiment score per app
    - Installs vs. reviews correlation
    - Category vs. average rating
    - Price vs. rating for paid apps
    - Relationship between app rating and sentiment score
    - Most reviewed and highest installed apps

### 5. Feature Engineering and Model Preparation

- Select key features: 'Category', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating'
- Log-transform 'Installs' and 'Reviews' to address skewness
- Set up a preprocessing pipeline using `ColumnTransformer` for scaling and encoding
- Split data into training and testing sets

### 6. Model Building and Training

- Use `RandomForestRegressor` within a pipeline for predicting app ratings
- Train the model on preprocessed data

### 7. Model Evaluation

- Make predictions on the test set
- Evaluate using metrics: MAE, MSE, RMSE, R-squared
- Visualize actual vs. predicted ratings and residuals

---

## Key Findings and Conclusion

- The Google Play Store is dominated by free apps, with 'Family' and 'Game' as the most common categories.
- Most apps have high ratings (4.0-4.5), supported by positive user reviews.
- Strong correlation between number of reviews and installs.
- App size does not directly correlate with installs, but higher installs mean more reviews.
- The Random Forest model predicts app ratings with reasonable accuracy, showing the influence of app characteristics on perceived quality.

---

## Future Enhancements

- **Hyperparameter Tuning**: Optimize models using GridSearchCV or RandomizedSearchCV.
- **More Complex Models**: Explore Gradient Boosting, XGBoost, Neural Networks.
- **Feature Engineering**: Extract features from 'Last Updated', analyze 'App Name' or 'Genres'.
- **Outlier Treatment**: Implement advanced outlier detection.
- **Cross-Validation**: Use k-fold cross-validation for robust evaluation.oogle Play Store Data Analysis