#!/bin/bash


cat liberalsTableClean.txt  > _temp.txt
tail -n+2 republicanTableClean.txt >> _temp.txt

cat _temp.txt | tr -d \' > politicsData.txt