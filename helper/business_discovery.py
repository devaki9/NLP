from func import getCredentials, callAPI

def getAccountDetails( params ) :
	#API Endpoint:
	#	https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}
	endpointParams = dict() 
	endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){username,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' 
	endpointParams['access_token'] = params['access_token'] 

	url = params['endpoint_base'] + params['instagram_account_id'] 

	return callAPI( url, endpointParams, params['debug'] ) 

params = getCredentials() 

params['debug'] = 'no' 
response = getAccountDetails( params ) 
print ("\n---- ACCOUNT Detaisl -----\n") 
print ("username:") 
print (response['json_data']['business_discovery']['username']) 

print ("\nNumber of posts:") 
print (response['json_data']['business_discovery']['media_count']) 
print ("\nFollowers:")
print (response['json_data']['business_discovery']['followers_count'])
print ("\nFollowing:") 
print (response['json_data']['business_discovery']['follows_count']) 
print ("\nProfile picture url:") 
print (response['json_data']['business_discovery']['profile_picture_url'])
print ("\nBio:") 
print (response['json_data']['business_discovery']['biography']) 