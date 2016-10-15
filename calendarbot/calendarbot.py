import os
import yaml
from slackclient import SlackClient


BOT_NAME = 'calendarbot'

with open('api_keys.yml') as txt:
    key = yaml.load(txt)
key = key['slack_key']

slack_client = SlackClient('key')

if __name__ == '__main__':
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for " + user['name'] + " is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)
