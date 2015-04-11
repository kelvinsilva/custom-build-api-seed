#!/bin/bash

awk 'BEGIN {FS = ","; print "party%%%createdUtc%%%score%%%domain%%%title%%%author%%%ups%%%downs%%%numComments%%%permaLinks%%%selfText%%%thumbNail%%%urlImg" > "republicanTableClean.txt" }   {if ($0 ~ /^[0-9].*,$/) 
							{ 
								if ($0 ~ /".*,.*"/) ; 
									else printf "Republican%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s%%%%%%%-s\n", $1, $2, $3, $5, $6, $7, $8, $9, $10, $11, $14, $21 >> "republicanTableClean.txt"
							}	 
						}' Republican.csv
