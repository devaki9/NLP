from func import getCredentials, callAPI

def getInstagramAccount( params ) :
	#API Endpoint:
		#https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account
	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['access_token'] = params['access_token'] 
	endpointParams['fields'] = 'instagram_business_account' 

	url = params['endpoint_base'] + params['page_id'] 

	return callAPI( url, endpointParams, params['debug'] ) 

params = getCredentials() 
params['debug'] = 'no' 
response = getInstagramAccount( params ) 

print ("\n----- INSTAGRAM ACCOUNT INFO ----\n")
print ("Page Id:") 
print (response['json_data']['id']) 
print ("\nInstagram Business Account Id:")
print (response['json_data']['instagram_business_account']['id']) 
