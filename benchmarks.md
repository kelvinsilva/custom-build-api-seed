Apache Benchmark
===============================================================


##First Test, 100 requests, 10 concurrent

```ab -n 100 -c 10 http://localhost:5000/politics/ > benchmarks.md```


This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done

|_                  |                   _  |
|-------------------|----------------------|
| Server Software   |       Werkzeug/0.9.6 |
| Server Hostname   |        127.0.0.1     |
| Server Port       |            5000      |


 _               |                 _  
-----------------|--------------------
 Document Path   |        /politics/  
 Document Length |      32907 bytes   


 _        |      _         
 ------------------- | ----------------
Concurrency Level    |   10
Time taken for tests |   26.089 seconds
Complete requests   |    100
Failed requests|        0
Total transferred|     3305500 bytes
HTML transferred|      3290700 bytes
Requests per second |    3.83 [#/sec] (mean)
Time per request |       2608.909 [ms] (mean)
Time per request |       260.891 [ms] (mean, across all concurrent requests)
Transfer rate |          123.73 [Kbytes/sec] received

####Connection Times (ms)
|        _   | min | mean | [+/-]sd |median| max |
|------------|-----|------|-------|------|-------|
| Connect    |  0  |   0  |  0.2  |   0  |      2|
| Processing | 224 | 2484 | 433.6 | 2560 |  2984 |
| Waiting    | 222 | 2482 | 433.1 | 2555 |  2984 |
| Total      | 224 | 2484 | 433.5 | 2560 |  2984 |


####Percentage of the requests served within a certain time (ms)

_        |        _
-------|--------
 50%   |  2560 
  66%   |  2601 
  75%   |2709 
  80%   |2733 
  90%   |2804
  95%   |2858 
  98%   |2973 
  99%   |2984 
 100%   |2984 (longest request) 


For this test there was a lot of latency, and we saw that in the table above, 50% and above requests were served with greater than 2500 ms latency
which is too high for the user. Since all these percentages had close to 2500ms of time, we can conclude that ALL requests took a similar amount of time.
For the next two tests i wont bother going any higher because I know that we already reached an unbearable amount of load.
Also, this machine is running on a single core CPU, with 512 mb of ram, so it is not optimized for high loads

Since the program is failing at such a low number of requests it indicates to me that it has to be the low performant hardware. If we try to increase the hardware specs
and we still obtain bad results, then we can conclude that it is a software problem.
To fix this problem we need to get more CPU power 

 

##Second test, 200 requests, 1 concurrent

```ab -n 200 -c 1 127.0.0.1:5000/politics/    ```

This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)

Completed 100 requests
Completed 200 requests
Finished 200 requests

_ | _
---|----
Server Software:   |     Werkzeug/0.9.6
Server Hostname:   |     127.0.0.1
Server Port:        |    5000
Document Path:      |    /politics/
Document Length:    |    32907 bytes
Concurrency Level:   |   1
Time taken for tests:  | 47.511 seconds
Complete requests:   |   200
Failed requests:     |   0
Total transferred:  |    6611000 bytes
HTML transferred:    |   6581400 bytes
Requests per second: |   4.21 [#/sec] (mean)
Time per request:   |    237.557 [ms] (mean)
Time per request:   |    237.557 [ms] (mean, across all concurrent requests)
Transfer rate:      |    135.88 [Kbytes/sec] received

####Connection Times (ms)

      _  |      min | mean | [+/-sd] | median |  max
------------|-------|----|-------|---------|-----
Connect:    |    0 |   0 |  0.0   |   0    |   0
Processing: |  100 | 237 | 94.7  |  200  |   556
Waiting:    |  100 | 236 | 94.0  |  200   |  555
Total:     |   100 | 237 | 94.7  |  201   |  556

Percentage of the requests served within a certain time (ms)

_ | _
----|----
  50%  |  201
  66%  |  230
  75%  |  267
  80%  |  314
  90%  |  392
  95%  |  431
  98%  |  516
  99%  |  537
 100%  |  556 (longest request)
 
 
##Third test 1 request, 1 concurrent, baseline test
 
```ab -n 1 -c 1 http://127.0.0.1:5000/politics/ >> benchmarks.md ```

This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done

_ | _
---|---
Server Software:   |     Werkzeug/0.9.6
Server Hostname:    |    127.0.0.1
Server Port:       |     5000
Document Path:    |      /politics/
Document Length:   |     32907 bytes
Concurrency Level:   |   1
Time taken for tests:  | 9.641 seconds
Complete requests:   |   1
Failed requests:     |   0
Total transferred:   |   33055 bytes
HTML transferred:    |   32907 bytes
Requests per second: |   0.10 [#/sec] (mean)
Time per request:    |   9640.525 [ms] (mean)
Time per request:    |   9640.525 [ms] (mean, across all concurrent requests)
Transfer rate:       |   3.35 [Kbytes/sec] received

####Connection Times (ms)

   _        | min  |  mean | [+/-sd] | median |  max
------------|------|-------|---------|--------|------|--------
Connect:    |  1   |  1    |  0.0  |    1   |    1
Processing: | 9639 | 9639  | 0.0 |  9639  |  9639
Waiting:    | 9639 | 9639  | 0.0 |  9639  |  9639
Total:      | 9640 | 9640  | 0.0 |  9640  |  9640
