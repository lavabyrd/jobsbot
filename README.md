# Glow Worm Slack Bot

## Overview
This Slack app is built on an idea provided by Specious Stream where a user can be part of a Slack channel that can run to start the process of a GlowWorm. This is meant as a way of promoting positivity!

## Technical Overview
When a slash command is run, the app will query all the users in that channel and send out a rolling direct message from the App bot to them asking them to provide thoughts about those users. Its can then give the users a way of asking for feedback on another user. e.g. 

> Hey John, please provide your thoughts on Anna in a thread reply!

Once the threaded reply is recieved for all users, it will send the full consolidated list to Anna with what her channel mates think.

## Technical methods and technology used
This app is written in Python 3.6 and uses the Slackclient SDK to ensure ease of calling the api methods required.

For more imformation please see https://api.slack.com