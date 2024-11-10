# Simple News Aggregator

This project scrapes news headlines, summaries, and sources from the BBC website and saves them to a CSV file.

## Requirements
- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `pandas`

## How to Run
1. Install the required packages:
   ```bash
   pip install requests beautifulsoup4 pandas
2. Run the script:
   python simple_news_aggregator.py
Output

The script saves the scraped news data to a CSV file called simple_news_aggregator.csv.

Challenges Faced

One challenge was managing multiple class names used across similar elements on the BBC website. To handle this, I specified multiple class names for parsing, allowing the script to scrape different sections consistently.

