import os
import json_format
import menu
import responses
from flask import Flask, request, json, jsonify, make_response, render_template
from slackclient import SlackClient
from config import Config

# Creation of the Flask app
app = Flask(__name__)

app.config.from_object(Config)

b_token = app.config['BOT_TOKEN']
u_token = app.config['USER_TOKEN']
veri = app.config['VERIFICATION_TOKEN']
oauth_scope = app.config['OAUTH_SCOPE']
client_id = app.config['CLIENT_ID']
client_secret = app.config['CLIENT_SECRET']

# Global reference for the Slack Client tokens
sc = SlackClient(b_token)


@app.route("/")
def index():
    return render_template('index.html')


# Endpoint for the slash command
@app.route("/job", methods=["POST"])
def job_post():
    payload = request.form.to_dict()
    # remove this to debug the payload
    # print(json_format.pretty_json(payload))

    # uncomment the below for debugging
    # print(payload['trigger_id'])
    sc.api_call('dialog.open', dialog=menu.job_menu,
                trigger_id=payload['trigger_id'])
    return make_response("", 200)


@app.route("/actions", methods=["POST"])
def action_route():
    payload = json.loads(request.form.get("payload"))
    # print(f"actions payload is {json_format.pretty_json(payload)}")
    if payload['callback_id'] == "job_post":
        if payload['type'] != 'dialog_cancellation':
            sc.api_call('chat.postMessage',
                        channel=payload['user']['id'],
                        text=responses.make_response(
                            payload["submission"]["contract_type"],
                            payload["submission"]["city"],
                            payload["submission"]["job_title"],
                            payload["submission"]["salary"],
                            payload["submission"]["info"],
                            payload["user"]["id"]
                        ),
                        attachments=responses.attachm,
                        as_user="true")
            return ""
        else:
            return make_response("", 200)
    elif payload['callback_id'] == 'confirm_post':
        # print(f"actions payload is {json_format.pretty_json(payload)}")
        if payload['team']['domain'] == "mgpreston":
            post_channel = "CBUAKB622"
        elif payload['team']['domain'] == "mpreston-owner":
            post_channel = "CBYPV45FF"
        elif payload['team']['domain'] == "irishtechcommunity":
            post_channel = "C035JE6UR"
        else:
            print(f"team {payload['team']['domain']} is not known")
        try:
            sc.api_call("chat.postMessage",
                        text=payload["original_message"]["text"],
                        as_user="true",
                        # channel="CBUAKB622")
                        channel=post_channel)
            sc.api_call('chat.update',
                        ts=payload["message_ts"],
                        channel=payload["channel"]["id"],
                        as_user="true",
                        attachments=responses.attachm_update)
            return ""
        except UnboundLocalError:
            print(f"error was encountered")
            print(f"{payload['team']['domain']} not recognised")
            return "error, team not recognised, please contact markgpreston@gmail.com"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host="0.0.0.0", port=port)
