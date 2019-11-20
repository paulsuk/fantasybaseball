import pdb
from yahoo_oauth import OAuth2

FILENAME = 'oauth2.json'

def get_yahoo_session():
	oauth = OAuth2(None, None, from_file=FILENAME)
	if not oauth.token_is_valid():
		oauth.refresh_access_token()

	return oauth.session


if __name__ == "__main__":
	# Run this to get your auth key for the first time
	oauth = OAuth2(None, None, from_file='oauth2.json')