import requests
import json
import os

def post_notification(status, webhook):
    url = f'https://maker.ifttt.com/trigger/{status}/with/key/{webhook}'
    res = requests.get(url)
    return res.text

def send_notifications(status):
    subscriptions = json.load(open('files/info.json'))
    subscriptions = subscriptions['subscriptions']
    if len(subscriptions['notifications']) > 0:
        for platform in subscriptions['notifications']:
            if platform['platform'] == 'ifttt':
                print('Mobile notification update sent to user')
                for event in platform['events']:
                    if event['title'] == status and event['permission'] is True:
                        post_notification(status, platform['webhook_key'])
