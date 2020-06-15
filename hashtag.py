from func import getCredentials, callAPI
import sys

def getHashtagInfo( params ) :
	#	API Endpoint:
	#	https://graph.facebook.com/{graph-api-version}/ig_hashtag_search?user_id={user-id}&q={hashtag-name}&fields={fields}
	
	endpointParams = dict()
	endpointParams['user_id'] = params['instagram_account_id'] 
	endpointParams['q'] = params['hashtag_name'] 
	endpointParams['fields'] = 'id,name' 
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + 'ig_hashtag_search' 

	return callAPI( url, endpointParams, params['debug'] ) 

def getHashtagMedia( params ) :
	#API Endpoints:
		#https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/top_media?user_id={user-id}&fields={fields}
		#https://graph.facebook.com/{graph-api-version}/{ig-hashtag-id}/recent_media?user_id={user-id}&fields={fields}
	
	endpointParams = dict() 
	endpointParams['user_id'] = params['instagram_account_id'] 
	endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink' # fields to get back
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + params['hashtag_id'] + '/' + params['type'] 

	return callAPI( url, endpointParams, params['debug'] ) 

def getRecentlySearchedHashtags( params ) :
	
	#API Endpoints:
	#	https://graph.facebook.com/{graph-api-version}/{ig-user-id}/recently_searched_hashtags?fields={fields}
	
	endpointParams = dict() 
	endpointParams['fields'] = 'id,name' 
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + params['instagram_account_id'] + '/' + 'recently_searched_hashtags' 

	return callAPI( url, endpointParams, params['debug'] ) 

try : 
	hashtag = sys.argv[1] 
except : 
	hashtag = 'sushantsinghrajput' 

params = getCredentials() 
params['hashtag_name'] = hashtag 
hashtagInfoResponse = getHashtagInfo( params ) 
params['hashtag_id'] = hashtagInfoResponse['json_data']['data'][0]['id']; 

print ("\n\n\n\t-------------------HASHTAG INFO -----------------------\n")
print ("\nHashtag: " + hashtag) # display hashtag
print ("Hashtag ID: " + params['hashtag_id']) # display hashtag id

print ("\n\n\n\t\t\t ------------------- HASHTAG TOP MEDIA --------------------\n") # section heading
params['type'] = 'top_media' 
hashtagTopMediaResponse = getHashtagMedia( params ) 

for post in hashtagTopMediaResponse['json_data']['data'] : 
	print ("\n\n---------- POST ----------\n") 
	print ("Link to post:") 
	print (post['permalink']) 
	print ("\nPost caption:") 
	print (post['caption']) 
	print ("\nMedia type:") 
	print (post['media_type']) 

print ("\n\n\n\t\t\t -------------------- HASHTAG RECENT MEDIA ----------------------\n") 
params['type'] = 'recent_media' 
hashtagRecentMediaResponse = getHashtagMedia( params ) 

for post in hashtagRecentMediaResponse['json_data']['data'] :
	print ("\n\n---------- POST ----------\n") 
	print ("Link to post:") 
	print (post['permalink']) 
	print ("\nPost caption:") 
	print (post['caption']) 
	print ("\nMedia type:") 
	print (post['media_type']) 

print ("\n\n\n\t\t\t ------------------------- USERS RECENTLY SEARCHED HASHTAGS -------------------\n") 
getRecentSearchResponse = getRecentlySearchedHashtags( params ) 

for hashtag in getRecentSearchResponse['json_data']['data'] : 
	print ("\n\n---------- SEARCHED HASHTAG ----------\n") 
	print ("\nHashtag: " + hashtag['name']) 
	print ("Hashtag ID: " + hashtag['id']) 