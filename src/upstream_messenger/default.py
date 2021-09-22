import os
from agavepy.actors import get_context, get_client
import requests


def main():
   """Main entrypoint"""
   context = get_context()
   m = context['raw_message']
   print("Actor received message: {}".format(m))

   # Get an active Tapis client
   client = get_client()

   # Pull in the downstream Actor ID from the environment
   downstream_actor_id = context['DOWNSTREAM_ACTOR_ID']
   # alternatively:
   # downstream_actor_id = os.environ['DOWNSTREAM_ACTOR_ID']

   # Using our Tapis client,
   # upload our fastq file to TACC Stockyard using
   url = "https://raw.githubusercontent.com/eho-tacc/fastqc_app/main/tests/data_R1_001.fastq"
   systemId = 'eho.work.storage'
   files_resp = client.files.importData(
      fileName='example.fastq',
      filePath='/', # fileToUpload=None,
      systemId=systemId, urlToIngest=url)
   print(files_resp)

   # Using our Tapis client, send the message containing file path
   # to the downstream Actor
   message = "agave://{}/{}".format(systemId, files_resp['path'])
   print("Sending message '{}' to {}".format(message, downstream_actor_id))
   response = client.actors.sendMessage(actorId=downstream_actor_id, body={"message": message})
   print("Successfully triggered execution '{}' on actor '{}'".format(response['executionId'], downstream_actor_id))


if __name__ == '__main__':
    main()