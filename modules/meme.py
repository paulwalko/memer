import sopel.module
import json, random, sys, os
sys.path.append(os.getcwd())
from img2txt import *
import urllib.request

@sopel.module.commands('meme')
def meme(bot, trigger):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	url = "https://api.imgflip.com/get_memes"
	headers={'User-Agent':user_agent,} 
	request=urllib.request.Request(url,None,headers)

	with urllib.request.urlopen(request) as response, open('data.json', 'wb') as out_file:
		data = response.read()
		out_file.write(data)

	with open('data.json') as data_file:
		jsonResponse = json.load(data_file)
	
	jsonList = jsonResponse["data"]
	memeList = jsonList["memes"]
	memeData = random.choice(memeList)
	memeURL = memeData.get("url")
	print(memeURL)	
	request=urllib.request.Request(memeURL,None,headers)
	
	with urllib.request.urlopen(request) as response, open('image.jpg', 'wb') as out_file:
		data = response.read()
		out_file.write(data)

	picStr = img2str('image.jpg')
	strList = picStr.split('\n')
	for i in strList:
		bot.say(i)
