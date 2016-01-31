import tweepy, random
import sopel.module

@sopel.module.commands('trump')
def trump(bot, trigger):
	consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXX"
	consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXX"
	access_token = "XXXXXXXXXXXXXXXXXXXXXXXXX"
	access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXX"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	tweets = api.user_timeline(screen_name = 'realDonaldTrump', count = 20, include_rts = False)
	tweet = random.choice(tweets)
	bot.say(tweet.text)
