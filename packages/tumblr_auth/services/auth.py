from requests_oauthlib import OAuth1Session

from tumblr_auth.utils.functions import create_random_id
from tumblr_auth.utils.constants import TUMBLR_ACCESS_KEY, TUMBLR_SECRET_KEY

TUMBLR_OAUTH_AUTH_BASE_URL = 'http://www.tumblr.com/oauth/authorize'
TUMBLR_OAUTH_ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
TUMBLR_OAUTH_REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'

def OauthSession(object):
    pass

def create_oauth_session(user_redirect_url):
    """
    Create an oauth session that will use our Tumblr application keys and
    that will redirect users to the specified url after they authenticate
    on Tumblr.

    Returns:
        The oauth 1.0 session object
    """
    return OAuth1Session(TUMBLR_ACCESS_KEY, TUMBLR_SECRET_KEY, callback_uri=user_redirect_url)


def _get_request_token(oauth_session):
    """
    Authenticate our application with Tumblr.

    Args:
        oauth_session: OAuth1Session object

    Returns:
        The oauth session request token
    """
    return oauth_session.fetch_request_token(TUMBLR_OAUTH_REQUEST_TOKEN_URL)


def _get_tumblr_auth_url(oauth_session):
    """
    Get Tumblr authorization url. This is the Tumblr url where the user will
    grant or deny this application access to their account.

    Args:
        oauth_session: OAuth1Session object

    Returns:
        The Tumblr authorization url
    """
    return oauth_session.authorization_url(TUMBLR_OAUTH_AUTH_BASE_URL)


def get_tumblr_auth_url(oauth_session):
    """
    Get Tumblr authorization url as a dictionary.

    Args:
        oauth_session: OAuth1Session object

    Returns:
        A dictionary containing the tumblr authorization url. Ex:

        {
            "tumblr_auth_url": value
        }
    """
    request_token = _get_request_token(oauth_session)
    tumblr_auth_url = _get_tumblr_auth_url(oauth_session)
    tumblr_auth_url_dict = {
        "tumblr_auth_url": tumblr_auth_url
    }
    return tumblr_auth_url_dict
