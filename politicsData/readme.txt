This directory is used to manipulate and clean the csv files. 
Liberals.csv and Republicans.csv are cleaned using parseRepublicans.sh and parseLiberals.sh shell scripts.
The shell scrips will make a file called liberalsTableClean.txt or republicanTableClean.txt which are delimited with three percent signs.

The fields for these are: party, createdUtc, score, domain, title, author, ups, downs, numComments, permaLinks, selfText, thumbNail, urlImg

The process to go from a csv unclean file to generated curl requests are as follows:

1. Parse Liberal (or republican) csv file, and obtain only columns wanted, make sure to only grab a field if it is delimited by a comma, if a field has quotations in it, then treat it as a whole field regardless of delimiter, to the end of the quotation. Insert the fields into the csv file such that each field is delimited by three percent signs "%%%". Ideally you would create 2 files, one for republicans and one for liberals. You would also need to add a field, preferable the first column which denotes which party each post is from, using awk. 

(step 1 are files parseLiberals.sh, and parseRepublicans.sh), which outputs liberalsTableClean.txt and republicansTableClean.txt

1.5 Merge the liberal and republicans csv files into one single file. This will consist of our table. (mergeTable.sh, which outputs poiticsData.txt)  

2. From step 1.5, clean the file such that all quotation marks and single quotations are deleeted (mergeTable.sh, also politicsData.txt)

3. From step 2, generate curl requests using awk. (generateCurlRequests.sh, which generated dataQueries.sh)
