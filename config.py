WTF_CSRF_ENABLED = True
SECRET_KEY = 'it-is-a-mystery'

OPENID_PROVIDERS = [
	{'name': 'Google', 'url':'https://www.google.com/accounts/o8/id'},
	{'name': 'Yahoo', 'url':'https://me.yahoo.com'},
	{'name': 'Flickr', 'url':'http://www.flickr.com/<username>'},
	{'name': 'MyOpenID', 'url':'https://www.myopenid.com'}]