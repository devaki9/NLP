import pandas as pd
from get_user_media import *
import os,json
from func import getCredentials
from hashtag import *
from helper.access_token import AccessToken
import datetime




def AccessInstagramAPI():
	params = getCredentials() 
	params['debug'] = 'yes' 
	response = AccessToken( params ) 


def AccessYourAccount():
	#GETTING USER POSTS AND COMMENTS

	params=getCredentials()
	params['debug'] = 'no'
	response = getUserMedia(params)


	response_json=dict()
	i=0
	response_json['id'] = dict()
	response_json['permalink'] = dict()
	response_json['caption'] = dict()
	response_json['media_type'] = dict()
	response_json['timestamp'] = dict()
	response_json['comments'] = dict()
	response_json['like_count'] = dict()

	for post in response['json_data']['data'] :
		print ("\n\n---------- POST ----------\n") 
		print ("\nPost_id:")
		print (post['id'])

		response_json['id'][i] = post['id']

		print ("\nLink to post:") 
		print (post['permalink'])
		response_json['permalink'][i] = post['permalink']

		print ("\nPost caption:") 
		print (post['caption']) 
		response_json['caption'][i] = post['caption']

		print ("\nMedia type:") 
		print (post['media_type'])
		response_json['media_type'][i] = post['media_type']

		print ("\nPosted at:") 
		print (post['timestamp']) 
		response_json['timestamp'][i] = post['timestamp']
		

		if('comments' in post):
			j=0
			response_json['comments'][i]=dict()
			for com in post['comments']['data']:
					response_json['comments'][i][j] = com
					j+=1
		else:
			response_json['comments'][i]="null"
		print (post['like_count'])
		response_json['like_count'][i] = post['like_count']
		i=i+1
		


	os.chdir('/home/devaki/Desktop/insta')
	req = json.dumps(response_json)
	df=pd.read_json(req)
	df.to_csv('Insta_posts.csv',index=False)
	



def getPopularMedia():

	str_hashtag=input('Enter hashtag:#')
	
	params=getCredentials()
	params['hashtag_name'] = str_hashtag 
	hashtagInfoResponse = getHashtagInfo( params ) 
	params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; 
	params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id'];

	filename=str_hashtag+'_top'+'.csv'
	

	print ("\n\n\n\t-------------------HASHTAG INFO -----------------------\n")
	print ("\nHashtag: " + str_hashtag) 
	print ("Hashtag ID: " + params['hashtag_id']) 

	print ("\n\n\n\t\t\t ------------------- HASHTAG TOP MEDIA --------------------\n") 
	params['type'] = 'top_media' 
	hashtagPopularMediaResponse = getHashtagMedia( params ) 
	
	print(hashtagPopularMediaResponse)


	hashtag_response=dict()
	hashtag_response['id']=dict()
	hashtag_response['permalink']=dict()
	hashtag_response['caption']=dict()
	hashtag_response['media_type']=dict()
	hashtag_response['like_count']=dict()
	hashtag_response['comments_count']=dict()

	i=0

	for post in hashtagPopularMediaResponse['json_data']['data'] :

		
		print ("\n\n---------- POST ----------\n") 
		print ("Postid:")
		print (post['id'])

		hashtag_response['id'][i]=post['id']
			
		print ("Link to post:") 
		print (post['permalink']) 
		hashtag_response['permalink'][i]=post['permalink']
		

		print ("\nPost caption:") 
		print (post['caption']) 
		hashtag_response['caption'][i]=post['caption']
		

		print ("\nMedia type:") 
		print (post['media_type']) 
		hashtag_response['media_type'][i]=post['media_type']

		print ("\nlike_count:") 
		print (post['like_count']) 
		hashtag_response['like_count'][i]=post['like_count']

		print ("\nComments:") 
		print (post['comments_count']) 
		hashtag_response['comments_count'][i]=post['comments_count']
		
		i+=1

	req = json.dumps(hashtag_response)
	df=pd.read_json(req)
	df.to_csv(filename,index=False)



def getRecentMedia():

	str_hashtag=input('Enter hashtag:#')
	
	params=getCredentials()
	params['hashtag_name'] = str_hashtag 
	hashtagInfoResponse = getHashtagInfo( params ) 
	params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; 
	params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id'];

	filename=str_hashtag+'_recent'+'.csv'
	

	print ("\n\n\n\t-------------------HASHTAG INFO -----------------------\n")
	print ("\nHashtag: " + str_hashtag) 
	print ("Hashtag ID: " + params['hashtag_id']) 

	print ("\n\n\n\t\t\t ------------------- HASHTAG RECENT MEDIA --------------------\n") 
	params['type'] = 'recent_media' 
	hashtagRecentMediaResponse = getHashtagMedia( params ) 
	
	hashtag_response=dict()
	hashtag_response['id']=dict()
	hashtag_response['permalink']=dict()
	hashtag_response['caption']=dict()
	hashtag_response['media_type']=dict()
	hashtag_response['like_count']=dict()
	hashtag_response['comments_count']=dict()
	

	i=0

	for post in hashtagRecentMediaResponse['json_data']['data'] :

		
		print ("\n\n---------- POST ----------\n") 
		print ("Postid:")
		print (post['id'])

		hashtag_response['id'][i]=post['id']
			
		print ("Link to post:") 
		print (post['permalink']) 
		hashtag_response['permalink'][i]=post['permalink']
		

		print ("\nPost caption:") 
		print (post['caption']) 
		hashtag_response['caption'][i]=post['caption']
		

		print ("\nMedia type:") 
		print (post['media_type']) 
		hashtag_response['media_type'][i]=post['media_type']

		print ("\nlike_count:") 
		print (post['like_count']) 
		hashtag_response['like_count'][i]=post['like_count']

		print ("\nComments:") 
		print (post['comments_count']) 
		hashtag_response['comments_count'][i]=post['comments_count']
		
		i+=1

	req = json.dumps(hashtag_response)
	df=pd.read_json(req)
	df.to_csv(filename,index=False)



print ('\n-----------------------------------------MENU--------------------------------------------')
print ('\n1.Access Instagram account\n2.Account contents\n3.Hashtag search(PopularMedia)\n4.Hashtag Search(RecentMedia)')

choice=int(input('Enter your choice::'))



if(choice==1):
	AccessInstagramAPI()
elif(choice==2):
	AccessYourAccount()
elif(choice==3):
	getPopularMedia()
elif(choice==4):
	getRecentMedia()
else:
	print('Invalid option')


print('\n----------------------------------------------------------------------------------------------------')


