# actor.py
"""Forward message from Actor inbox to Slack"""

from agavepy.actors import get_context
import requests
import os
import simplejson as json


def post_to_slack(message: str):
   """Forward string type `message` to Slack channel"""

   webhook_url = os.environ.get('SLACK_WEBHOOK')
   print("Actor sending message to Slack: {0}".format(message))

   response_from_slack = requests.post(
      webhook_url, data=json.dumps({'text': message}),
      headers={"Content-type": "application/json"})
   print("Response from Slack:")
   print(response_from_slack)


def main():
   """Main entrypoint"""
   context = get_context()
   message = context['raw_message']
   post_to_slack(message)


if __name__ == '__main__':
   main()
