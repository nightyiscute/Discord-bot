 Discord Bot
==============

### Usage
Add the token of your bot to `setting.json`
or
Set `TOKEN` environment variable.
### Docker
Run the script or tyoe them yourself
```bash
./docker.sh
```
##### Make docker image
```bash
docker build -t <image name> .
```
##### Run container
```bash
docker service create -d \
--replicas=4 \
--name <name> \
<IMAGE>
```
