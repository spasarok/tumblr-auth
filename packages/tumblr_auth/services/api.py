import requests
import sys

from tumblr_auth.utils.functions import validate_request_params
from tumblr_auth.services.auth import _create_oauth_session, TUMBLR_OAUTH_ACCESS_TOKEN_URL, TUMBLR_OAUTH_AUTH_BASE_URL

TUMBLR_API_USER_POST_URL = 'https://api.tumblr.com/v2/blog/{}/post'
TUMBLR_API_USER_BLOG_JSON_URL = 'https://{}.tumblr.com/api/read/json?debug=1'

def post_to_blog(data):
    if not validate_request_params(data, ['user_blog_name', 'user_auth_string']):
        return 'HTTP/1.1 500\n\nInvalid request'

    user_blog_name = data['user_blog_name']
    api_url = TUMBLR_API_USER_POST_URL.format(user_blog_name)

    oauth_session = _create_oauth_session()
    print(data['user_auth_string'], file=sys.stderr)

    oauth_session.authorization_url(TUMBLR_OAUTH_AUTH_BASE_URL)
    oauth_session.parse_authorization_response(data['user_auth_string'])
    oauth_session.fetch_access_token(TUMBLR_OAUTH_ACCESS_TOKEN_URL)



    print('b', file=sys.stderr)

    oauth_session.post(api_url, data=data)

    return 'HTTP/1.1 200 OK\n\nPosted'

def get_blog_json(data):
    if not validate_request_params(data, ['user_blog_name', 'user_session_id']):
        return 'HTTP/1.1 500\n\nInvalid request'

    user_session_id = data['user_session_id']
    user_blog_name = data['user_blog_name']
    api_url = TUMBLR_API_USER_BLOG_JSON_URL.format(user_blog_name)

    response = self.tumblr_auth.oauth_sessions[user_session_id].get(api_url).text
    return 'HTTP/1.1 200 OK\n\n' + response
