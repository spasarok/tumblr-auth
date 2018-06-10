# Notes

* Can't share Oauth1Session object for multiple access token requests, doesn't redirect properly.
* Can't save user auth access string in client and send to server to construct requests because server needs to create new Oauth1Session object, and signatures do not match
```
File "/home/docker/packages/requests_oauthlib/oauth1_session.py", line 351, in _fetch_token
dev_1  |     raise TokenRequestDenied(error % (r.status_code, r.text), r)
dev_1  | requests_oauthlib.oauth1_session.TokenRequestDenied: Token request fail
```
