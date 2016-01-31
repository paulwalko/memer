import tweepy, random
import sopel.module

@sopel.module.commands('trump')
def trump(bot, trigger):
	consumer_key = "R3RIRZ9B6UxhdaHqYRPujbOBo"
	consumer_secret = "OXmfGjuINfGuGy0pPHlp0xIhPirRHO84I0J9ipGGh3F2UAx2gI"
	access_token = "553052831-cW2ph0YocqPeLGp9BOhoaShfUAp4gbsg1VAwOO2H"
	access_token_secret = "eAVMCB7P9WSIDk3j2UCqSSb0SVlELnGSkssJsTElfwCkL"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	tweets = api.user_timeline(screen_name = 'realDonaldTrump', count = 20, include_rts = False)
	tweet = random.choice(tweets)
	bot.say(tweet.text)
