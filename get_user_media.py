from func import getCredentials, callAPI

def getUserMedia( params, pagingUrl = '' ) :
	#	https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}

	endpointParams = dict() 
	endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username,comments,like_count' 
	endpointParams['access_token'] = params['access_token'] 

	if ( '' == pagingUrl ) : #1st page
		url = params['endpoint_base'] + params['instagram_account_id'] + '/media' 
	else : 
		url = pagingUrl  

	return callAPI( url, endpointParams, params['debug'] ) 


