import praw
import time




# Reddit API credentials
client_id = 'zhqVoye8iz6Exe9Bk_n8pw'
client_secret = 'mCJ98inv4C-FvSfZ7r-N4HHrq6on7w'
username = 'RedditBotFinal'
password = 'Theomnivision1'
user_agent = '<RedditBot:1.0>'




# Keyword to monitor
keyword = 'Trump'




# Reply message
reply_message = 'This is about Trump.'



# Subreddit to monitor
subreddit_name = 'Politics'



# Create a Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)



def monitor_comments():
    subreddit = reddit.subreddit(subreddit_name)

    print(f"Monitoring comments in /r/{subreddit_name}. Press Ctrl+C to exit.")

    while True:
        try:
            for comment in subreddit.stream.comments(skip_existing=True):
                process_comment(comment)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(90)  # Wait for a minute before retrying



def process_comment(comment):
  if keyword.lower() in comment.body.lower():
      # Reply to the comment
      comment.reply(reply_message)
      print(f"Replied to comment {comment.id} in /r/{subreddit_name}.")




if __name__ == "__main__":
  monitor_comments()
