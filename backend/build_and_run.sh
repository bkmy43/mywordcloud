#!/bin/bash

cd python-flask-server

# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
