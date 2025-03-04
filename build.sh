#!/bin/bash


docker image build -f docker/production.Dockerfile . -t ghcr.io/emaddeve20/hoopoe:latest

docker push ghcr.io/emaddeve20/hoopoe:latest
