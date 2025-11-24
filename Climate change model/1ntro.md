# Climate Change Sentiment Analysis

This repository contains a comprehensive analysis of social media discussions surrounding climate change. The project leverages Natural Language Processing (NLP) and machine learning techniques to uncover public sentiment, identify key topics, and understand the dynamics of online engagement with climate-related content.

## Project Overview

The core of this project is a Jupyter Notebook, `climate_change_analysis.ipynb`, which provides a step-by-step walkthrough of the data analysis process. The analysis includes:

-   **Data Exploration and Cleaning:** Initial assessment and preprocessing of the raw data to prepare it for analysis.
-   **Advanced Visualizations:** Use of Plotly and Seaborn to create insightful charts and graphs.
-   **Sentiment Analysis:** Application of TextBlob to classify the sentiment of social media posts as positive, negative, or neutral.
-   **Temporal Analysis:** Examination of trends in posting frequency and sentiment over time.
-   **Textual Analysis:** Word frequency analysis and word clouds to highlight the most discussed terms.
-   **Engagement Analysis:** Correlation analysis between likes, comments, and sentiment scores.
-   **Predictive Modeling:** Building machine learning models to predict user engagement (likes) based on post characteristics.

## Data Source

The analysis is based on the `climate_nasa.csv` dataset, which contains the following columns:
-   `date`: Timestamp of the post.
-   `likesCount`: Number of likes on the post.
-   `profileName`: Anonymized user profile identifier.
-   `commentsCount`: Number of comments on the post.
-   `text`: The text content of the post.

## Key Findings

-   **Sentiment Distribution:** A significant portion of the conversation is neutral, with a substantial number of positive posts and a smaller, but notable, number of negative posts.
-   **Engagement Dynamics:** Posts with positive and negative sentiment tend to receive more likes on average than neutral posts.
-   **Core Topics:** The most frequent words include "climate," "change," "global," and "warming," indicating a focus on the central issues.
-   **Temporal Trends:** The volume of posts and average sentiment polarity show fluctuations over time, suggesting that specific events or news may influence the conversation.
-   **Predictive Insights:** Machine learning models, particularly Random Forest, demonstrate the ability to predict the number of likes a post will receive based on its content and sentiment.

## Technologies and Libraries

The analysis is conducted in a Python environment, utilizing the following key libraries as listed in `requirements.txt`:

-   `pandas` for data manipulation.
-   `numpy` for numerical operations.
-   `matplotlib`, `seaborn`, and `plotly` for data visualization.
-   `textblob` for sentiment analysis.
--  `wordcloud` for generating word clouds.
-   `scikit-learn` for machine learning.

## How to Run the Analysis

1.  Ensure you have Python and the required libraries installed. You can install the dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
2.  Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
3.  Open and run the `climate_change_analysis.ipynb` notebook to see the full analysis.
