import os
from agavepy.actors import get_context, get_client


def main():
   context = get_context()
   fastq_path = context['raw_message']
   print("Actor received message: {}".format(fastq_path))

   # Get an active Tapis client
   client = get_client()

   # Using our Tapis client, submit a job to Tapis App eho-fastqc-0.11.9
   body = {
      "name": "fastqc-test",
      "appId": "eho-fastqc-0.11.9",
      "archive": False,
      "inputs": {
         "fastq": "agave://eho.work.storage/{}".format(os.path.basename(fastq_path))
      }
   }
   response = client.jobs.submit(body=body)
   print("Successfully submitted job {} to Tapis App {}".format(response['id'], response['appId']))


if __name__ == '__main__':
    main()
