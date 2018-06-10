import json
from flask import Flask, request, render_template

from flumblr.app import app
from tumblr_auth.services.auth import get_tumblr_auth_url
from tumblr_auth.services.api import post_to_blog, get_blog_json

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html')


@app.route('/auth/tumblr')
def tumblr_auth():
    tumblr_auth_dict = get_tumblr_auth_url('http://{}/auth/user/'.format(request.host))
    return json.dumps(tumblr_auth_dict)


@app.route('/auth/user/', methods=['GET'])
def user_auth():
    return render_template('session-redirect.html')


@app.route('/user', methods=['GET'])
def user():
    return render_template('user.html')


@app.route('/api/post', methods=['POST'])
def post():
    return post_to_blog(request.form)


@app.route('/api/get', methods=['POST'])
def get():
    return get_blog_json(request.form)
