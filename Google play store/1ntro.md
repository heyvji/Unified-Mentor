# Google Play Store Analysis

**Objective:** Analyze the Google Play Store apps dataset to understand app characteristics, user sentiments, and market trends.

This project performs a comprehensive analysis of the Google Play Store dataset. The analysis covers the following key areas:

### 1. Data Cleaning and Preprocessing
- Loaded and inspected two datasets: `googleplaystore.csv` and `googleplaystore_user_reviews.csv`.
- Handled missing values in the 'Rating' column by filling them with the median.
- Parsed and cleaned the 'Size', 'Installs', and 'Price' columns to convert them into numeric types for analysis.
- Converted the 'Last Updated' column to a datetime format.
- Cleaned the user reviews dataset by removing rows with missing sentiment data.

### 2. Exploratory Data Analysis (EDA)
- Investigated the distribution of app ratings, categories, types (free vs. paid), and content ratings.
- Analyzed user sentiment distribution (Positive, Negative, Neutral).
- Visualized the relationships between different features, such as installs vs. rating.

### 3. Key Insights and Visualizations
- **Rating Distribution:** The majority of apps have ratings between 4.0 and 4.7.
- **Top Categories:** The 'FAMILY', 'GAME', and 'TOOLS' categories have the highest number of apps.
- **App Types:** Approximately 92.6% of the apps in the store are free.
- **User Sentiment:** A majority of user reviews are positive (64.1%).
- **Correlation:** A correlation matrix was generated to understand the relationships between numeric features like 'Rating', 'Reviews', 'Size', 'Installs', and 'Price'.

### 4. Advanced Analysis
- Merged the app data with user reviews to analyze sentiment on a per-category basis.
- Identified the top-rated and most-installed apps to understand markers of success on the platform.

This analysis provides valuable insights for app developers, marketers, and data scientists interested in the mobile app ecosystem.
