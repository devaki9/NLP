from func import getCredentials, callAPI

def getLongLivedAccessToken( params ) :
	#API Endpoint:
	#	https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}
	
	endpointParams = dict() 
	endpointParams['grant_type'] = 'fb_exchange_token' 
	endpointParams['client_id'] = params['client_id'] 
	endpointParams['client_secret'] = params['client_secret'] 
	endpointParams['fb_exchange_token'] = params['access_token'] 

	url = params['endpoint_base'] + 'oauth/access_token' 

	return callAPI( url, endpointParams, params['debug'] ) 

params = getCredentials() 
params['debug'] = 'yes' 
response = getLongLivedAccessToken( params )

print ("\n ---- ACCESS TOKEN INFO ----\n") 
print ("Access Token:")  
print (response['json_data']['access_token']) 