# tweet_cleaner
Deletes tweets older than X number of days and skip pinned tweets.

## Install
1. Download files
2. `poetry install`
3. Rename config_sample.py to config.py and put your Twitter API keys and secrets in it
4. `chmod u+x delete_tweets.py`

## Usage
**From the CLI**

`python3 delete_tweets.py X` or `./delete_tweets.py X` (where **X** is the number of days you want to skip)
- Delete tweets older than 7 days: `python3 delete_tweets.py 7`
- Delete tweets older than 365 days: `python3 delete_tweets.py 365`

**cron examples**

Another option is to put the script on a server somewhere and run it regularly using crontab:

Every 16 minutes - `*/16 * * * * python3 /home/username/tools/tweet_cleaner/delete_tweets.py 7 >> /home/username/tools/tweet_cleaner/cron.log`

Every day at 0100 - `0 1 * * * python3 /home/username/tools/tweet_cleaner/delete_tweets.py 7 >> /home/username/tools/tweet_cleaner/cron.log`

Deleted Tweet IDs will be appended to cron.log

### Sample output
```
Searching for tweets older than 7 days
  [+] Deleting 1556692985852530688
  [+] Deleting 1556675626005712898
  [+] Deleting 1556674409112281088
  
  <snip for brevity>
  
  [+] Deleting 1555535089043263490
  [+] Deleting 1555505187011248128
  [!] Skipping pinned tweet id 1526997212445564928
  ---> Removed 40 tweets <---
```

## Limitations
Can only delete 50 tweets every 15 minutes due to API restrictions, but once you're down to a reasonable number it will keep up.


