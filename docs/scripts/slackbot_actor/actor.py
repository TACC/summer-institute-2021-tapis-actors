"""Post user message to Slack"""
from agavepy.actors import get_context
import requests
import os
import simplejson as json


def post_slack(text):
    """Send a message containing text to Slack channel"""

    webhook_url = os.environ.get('SLACK_WEBHOOK')
    print("Actor sending message to Slack: {0}".format(text))

    payload = {
        'text': text,
        'channel': "#lsc",
        'username': "tapis_actors"
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
    post_slack(message)


if __name__ == '__main__':
    main()
