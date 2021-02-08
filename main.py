import tweepy
from keys import Keys

auth = tweepy.OAuthHandler(Keys.CONSUMER_KEY, Keys.CONSUMER_SECRET)
auth.set_access_token(Keys.ACCESS_KEY, Keys.ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'lastSeenId.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


last_seen_id = retrieve_last_seen_id(FILE_NAME)

mention = api.mentions_timeline(
    last_seen_id,
    tweet_mode='extended'
)

# print(mention[0].__dict__.keys())  # printing keys of the dictionary
# print(mention[0].full_text)  # printing text of the tweet
# print(mention[4].id)  # printing id

for singleMention in reversed(mention):
    print(str(singleMention.id) + ' - ' + singleMention.full_text)  # printing all my tweets
    last_seen_id = singleMention.id
    store_last_seen_id(last_seen_id, FILE_NAME)
    if 'hello friend' in singleMention.full_text.lower():
        print('Found something')
        api.update_status('@' + singleMention.user.screen_name +
                          ' Hello Friend, maybe I should give a name to you'
                          ', but again that\'s a slippery slope.', singleMention.id)

