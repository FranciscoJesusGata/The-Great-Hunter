#!/bin/bash
bash config.sh
if [ $? -eq 0 ]; then
	docker build . -t hunter:1.0
	docker run -it --name great hunter:1.0
fi
