#!/bin/bash
if [ ! -f apilib/ ]; then
	git submodule init
	git submodule update
fi
touch apilib/__init__.py
pip3 install -q -r apilib/requirements.txt
if [ $? -ne 0 ]; then
	exit $?
fi
if [ ! -f apilib/config.yml ]; then
	echo "Api credentials not set."
	echo "Before continue go to your API apps page on the intra and copy the uid and secret."
	echo "Note: the secrets expires eventually and you have to change it on your credentials by hand;"
	echo "to edit the credentials, go to apilib folder and edit config.yml file."
	echo -n "Insert your app UID: "
	read uid
	echo -n "Insert your app Secret: "
	read secret
	cat << EOF > apilib/config.yml
---
  intra:
    client: "$uid" #UID
    secret: "$secret" #Secret
    uri: "https://api.intra.42.fr/v2/oauth/token"
    endpoint: "https://api.intra.42.fr/v2"
    scopes: ""

EOF
fi
echo "Running script..."
exec python3 main.py
