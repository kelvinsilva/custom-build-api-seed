#!/bin/bash
for i in {1..30};
do 
RANDOM_NAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
echo $RANDOM_NAME
curl -X POST -H "Content-Type: application/json" -d '{"name":"'"$RANDOM_NAME"'"}' http://localhost:5000/moneys/	
done
