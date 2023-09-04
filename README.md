# Twitter Sentiment Analysis with Python

## Overview

This Python script allows you to analyze the sentiment of tweets based on a specified hashtag using Tweepy and VADER Sentiment Analysis.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- Python installed.
- A Twitter Developer account with API access credentials (consumer_key, consumer_secret, access_token, access_token_secret).
- Necessary Python libraries installed using `pip install tweepy pandas numpy matplotlib vaderSentiment`.

## Usage

1. Clone this repository or download the script:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   ```

2. Create a `Twitter_config.py` file in the same directory with your Twitter API credentials:

   ```python
   consumer_key = "YOUR_CONSUMER_KEY"
   consumer_secret = "YOUR_CONSUMER_SECRET"
   access_token = "YOUR_ACCESS_TOKEN"
   access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
   ```

3. Run the script:

   ```bash
   python twitter_sentiment_analysis.py
   ```

4. Enter the hashtag you want to analyze when prompted.

5. The script will fetch tweets containing the specified hashtag, clean the data, perform sentiment analysis using VADER, and display histograms of sentiment scores.

## Example

Here's an example of how to use the script:

```bash
Type your hashtag: #OpenAI
```

## Output

The script will generate a CSV file `tweets.csv` containing the date and cleaned tweet text. It will also display histograms of sentiment scores (Positive, Negative, Compound, and Neutral) using Matplotlib.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Tweepy](https://www.tweepy.org/)
- [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment)
- [Matplotlib](https://matplotlib.org/)
