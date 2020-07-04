from func import getCredentials, callAPI

def getUserPages( params ) :
	#API Endpoint:
	#	https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}
	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['access_token'] = params['access_token'] 
	url = params['endpoint_base'] + 'me/accounts' 
	return callAPI( url, endpointParams, params['debug'] ) 

params = getCredentials() 
params['debug'] = 'no' 
response = getUserPages( params ) 

print ("\n---- FACEBOOK PAGE DETAILS ----\n") 
print ("Page Name:") 
print (response['json_data']['data'][0]['name']) 
print ("\nPage Category:") 
print (response['json_data']['data'][0]['category']) 
print ("\nPage Id:")
print (response['json_data']['data'][0]['id']) 