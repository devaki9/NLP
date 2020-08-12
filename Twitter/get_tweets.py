import tweepy,csv,json
from Credentials import *
import time


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#Authentication
api = tweepy.API(auth,wait_on_rate_limit=True)
print(api)

filename='realtime_ds.csv'

search_lst=['Sarcasm','TooSoon','sarcasm','JustSaying']
label=-1
for hashtag in search_lst:
	i=0
	file = open(filename, 'w+') 
	ptr = csv.writer(file)

	for tweet in tweepy.Cursor(api.search,q=hashtag,lang="en").items():
  
		if(i<50):
			print("**************************************",i,"**********************************************")
			print (tweet.text)
			print("*****************************************************************************************")
			ptr.writerow([label,tweet.text.encode('utf-8')])
			i=i+1
		else:
			break	
	time.sleep(15)
	print('sleeping')



