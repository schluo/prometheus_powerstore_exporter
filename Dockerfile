# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# CMD [ "python3", "powerstore_exporter.py","-H ${ARRAY}","-u ${USER}","-p ${PASSWORD}","-o $PORT","-i ${INTERVAL}", "&"]

CMD sh -c "python3 powerstore_exporter.py -H \"$ARRAY\" -u \"$USER\" -p \"$PASSWORD\" -o \"$PORT\" -i \"$INTERVAL\"" 
