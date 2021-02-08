import tweepy
from keys import Keys

auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
api = tweepy.API(auth)

mention = api.mentions_timeline()

print(mention[0].__dict__.keys())  # printing keys of the dictionary
print(mention[0].text)  # printing text of the tweet

for singleMention in mention:
    print(str(singleMention.id) + ' - ' + singleMention.text)  # printing all my tweets
    if 'hello friend' in singleMention.text.lower():
        print('Found something')

