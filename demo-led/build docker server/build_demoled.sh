#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DOCKER_LOCAL_NAME="cohorte/demo-led"
DOCKER_LOCAL_TAG="latest"
DOCKER_FULL_TAG="$DOCKER_LOCAL_NAME:$DOCKER_LOCAL_TAG"

cd ${DIR}/demoled

#DOCKER_REGISTRY="$1"
#DOCKER_REGISTRY_TAG="$DOCKER_REGISTRY$DOCKER_FULL_TAG"
#DOCKER_REGISTRY_LATEST_TAG="$DOCKER_REGISTRY$DOCKER_LOCAL_NAME:latest"

echo "DIR=${DIR}"
echo -e "\x1B[1;32m---- Building docker image \x1B[1;33m[$DOCKER_FULL_TAG]\x1B[1;32m...\x1B[0m"
docker build --force-rm=true --pull=true --tag="$DOCKER_FULL_TAG" -f Dockerfile "${DIR}"

echo -e "\x1B[1;32m---- Build finished.\x1B[0m"
#echo -e "\x1B[1;32m---- Pushing \x1B[1;33m[$DOCKER_REGISTRY_TAG]\x1B[1;32m and \x1B[1;33m[$DOCKER_REGISTRY_LATEST_TAG]\x1B[1;32m to registry...\x1B[0m"
#docker tag -f $DOCKER_LOCAL_TAG $DOCKER_REGISTRY_TAG
#docker tag -f $DOCKER_LOCAL_TAG $DOCKER_REGISTRY_LATEST_TAG

#docker push $DOCKER_REGISTRY_TAG
#docker push $DOCKER_REGISTRY_LATEST_TAG

#echo -e "\x1B[1;32m---- Push finished.\x1B[0m"
#echo -e "\x1B[1;32mAll finished locally.\x1B[0m"

# push to docker hub
echo -e "\x1B[1;32mPushing to Docker Hub...\x1B[0m"
docker login --username="$1" --password="$2" $3
docker push $DOCKER_FULL_TAG

#echo -e "\x1B[1;32mAll finished.\x1B[0m"

#cd centos7
#docker build --rm -t local/centos7 .
