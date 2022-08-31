#!/usr/bin/env python3

import datetime
import sys
import time
import tweepy
import config

client = tweepy.Client(
    consumer_key=config.CONSUMER_KEY,
    consumer_secret=config.CONSUMER_SECRET,
    access_token=config.ACCESS_TOKEN,
    access_token_secret=config.ACCESS_TOKEN_SECRET,
)

# Important user details
my_user_details = client.get_me(expansions="pinned_tweet_id")
my_user_id = my_user_details.data.id
my_pinned_tweet = my_user_details.includes.get("tweets")[0].id

# Date and time stuff
right_now = time.time()
if sys.argv[1]:
    older_than_x_days = sys.argv[1]
else:
    older_than_x_days = 14
my_end_date = right_now - int(older_than_x_days) * 86400
dt = datetime.datetime.fromtimestamp(my_end_date).strftime("%Y-%m-%dT%H:%M:%SZ")

# This is where the magic happens
def main():
    old_tweets = client.get_users_tweets(my_user_id, end_time=dt, max_results=50, user_auth=True)
    print(f"Searching for tweets older than {older_than_x_days} days")
    number_of_deleted = 0
    for item in old_tweets[0]:
        if item.id != my_pinned_tweet:
            print(f"  [+] Deleting {item.id}")
            client.delete_tweet(item.id)
            number_of_deleted += 1
        else:
            print(f"  [!] Skipping pinned tweet id {my_pinned_tweet}")
    print(f"  ---> Removed {number_of_deleted} tweets <---\n")


if __name__ == "__main__":
    main()