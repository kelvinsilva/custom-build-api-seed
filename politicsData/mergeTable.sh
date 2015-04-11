#!/bin/bash


cat liberalsTableClean.txt  > politicsData.txt
tail -n+2 republicanTableClean.txt >> politicsData.txt