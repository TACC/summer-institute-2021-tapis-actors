import os
from agavepy.actors import get_context, get_client


def main():
   context = get_context()
   fastq_uri = context['raw_message']
   print("Actor received message: {}".format(fastq_uri))

   # Usually, one would perform some input validation before submitting
   # a job to a Tapis App. Here, we simply validate that the path looks
   # like a Tapis/Agave URI
   assert fastq_uri.startswith('agave://')

   # Get an active Tapis client
   client = get_client()

   # Using our Tapis client, submit a job to Tapis App eho-fastqc-0.11.9
   body = {
      "name": "fastqc-test",
      "appId": "eho-fastqc-0.11.9",
      "archive": False,
      "inputs": {
         "fastq": "agave://eho.work.storage/{}".format(os.path.basename(fastq_uri))
      }
   }
   response = client.jobs.submit(body=body)
   print("Successfully submitted job {} to Tapis App {}".format(response['id'], response['appId']))


if __name__ == '__main__':
    main()

