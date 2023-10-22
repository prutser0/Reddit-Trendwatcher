import praw
import re
from collections import Counter

# Reddit API credentials (Users need to fill these in)
CLIENT_ID = 'info'
CLIENT_SECRET = 'cK5vlHcylA_9Hf9rE1UhcQ'
USER_AGENT = 'tren'

# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

def get_tickers_from_subreddit(subreddit_name, post_limit=100):
    """
    Fetch posts from a subreddit and extract stock/crypto tickers.
    
    Args:
    - subreddit_name (str): The name of the subreddit.
    - post_limit (int): Number of posts to fetch.
    
    Returns:
    - Counter object with tickers and their counts.
    """
    # Fetch the subreddit and its hot posts
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.hot(limit=post_limit)

    # Placeholder for found tickers
    tickers = []

    # Regular expression to identify tickers (basic example)
    ticker_pattern = re.compile(r'\b[A-Z]{2,5}\b')

    for post in posts:
        tickers += re.findall(ticker_pattern, post.title)
        # Check comments as well
        for comment in post.comments:
            if isinstance(comment, praw.models.Comment):
                tickers += re.findall(ticker_pattern, comment.body)

    return Counter(tickers)


if __name__ == "__main__":
    subreddit_name = "wallstreetbets"
    tickers_count = get_tickers_from_subreddit(subreddit_name)
    print(f"Most mentioned tickers in {subreddit_name}:")
    for ticker, count in tickers_count.most_common(10):
        print(f"{ticker}: {count} mentions")
