import requests

from tumblr_auth.utils.functions import validate_request_params

TUMBLR_API_USER_POST_URL = 'https://api.tumblr.com/v2/blog/{}/post'
TUMBLR_API_USER_BLOG_JSON_URL = 'https://{}.tumblr.com/api/read/json?debug=1'

class TumblrApi:
    def __init__(self, TumblrAuth):
        self.tumblr_auth = TumblrAuth

    def post_to_blog(self, data):
        if not validate_request_params(data, ['user_blog_name', 'user_session_id']):
            return 'HTTP/1.1 500\n\nInvalid request'

        user_blog_name = data['user_blog_name']
        user_session_id = data['user_session_id']
        api_url = TUMBLR_API_USER_POST_URL.format(user_blog_name)

        self.tumblr_auth.oauth_sessions[user_session_id].post(api_url, data=data)
        return 'HTTP/1.1 200 OK\n\nPosted'

    def get_blog_json(self, data):
        if not validate_request_params(data, ['user_blog_name', 'user_session_id']):
            return 'HTTP/1.1 500\n\nInvalid request'

        user_session_id = data['user_session_id']
        user_blog_name = data['user_blog_name']
        api_url = TUMBLR_API_USER_BLOG_JSON_URL.format(user_blog_name)

        response = self.tumblr_auth.oauth_sessions[user_session_id].get(api_url).text
        return 'HTTP/1.1 200 OK\n\n' + response
