*because of reddits new rate limit, you will have to wait between comments*


First, import praw and time.

In order to use this bot, you will need a client id, client secret, username and password to satisfy Reddit's API credentials.
This can be found after creating an app at reddit.cim/prefs/aoos and your user name and password are the login credentials of your account.

For this project, I am using a throwaway account with the username RedditFinalBot with the password Theomnivision1. Feel free to use it

Enter the keytword, this will be the word that this bot will search for to comment in.
Next, enter the reply_message. This is the reply you want the bot to comment. and then you will enter the specific subreddit you wish to search.

You will then create a reddit instance from the bot class.
then you will use a monitor_comments function which will search reddit for your keyword.

Then you will use a try-except block which will post the actual comment followed by utilizing async to put the bot in sleep for 60 seconds before posting another comment.
then, you use process_comment to reply to the comment.

Then, you will use a function to monitor the comments.
