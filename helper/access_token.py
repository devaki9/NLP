from func import getCredentials,callAPI

def AccessToken(params) :
	#API Endpoint:
		#https://graph.facebook.com/debug_token?input_token={input-token}&access_token={valid-access-token}
	endpointParams = dict() 
	endpointParams['input_token'] = params['access_token'] 
	endpointParams['access_token'] = params['access_token'] 
	url = params['graph_domain'] + '/debug_token' 
	return callAPI( url, endpointParams, params['debug'] ) 
