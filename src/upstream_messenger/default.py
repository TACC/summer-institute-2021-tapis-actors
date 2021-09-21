import os
from agavepy.actors import get_context, get_client
import requests


def download_fastq(out_path) -> None:
   url = 'https://raw.githubusercontent.com/eho-tacc/fastqc_app/main/tests/data_R1_001.fastq'
   fq_file = requests.get(url, allow_redirects=True)
   with open(out_path, 'wb') as f:
      f.write(fq_file.content)


def main():
   """Main entry to grab message context from user input"""
   context = get_context()
   m = context['raw_message']
   print("Actor received message: {}".format(m))

   # Get an active Tapis client
   client = get_client()

   # Pull in the downstream Actor ID from the environment
   downstream_actor_id = context['DOWNSTREAM_ACTOR_ID']
   # alternatively:
   # downstream_actor_id = os.environ['DOWNSTREAM_ACTOR_ID']

   # Download our fastq file to TACC Stockyard
   out_path = '/work/06634/eho/my_reads.fastq'
   download_fastq(out_path)

   # Using our Tapis client, send the message containing file path
   # to the downstream Actor
   message = out_path
   print("Sending message '{}' to {}".format(message, downstream_actor_id))
   response = client.actors.sendMessage(actorId=downstream_actor_id, body={"message": message})
   print("Successfully triggered execution '{}' on actor '{}'".format(response['executionId'], downstream_actor_id))


if __name__ == '__main__':
    main()
