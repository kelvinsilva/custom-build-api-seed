#!/bin/bash

awk 'BEGIN {FS = ","; print "party%%%createdUtc%%%score%%%domain%%%title%%%author%%%ups%%%downs%%%numComments%%%permaLinks%%%thumbNail%%%urlImg" > "liberalsTableClean.txt" }   {if ($0 ~ /^[0-9].*,$/) 
							{ 
								if ($0 ~ /".*,.*"/) ; 
									else printf "Liberal%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-\n", $1, $2, $3, $5, $6, $7, $8, $9, $10, $14, $21 >> "liberalsTableClean.txt"
							}	 
						}' Liberal.csv
