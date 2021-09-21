# pull base image, which provides a Python3 runtime
FROM python:3.6

# install package dependencies using pip
RUN pip3 install agavepy simplejson requests

# add our custom Python script
ADD actor.py /actor.py

# command to run the python script
CMD ["python", "/actor.py"]
