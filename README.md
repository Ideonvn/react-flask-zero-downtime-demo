# Zero Downtime Demo

## Locally

```sh
# Setup env
python3 -m venv .venv
source .venv/bin/activate
pip install -r web/requirements.txt
# Start database
npm run database
# Start backend
npm run backend
# Start frontend
npm run frontend
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

