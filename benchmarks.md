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


###Second test, 10 requests, 1 concurrent
 
```ab -n 10 -c1 127.0.0.1:5000/politics/ >> benchmarks.md```
 
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done

_ | _
----|-----
Server Software:    |    Werkzeug/0.9.6
Server Hostname:    |    127.0.0.1
Server Port:       |     5000
Document Path:     |     /politics/
Document Length:   |     32907 bytes
Concurrency Level:   |   1
Time taken for tests: |  3.037 seconds
Complete requests:   |   10
Failed requests:    |    0
Total transferred:  |    330550 bytes
HTML transferred:   |    329070 bytes
Requests per second: |   3.29 [#/sec] (mean)
Time per request:    |   303.665 [ms] (mean)
Time per request:   |    303.665 [ms] (mean, across all concurrent requests)
Transfer rate:      |    106.30 [Kbytes/sec] received

####Connection Times (ms)

              
      _    |   min|  mean | [+/-sd] | median |   max
-----------|------|----|-----|-------|------|------
Connect:    |    0  |  0  |  0.0  |    0    |   0
Processing:  | 183 | 303 | 171.9  |  241   |  738
Waiting:    |  182 | 303  | 171.8  |  240   |  737
Total:     |   183 | 304 | 171.9  |  241   |  739

####Percentage of the requests served within a certain time (ms)

_ | _
---|----
  50%   | 241
  66%  |  312
  75%   | 374
  80%  |  395
  90%  |  739
  95%  |  739
  98%  |  739
  99%  |  739
 100%  |  739 (longest request)
 
##Third test 1 request, 1 concurrent, baseline test
 
```ab -n 1 -c 1 http://127.0.0.1:5000/politics/ >> benchmarks.md ```

This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done

_ | _
Server Software:        Werkzeug/0.9.6
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /politics/
Document Length:        32907 bytes

Concurrency Level:      1
Time taken for tests:   9.641 seconds
Complete requests:      1
Failed requests:        0
Total transferred:      33055 bytes
HTML transferred:       32907 bytes
Requests per second:    0.10 [#/sec] (mean)
Time per request:       9640.525 [ms] (mean)
Time per request:       9640.525 [ms] (mean, across all concurrent requests)
Transfer rate:          3.35 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1    1   0.0      1       1
Processing:  9639 9639   0.0   9639    9639
Waiting:     9639 9639   0.0   9639    9639
Total:       9640 9640   0.0   9640    9640
