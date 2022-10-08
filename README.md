 Discord Bot
==============

###Usage
add a file named `setting.json` and add `{"token":"your bot token"}` in the file.
```bash
cat > setting.json << 'EOF'
{
	"token" : "your bot token"
}
EOF
```
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
