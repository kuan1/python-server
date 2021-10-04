#!/bin/bash

rsync \
  mongo-docker \
  python-api \
  docker-compose.yml \
  Dockerfile \
  --exclude mongo-docker/data \
  --exclude __pycache__ \
  -av \
  huawei:/opt/python-server