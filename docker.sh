#!/bin/bash
if [ -z $(whereis docker) ]
then
	echo "You haven't installed docker"
fi
if [ -z $IMAGE ]
then
	echo -n "What name is your image: "
	read IMAGE
fi
if [ -z $(docker image list | grep $IMAGE) ]
then
	docker build -t $IMAGE .
fi
if [ -z $SERVICE_NAME ]
then
	echo -n "What name is your service: "
	read SERVICE_NAME
fi
if [ -z $(docker service ls | grep $SERVICE_NAME) ]
then
	docker service create -d \
		--replicas=4 \
		--name $SERVICE_NAME \
		$IMAGE
fi
