# prometheus_powerstore_exporter

Prometheus Exporter for Dell EMC PowerStore Systems  

### Usage
    usage: powerstore_exporter.py [-h] -H HOSTNAME -u USERNAME -p PASSWORD -o PORT [-v] -i INTERVAL

    optional arguments:
        -h, --help                          show this help message and exit
        -H HOSTNAME, --hostname HOSTNAME    hostname or IP address and Port of PowerStore API
        -u USERNAME, --username USERNAME    username
        -p PASSWORD, --password PASSWORD    user password
        -o PORT, --port PORT                exporter TCP Port
        -v, --verbose                       verbose logging
        -i INTERVAL, --interval INTERVAL    polling interval

### Example
    python3 powerstore_exporter.py -H 172.21.16.150 -u admin -p password -o 9877 -i 5


---
  
### Copyright (c) 2022 Dell Technologies

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
