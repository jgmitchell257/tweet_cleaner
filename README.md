# tweet_cleaner
Deletes tweets older than X number of days and skip pinned tweets.

`python3 delete_tweets.py X` (where is the number of days you want to skip)
- Delete tweets older than 7 days: `python3 delete_tweets.py 7`
- Delete tweets older than 365 days: `python3 delete_tweets.py 365`

## Intsall
1. Download files
2. `poetry install`
3. Create config.py file and put your Twitter API keys and secrets in it
4. `chmod u+x delete_tweets.py`

## limitations
Can only delete 50 tweets every 15 minutes due to API restrictions, but once you're down to a reasonable number it will keep up.

Another option is to put the script on a server somewhere and run it it every 16+ minutes or so using crontab:
`*/16 * * * * python3 /home/username/tools/tweet_cleaner/delete_tweets.py 7 >> /home/username/tools/tweet_cleaner/cron.log`

Deleted Tweet IDs will be appended to cron.log
