# pull base image
FROM python:3.6

# install requirements
RUN pip3 install agavepy simplejson requests

# add the python script to docker container
ADD actor.py /actor.py

# command to run the python script
CMD ["python", "/actor.py"]
