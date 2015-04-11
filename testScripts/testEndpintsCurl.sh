#!/bin/bash

echo "Testing GET******************"
curl -X GET http://localhost:5000/moneys/
     
echo "Testing DELETE***************"
curl -X DELETE http://localhost:5000/moneys/3
     
echo "Testing PUT******************"
curl -X PUT -H "Content-Type: application/json" -d '{"name":"money for car"}' http://localhost:5000/moneys/1
     
echo "Testing POST*****************"
curl -X POST -H "Content-Type: application/json" -d '{"name":"money for girl"}' http://localhost:5000/moneys/


