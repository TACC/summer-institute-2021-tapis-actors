"""Post user message to Slack"""
import requests
import json
from agavepy.actors import get_context

def post_slack(text, webhook_url):
    """Send a message containing text to Slack channel"""

    print("Sending message to Slack: {0}".format(text))

    payload = {
        'text': text,
        'channel': '#notifications',
        'username': 'tapis-actors'
    }

    try:
        requests.post(webhook_url,
                      data=json.dumps(payload),
                      headers={
                          "Content-type": "application/json"
                      }).content
    except Exception as ex:
        print("Exception occured", ex)


def main():
    """Main entry to grab message context from user input"""
    context = get_context()
    message = context['raw_message']
    webhook_url = context['_REACTOR_SLACK_WEBHOOK']
    post_slack(message, webhook_url)

if __name__ == '__main__':
    main()
