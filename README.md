# Running JupyterHub  in docker

This is a simple example of running jupyterhub in a docker container.

This example will:

- create a docker network
- run jupyterhub in a container
- enable 'dummy authenticator' for testing
- run users in their own containers
- mount a volume name jupyterhub-user-username for each user

It does not:

- run the proxy in its own container

## to skip building the images

    cd jupyterhub_basics/examples/simple
    docker-compose pull notebook
    docker-compose pull jupyterhub

## to build the images

    docker-compose build notebook
    docker-compose build jupyterhub

## to start the hub

### using docker run

    docker network create net_basic
    docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock --net net_basic \
        --name jupyterhub_basic -p8082:8000 phaustin/newhub:step1


### using  docker-compose run

    docker-compose up

### to start a notebook

* open your browser at localhost:8082

* log in with anyname/anypassword

## to remove network and docker processes

     ./bringdown.sh

Original source:  https://github.com/jupyterhub/dockerspawner/tree/master/examples/simple


