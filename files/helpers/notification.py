import requests
import json
import os

def post_notification(status):
    url = f'https://maker.ifttt.com/trigger/{status}/with/key/nI5r3MpBjShaTXZb4wOssnap8DMMk3B0i_PWDrwoCxw'
    res = requests.get(url)
    return res.text

def send_notifications(status):
    subscriptions = json.load(open('helpers/info.json'))
    subscriptions = subscriptions['subscriptions']
    if len(subscriptions['notifications']) > 0:
        for platform in subscriptions['notifications']:
            if platform['platform'] == 'ifttt':
                print('Mobile notification update sent to user')
                post_notification(status)