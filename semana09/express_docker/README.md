# Docker

## Comandos

### Docker build

```bash
# docker build -t {image_name} .
# -t => Tag
docker build -t express_docker .
```

### Run (Docker)

```bash
# docker run -p {container_port}:{host_port} {image_name}
# -p => Map container port to host port
# -d => Daemon mode (En segundo plano)
docker run -p 5000:3000 express_docker
```

### Show Executing Containers 

```bash
docker ps
```

### Show All Containers

```bash
docker ps -a
```

### Stop Container

```bash
docket stop {id_container}
```

### Remove Container

```bash
docker rm {id_container}
```

### Remove All Containers (Warning)

```bash
docker rm -f $(docker ps -a -q)
```

### Show Images

```bash
docker images
```

### Remove Images

```bash
docker rmi {image_name}
```

### Remove All Images (Warning)
```bash
docker rmi $(docker images -q)
```

### Show Container Logs

```bash
docker logs {id_container}
```