#!/usr/bin/env python3

import datetime
import time
import tweepy

client = tweepy.Client(
    consumer_key="YOUR_CONSUMER_KEY",
    consumer_secret="YOUR_CONSUMER_SECRET",
    access_token="YOUR_ACCESS_TOKEN",
    access_token_secret="YOUR_ACCESS_TOKEN_SECRET",
)

# Important user details
my_user_details = client.get_me(expansions="pinned_tweet_id")
my_user_id = my_user_details.data.id
my_pinned_tweet = my_user_details.includes.get("tweets")[0].id

# Date and time stuff
right_now = time.time()
older_than_x_days = 14
my_end_date = right_now - older_than_x_days * 86400
dt = datetime.datetime.fromtimestamp(my_end_date).strftime("%Y-%m-%dT%H:%M:%SZ")

# This is where the magic happens
def main():
    old_tweets = client.get_users_tweets(my_user_id, end_time=dt, max_results=50, user_auth=True)

    for item in old_tweets[0]:
        if item.id != my_pinned_tweet:
            print(f"[+] Deleting {item.id}")
            client.delete_tweet(item.id)
        else:
            print(f"[!] Skipping pinned tweet id {my_pinned_tweet}")


if __name__ == "__main__":
    main()