import json
from flask import Flask, request, render_template

from flumblr.app import app
from tumblr_auth.services.auth import create_oauth_session, get_tumblr_auth_url
from tumblr_auth.services.api import TumblrApi

#tumblr_api = TumblrApi(tumblr_auth)

oauth_session = create_oauth_session('http://localhost:5000/auth/user/')

def sanity_check(user_session_id):
    # Sanity check, should be 200
    print(tumblr_auth.oauth_sessions[user_session_id].get('http://api.tumblr.com/v2/user/dashboard'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')

@app.route('/auth/tumblr')
def tumblr_auth():
    tumblr_auth_dict = get_tumblr_auth_url(oauth_session)
    return json.dumps(tumblr_auth_dict)

@app.route('/auth/user/', methods=['GET'])
def user_auth():
    return render_template('session-redirect.html')

# @app.route('/oauth/user/<user_session_id>', methods=['GET'])
# def get_access_token(user_session_id):
#     print('HERE')
#     try:
#         tumblr_auth.get_access_token(user_session_id, request.url)
#         return render_template('session-redirect.html')
#     except:
#         return render_template('unauthorized.html')

@app.route('/user', methods=['GET'])
def user():
    return render_template('user.html')
#
# @app.route('/api/post', methods=['POST'])
# def post():
#     return tumblr_api.post_to_blog(request.form)
#
# @app.route('/api/get', methods=['POST'])
# def get():
#     return tumblr_api.get_blog_json(request.form)
