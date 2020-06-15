import pandas as pd
from get_user_media import getUserMedia
import os,json
from func import getCredentials


params=getCredentials()
params['debug'] = 'no'
response = getUserMedia(params)


response_json=dict()
i=0
response_json['id']=dict()
response_json['permalink']=dict()
response_json['caption']=dict()
response_json['media_type']=dict()
response_json['timestamp']=dict()
response_json['comments']=dict()
response_json['like_count']=dict()


response_json['comments']=dict()

for post in response['json_data']['data'] :
	print ("\n\n---------- POST ----------\n") 
	print ("\nPost_id:")
	print (post['id'])

	response_json['id'][i]=post['id']

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

