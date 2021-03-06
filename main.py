import os
import json_format
import menu
import responses
from flask import Flask, request, json, jsonify, make_response, render_template
from slackclient import SlackClient
import os
from config import Config
import oauth_logic

# Creation of the Flask app
app = Flask(__name__)

app.config.from_object(Config)

b_token = app.config['BOT_TOKEN']
veri = app.config['VERIFICATION_TOKEN']
oauth_scope = app.config['OAUTH_SCOPE']
client_id = app.config['CLIENT_ID']
client_secret = app.config['CLIENT_SECRET']
target_channel = app.config['TARGET_JOB_CHANNEL']

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
            # sc = SlackClient(os.environ.get(
            #     f"{payload['team']['domain']}_token"))
            sc.api_call("chat.postMessage",
                        text="You can click *Post It!* to let jobbot post the job " +
                        "listing exactly as you see it. \n " +
                        "*Note:* The job listing posted by jobbot cannot " +
                        "be edited or removed. If you’d prefer the flexibility " +
                        "to tweak it later, then simply copy the text and paste it into the <#C035JE6UR|Jobs> channel \n",
                        as_user="true",
                        channel=payload['user']['id'])

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
        if payload['actions'][0]['name'] == 'cancelled_job':
            return payload["original_message"]["text"]
        elif payload['actions'][0]['name'] == 'PostJob':
            # print(f"actions payload is {json_format.pretty_json(payload)}")
            sc.api_call("chat.postMessage",
                        text=payload["original_message"]["text"],
                        as_user="true",
                        channel=target_channel)
            sc.api_call('chat.update',
                        ts=payload["message_ts"],
                        channel=payload["channel"]["id"],
                        as_user="true",
                        text=payload["original_message"]["text"],
                        attachments=responses.attachm_update)
            return ""
        else:
            return ""


# Oauth install endpoint
@app.route("/oauth_install", methods=["GET"])
def pre_install():

    # This shall be split out to a template shortly
    # return render_template("install.html",
    #                        oauth_scope=oauth_scope,
    #                        client_id=client_id
    #                        )
    return "Not available"


# Oauth finished endpoint
@app.route("/oauth_completed", methods=["GET", "POST"])
def post_install():
    auth_response = oauth_logic.oauth_access(sc)
    return f"Authed and installed to your team - {auth_response['team_name']}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host="0.0.0.0", port=port)
