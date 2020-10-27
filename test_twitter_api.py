#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import twitter


# Connect to Twitter API

api = twitter.Api(consumer_key='your_consumer_key',
  consumer_secret='your_consumer_secret',
    access_token_key='your_access_token_key',
    access_token_secret='your_access_token_secret')

print(api.VerifyCredentials())

# List tweets for news feed

api.GetSearch(term='news', since=2020-10-25, count=10)
print(api.comment)

# List all the followers

followers = api.GetFollowers()
followers = []
for name in followers:
	print(name)
	followers.append(name)

# List tweets for followers

followers = api.GetFollowers()
followers = []
for name in followers:
	print(name)
	followers.append(name)


for name in followers:
	tweets = api.GetUserTimeline(screen_name=name)
	for tweet in tweets:
		print(name, tweet)

