from Credentials import *
import requests
import json

def getCredentials() :
	
	creds = dict()
	creds['access_token'] = ACCESS_TOKEN
	creds['client_id'] = CLIENT_ID 
	creds['client_secret'] = CLIENT_SECRET 
	creds['graph_domain'] = 'https://graph.facebook.com/' 
	creds['graph_version'] = 'v7.0' 
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' 
	creds['debug'] = 'no'
	creds['page_id'] = PAGE_ID
	creds['instagram_account_id'] = INSTAGRAM_ACCOUNT_ID 
	creds['ig_username'] = IG_USERNAME 
	print(creds)
	return creds

def callAPI( url, endpointParams, debug = 'no' ):
	data = requests.get( url, endpointParams )
	response = dict() 
	response['url'] = url 
	response['endpoint_params'] = endpointParams 
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 5) 
	response['json_data'] = json.loads( data.content ) 
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 5 ) 

	if (debug=='yes') : 
		displayData( response ) 

	return response 

def displayData( response ) :
	print ("\nURL: " )# title
	print (response['url']) # display url hit
	print ("\nEndpoint Params: ") # title
	print (response['endpoint_params_pretty']) # display params passed to the endpoint
	print ("\nResponse: ") # title
	print (response['json_data_pretty']) # make look pretty for cli