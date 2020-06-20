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
	endpointParams['fields'] = 'id,children,caption,comments_count,like_count,media_type,media_url,permalink' # fields to get back
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

