# Climate Change Discussion Analysis

Welcome to the **Climate Change Discussion Analysis** project! This project explores social media conversations about climate change, using data-driven methods to extract insights and predict engagement.

## Project Overview

This project analyzes a dataset of social media comments related to climate change. The workflow includes:

- **Data preprocessing**
- **Sentiment analysis**
- **Exploratory data analysis (EDA)**
- **Text and temporal trend analysis**
- **Predictive modeling for engagement**

The main objective is to uncover public sentiment, key discussion points, and factors influencing user interaction (e.g., likes).

## Data Source

- **Dataset:** `climate_nasa.csv`
- **Contents:** Social media comments with fields such as `date`, `likesCount`, `profileName`, `commentsCount`, and `text`.

## Analysis Workflow

The analysis is performed using the Python script `social_media_climate_analysis.py` and follows these steps:

### 1. Data Loading & Exploration

- Load the dataset and inspect its structure.
- Check for missing values and basic statistics.

### 2. Data Preprocessing & Feature Engineering

- Convert `date` to datetime format.
- Extract `year` and `month_year` for temporal analysis.
- Clean text (lowercase, remove URLs, mentions, hashtags, punctuation, numbers).
- Add a `text_length` feature.

### 3. Sentiment Analysis

- Use TextBlob to compute sentiment polarity.
- Categorize comments as Positive, Negative, or Neutral.
- Visualize sentiment distribution.

### 4. Engagement Analysis

- Analyze average `likesCount` and `commentsCount` by sentiment.
- Compute correlations between engagement metrics and features.
- Visualize with heatmaps.

### 5. Basic Text Analysis

- Identify and visualize the top 20 most common words (excluding stop words and climate-specific terms).

### 6. Temporal Analysis

- Track average sentiment polarity and comment volume over time.

### 7. Predictive Modeling

- **Target:** Predict `likesCount`.
- **Features:** Sentiment polarity, text length, comments count.
- **Models:** Linear Regression (baseline) and Random Forest Regressor (ensemble).
- **Evaluation:** Mean Squared Error (MSE), R-squared (R²), feature importance, and actual vs. predicted plots.

## Key Findings

- **Sentiment Distribution:** Insights into the emotional tone of climate change discussions.
- **Engagement Drivers:** Factors (sentiment, text length, comments count) that influence likes.
- **Common Themes:** Frequently discussed words and topics.
- **Temporal Trends:** Changes in discussion volume and sentiment over time.
- **Predictive Power:** Machine learning models (especially Random Forest) can predict engagement based on comment features.

## Future Enhancements

- **Advanced NLP:** Use TF-IDF, word embeddings, or pre-trained models (e.g., BERT).
- **Model Tuning:** Hyperparameter optimization and cross-validation.
- **Complex Models:** Try XGBoost, LightGBM, or deep learning (LSTM).
- **Topic Modeling:** Use LDA or NMF to extract latent topics.
- **Multi-Target Prediction:** Predict other metrics like comments count or composite engagement.
- **Qualitative Analysis:** Investigate misclassified or poorly predicted comments.
- **Interactive Dashboard:** Deploy results with Streamlit or Dash for interactive exploration.

This project demonstrates how data science techniques can provide actionable insights into online climate change discussions and help predict what drives engagement.