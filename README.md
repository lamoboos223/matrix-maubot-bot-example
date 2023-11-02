# run synapse instance on docker
```sh
docker run -it --rm \
    --mount type=volume,src=synapse-data,dst=/data \
    -e SYNAPSE_SERVER_NAME=my.matrix.host \
    -e SYNAPSE_REPORT_STATS=yes \
    matrixdotorg/synapse:latest generate

docker run -d --name synapse \
    --mount type=volume,src=synapse-data,dst=/data \
    -p 8008:8008 \
    matrixdotorg/synapse:latest
```

# Generating an (admin) user also create another user for the (bot)
`docker exec -it synapse register_new_matrix_user http://localhost:8008 -c /data/homeserver.yaml`
# generate matrix access token
```sh
curl --location 'http://localhost:8008/_matrix/client/r0/login' \
--header 'Content-Type: application/json' \
--data '{
    "type": "m.login.password",
    "user": "bot",
    "password": "bot"
}'
```

# run muabot on docker
```
mkdir maubot-server
cd maubot-server
docker run --rm -v $PWD:/data:z dock.mau.dev/maubot/maubot
```
> update the config.yaml file, add the user admin and password 'admin' to the admins directive.
> update the homeservers.matrix.org.url directive to synapse container ip http://<container-ip>:8008
```sh
sed -i 's/matrix.org/matrix.lab-lama.com/g' config.yaml
sed -i "s#url: ''#url: 'http://localhost:8008'#g" config.yaml
sed -i "/admins:/a \ \ admin: 'admin'" config.yaml
docker run --restart unless-stopped -p 29316:29316 -v $PWD:/data:z dock.mau.dev/maubot/maubot:<version>
```
> login 
> http://localhost:29316/_matrix/maubot
> username: admin
> password: admin

### go inside the muabot container to build the bot using the mbc command
```sh
cd /opt
wget https://github.com/lamoboos223/matrix-maubot-bot-example/archive/refs/heads/master.zip
unzip master.zip -o webhook-bot
cd webhook-bot
mbc build webhook
```
# go outside the maubot container to copy the generated .mbp file
docker cp <container-id>:/opt/*.mbp .
```




---
## Build muabot from source code
```sh
git clone git@github.com:maubot/maubot.git
cd maubot
pip install --upgrade maubot
python3 -m maubot
# http://localhost:29316/_matrix/maubot
```


