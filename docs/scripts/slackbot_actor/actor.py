"""Post user message to Slack"""
import requests
import simplejson as json
from agavepy.actors import get_context

def post_slack(text, webhook_url, slack_channel, slack_username):
    """Send a message containing text to Slack channel"""

    print("Actor sending message to Slack: {0}".format(text))

    payload = {
        'text': text,
        'channel': slack_channel,
        'username': slack_username
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
    webhook_url = context['SLACK_WEBHOOK']
    slack_channel = context['SLACK_CHANNEL']
    slack_username = context['SLACK_USERNAME']
    post_slack(message, webhook_url, slack_channel, slack_username)


if __name__ == '__main__':
    main()
