from requests_oauthlib import OAuth1Session

from tumblr_auth.utils.functions import create_random_id
from tumblr_auth.utils.constants import TUMBLR_ACCESS_KEY, TUMBLR_SECRET_KEY

TUMBLR_OAUTH_AUTH_BASE_URL = 'http://www.tumblr.com/oauth/authorize'
TUMBLR_OAUTH_ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
TUMBLR_OAUTH_REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'

class TumblrAuth:

    oauth_sessions = {}

    def create_oauth_session(self, user_redirect_url_base):
        user_session_id = create_random_id(12)
        user_redirect_url = user_redirect_url_base + user_session_id
        self.oauth_sessions[user_session_id] = OAuth1Session(TUMBLR_ACCESS_KEY, TUMBLR_SECRET_KEY, callback_uri=user_redirect_url)
        return user_session_id

    def get_request_token(self, user_session_id):
        return self.oauth_sessions[user_session_id].fetch_request_token(TUMBLR_OAUTH_REQUEST_TOKEN_URL)

    def get_user_auth_url(self, user_session_id):
        auth_url = self.oauth_sessions[user_session_id].authorization_url(TUMBLR_OAUTH_AUTH_BASE_URL)
        return auth_url

    def get_access_token(self, user_session_id, user_redirect_url_with_auth):
        self.oauth_sessions[user_session_id].parse_auth_response(user_redirect_url_with_auth)
        self.oauth_sessions[user_session_id].fetch_access_token(TUMBLR_OAUTH_ACCESS_TOKEN_URL)
