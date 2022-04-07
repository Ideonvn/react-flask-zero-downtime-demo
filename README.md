# Zero Downtime Demo

## Locally

```sh
# Start flask
cd web && python server
# Start react
npm start
```

## Build

```sh
# Proxy server
docker build --no-cache -t ideonvn-nginx ./nginx
# Python server with react static
docker build --no-cache -t ideonvn-web ./web
```

## Setup:

```sh
docker swarm init
```

## Monitor

```sh
watch docker stack services demo
```

## Deploy

```sh
docker stack deploy --compose-file docker-compose.yml demo
```

## Update

```sh
docker service update --force demo_web
```

## Scaling

```sh
# Scale up web instance
docker service scale demo_web=3
# Scale down web instance
docker service scale demo_web=1
```

## Cleanup

```sh
docker stack rm demo
```

