 Discord Bot
==============

###Usage
add the token of your bot to `setting.json`
###Docker
Run the script or tyoe them yourself
```bash
./docker.sh
```
#####Make docker image
```bash
docker build -t <image name> .
```
#####Run container
```bash
docker service create -d \
--replicas=4 \
--name <name> \
<IMAGE>
```
