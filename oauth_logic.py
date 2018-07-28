import main
from flask import request

import os


def oauth_access(sc):
    # Retrieve the authentication code from the request
    auth_code = request.args['code']

    # Request the authentication tokens from Slack
    auth_response = sc.api_call(
        "oauth.access",
        client_id=main.client_id,
        client_secret=main.client_secret,
        code=auth_code
    )
    # os.environ["SO_USER_TOKEN"] = auth_response['access_token']
    os.environ[f"{auth_response['team_name']}_token"] = auth_response['bot']['bot_access_token']
    print(f"{auth_response['team_name']}_token")
    print(f"the team_id is {auth_response['team_id']}")
    print(auth_response)
    return auth_response
