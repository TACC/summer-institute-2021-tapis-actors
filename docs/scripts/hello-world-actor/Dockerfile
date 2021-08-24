# pull base image
FROM python:3.6

# add requirements.txt to docker container
ADD requirements.txt /requirements.txt

# install requirements.txt
RUN pip3 install -r /requirements.txt

# add the python script to docker container
ADD actor.py /actor.py

# command to run the python script
CMD ["python", "/actor.py"]
