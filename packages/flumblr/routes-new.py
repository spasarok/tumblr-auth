from flask import Flask, request, render_template

from flumblr.app import app
from tumblr_auth.services.auth import TumblrAuth
from tumblr_auth.services.api import TumblrApi

tumblr_auth = TumblrAuth()
tumblr_api = TumblrApi(tumblr_auth)

def sanity_check(user_session_id):
    # Sanity check, should be 200
    print(tumblr_auth.oauth_sessions[user_session_id].get('http://api.tumblr.com/v2/user/dashboard'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')

@app.route('/oauth/auth_url')
def get_auth_url():
    user_session_id = tumblr_auth.create_oauth_session('http://' + request.host + '/oauth/user/')
    tumblr_auth.get_request_token(user_session_id)
    return 'HTTP/1.1 200 OK\n\n' + tumblr_auth.get_user_auth_url(user_session_id)

@app.route('/oauth/user/<user_session_id>', methods=['GET'])
def get_access_token(user_session_id):
    print('HERE')
    try:
        tumblr_auth.get_access_token(user_session_id, request.url)
        return render_template('session-redirect.html')
    except:
        return render_template('unauthorized.html')

@app.route('/user', methods=['GET'])
def user():
    return render_template('user.html')

@app.route('/api/post', methods=['POST'])
def post():
    return tumblr_api.post_to_blog(request.form)

@app.route('/api/get', methods=['POST'])
def get():
    return tumblr_api.get_blog_json(request.form)
