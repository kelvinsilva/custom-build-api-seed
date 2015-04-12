
Apache Benchmark
===============================================================


###ab -n 100 -c 10 http://localhost:5000/politics/ > benchmarks.md


This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/0.9.6
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /politics/
Document Length:        32907 bytes

Concurrency Level:      10
Time taken for tests:   26.089 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      3305500 bytes
HTML transferred:       3290700 bytes
Requests per second:    3.83 [#/sec] (mean)
Time per request:       2608.909 [ms] (mean)
Time per request:       260.891 [ms] (mean, across all concurrent requests)
Transfer rate:          123.73 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       2
Processing:   224 2484 433.6   2560    2984
Waiting:      222 2482 433.1   2555    2984
Total:        224 2484 433.5   2560    2984

Percentage of the requests served within a certain time (ms)
  50%   2560
  66%   2601
  75%   2709
  80%   2733
  90%   2804
  95%   2858
  98%   2973
  99%   2984
 100%   2984 (longest request)

