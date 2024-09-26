# Twitter Term Analysis using Streamlit

This is a Streamlit application that analyzes tweets containing a specific search term from a dataset and provides key insights such as the number of tweets per day, unique users, average likes, top locations, times of day tweets were posted, and the most active user.

## Features

- **Tweets per Day**: Visualize the number of tweets containing a `search term` for each day.
- **Unique Users**: Count of unique users who posted tweets containing the `search term`.
- **Average Likes**: Displays the average number of likes for tweets containing the `search term`.
- **Top Locations**: Shows the top 10 locations (place IDs) from where the tweets originated for a given `search term`.
- **Tweet Times**: Displays the most frequent times of day tweets were posted for a given `search term`.
- **Top User**: Identifies the user who posted the most tweets containing the `search term`.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
    ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
    streamlit run app.py 'or' python -m streamlit run app.py
    ```
## Usage
    - The app opens in your web browser @ `http://localhost:8501` to access the application.
    - Enter a search term in the input field.
    - Click the "Analyze" button to generate the analysis.
    - Explore the visualizations and insights provided by the application.
    
## License
    This project is licensed under the MIT License.
    
## Acknowledgments
    - [Streamlit](https://streamlit.io/)
    - [Pandas](https://pandas.pydata.org/)
