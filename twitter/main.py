import tweepy,csv,json
from Credentials import *
import time


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Authentication
api = tweepy.API(auth,wait_on_rate_limit=True)
print(api)


search_lst=['Sarcasm','TooSoon','sarcasm','JustSaying']


for hashtag in search_lst:
	i=0
	file = open(hashtag + '.csv', 'w') #if already present add more
	ptr = csv.writer(file)
	ptr.writerow(['id','timestamp','tweet','userid','name','screen_name'])
	for tweet in tweepy.Cursor(api.search,q=hashtag,lang="en").items():
  
		if(i<50):
			print("**************************************",i,"**********************************************")
			print (tweet.id,'\n',tweet.created_at, tweet.text,'\n',tweet.user.id,'\t',tweet.user.name,'\t',tweet.user.screen_name)
			print("*****************************************************************************************")
			ptr.writerow([tweet.id,tweet.created_at, tweet.text.encode('utf-8'),tweet.user.id,tweet.user.name,tweet.user.screen_name])
			i=i+1
		else:
			break	
	time.sleep(15)
	print('sleeping baby')



