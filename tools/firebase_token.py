import argparse
import requests

import firebase_admin
from firebase_admin import credentials, auth

DATABASE_URL = "https://dar-app-73e19.firebaseio.com/"
PATH_TO_PRIVATE_KEY = "keys/firebase.json"
API_KEY = "AIzaSyCiVwCG07qkl6wHS61QFLlXwKPyaXmUgNw"

cred = credentials.Certificate(PATH_TO_PRIVATE_KEY)
default_app = firebase_admin.initialize_app(cred, {"databaseURL": DATABASE_URL})

def get_token(uid):
    token = auth.create_custom_token(uid).decode()
    data = {
        'token': token,
        'returnSecureToken': True
    }
    url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty" \
        "/verifyCustomToken?key={}".format(API_KEY)
    
    response = requests.post(url, json=data)
    return response.json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Firebase ID token from a user id (UID).")
    parser.add_argument("uid", help="Firebase User ID (UID)", type=str)
    args = parser.parse_args()

    print(get_token(args.uid)["idToken"])
