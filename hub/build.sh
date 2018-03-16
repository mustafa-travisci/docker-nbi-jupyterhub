#!/usr/bin/env bash
IMAGE_NAME=nielsbohr/jupyterhub
IMAGE_VERS=devel

docker build -t $IMAGE_NAME:$IMAGE_VERS .
docker build -t $IMAGE_NAME:$IMAGE_VERS-test -f Dockerfile.test .