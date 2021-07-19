# python-concurrency-aiohttp

# Results

## Server info

| Components | Vendor | Model |
| ---------- | ------ | ----- | 
| Motherboard | Gigabyte Technology | AB350M-DS3H V2 |
| CPU | AMD | Ryzen 7 3700X |
| Memory | Goodram | GR2666D464L19/16G x 4 |


## CPU bound tests

| Test name | 3.5 | 3.6 | 3.7 | 3.8 | 3.9 | 3.10-rc |
| --------- | --- | --- | --- | --- | --- | ------- |
| cpu_bound_test.py | 8.801 | 8.923 | 8.275 | 8.671 | 8.741 | 7.451 |
| cpu_bound_test_with_threading.py | 9.068 | 9.035 | 8.569 | 8.951 | 8.379** | 7.500 | 
| cpu_bound_test_with_multiprocessing.py | **4.638** | **4.645** | **4.431** | **4.628** | **4.279** | **4.020** | 


## IO bound tests

### io_bound_test_with_async.py				

| version/urls |  1  |  10 | 100 | 500 | 1000 |
| ------------ | --- | --- | --- | --- | ---- |
| 3.5 | 1.003 | 1.006 | 3.037 | 11.180 | 11.344 |
| 3.6 | 1.003 | 1.005 | 3.033 | 11.163 | 14.312 |
| 3.7 | 1.002 | 1.005 | 3.032 | 11.156 | 12.300 |
| 3.8 | 1.003 | 1.006 | 3.031 | 11.154 | 11.291 |
| 3.9 | 1.003 | 1.005 | 3.030 | 11.151 | 15.296 |
| 3.10-rc | 1.003 | 1.006 | 3.031 | 11.153 | 11.275 | 
| **avg** |  **1.003** | **1.006** | **3.032** | **11.160** | **12.636** |


### io_bound_test_with_multiprocessing.py	

| version/urls |  1  |  10 | 100 | 500 | 1000 |
| ------------ | --- | --- | --- | --- | ---- |
| 3.5 | 1.019 | 1.018 | 7.039 | 32.115 | 63.224 |
| 3.6 | 1.019 | 1.020 | 7.039 | 32.114 | 63.250 |
| 3.7 | 1.032 | 1.020 | 7.037 | 32.124 | 63.243 |
| 3.8 | 1.033 | 1.019 | 7.038 | 32.122 | 63.222 |
| 3.9 | 1.027 | 1.014 | 7.027 | 32.104 | 63.210 |
| 3.10-rc | 1.028 | 1.015 | 7.027 | 32.105 | 63.206 |
| **avg** | **1.026** | **1.018** | **7.034** | **32.114** | **63.226** |


### io_bound_test_with_threading.py

| version/urls |  1  |  10 | 100 | 500 | 1000 |
| ------------ | --- | --- | --- | --- | ---- |
| 3.5 | 1.004 | 1.012 | 3.010 | 11.022 | 21.048 |
| 3.6 | 1.005 | 1.012 | 3.009 | 11.026 | 21.055 |
| 3.7 | 1.006 | 1.011 | 3.008 | 11.024 | 21.056 |
| 3.8 | 1.006 | 1.011 | 5.058 | 25.168 | 50.287 |
| 3.9 | 1.005 | 1.010 | 5.050 | 25.163 | 50.288 |
| 3.10-rc | 1.004 | 1.010 | 5.042 | 25.166 | 50.227 |
| **avg** | **1.005** | **1.011** | **4.030** | **18.095** | **35.660** |


## How to use

```shell
$ podman run -v $(pwd):/tmp --security-opt label=disable --rm python:3.5 bash /tmp/bin/run.sh
$ podman run -v $(pwd):/tmp --security-opt label=disable --rm python:3.6 bash /tmp/bin/run.sh
$ podman run -v $(pwd):/tmp --security-opt label=disable --rm python:3.7 bash /tmp/bin/run.sh
$ podman run -v $(pwd):/tmp --security-opt label=disable --rm python:3.8 bash /tmp/bin/run.sh
$ podman run -v $(pwd):/tmp --security-opt label=disable --rm python:3.9 bash /tmp/bin/run.sh
$ podman run -v $(pwd):/tmp --security-opt label=disable --rm python:3.10-rc bash /tmp/bin/run.sh
```

## HTTP Server

### Build HTTP server

```shell
$ cargo build --release
```

### Run HTTP server

```shell
$ ROCKET_PORT=9991 ./target/release/http_server
$ ROCKET_PORT=9992 ./target/release/http_server
$ ROCKET_PORT=9993 ./target/release/http_server
```

### Nginx Config
```
http {
    upstream io_bound {
        server 127.0.0.1:9991;
        server 127.0.0.1:9992;
        server 127.0.0.1:9993;
    }

    server {
        listen 9999;

        location / {
            proxy_pass http://io_bound;
        }
    }
}
```