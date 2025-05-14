#!/usr/bin/env python3
# encoding: utf-8

import urllib3
import argparse

from prometheus_client import start_http_server, Gauge
from exporter import Exporter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEBUG = False

def get_argument():

    try:

        # Setup argument parser
        parser = argparse.ArgumentParser()
        parser.add_argument('-H', '--hostname',
                            type=str,
                            help='hostname or IP address and Port of PowerStore API',
                            required=True)
        parser.add_argument('-u', '--username',
                            type=str,
                            help='username',
                            required=True)
        parser.add_argument('-p', '--password',
                            type=str,
                            help='user password',
                            required=True)
        parser.add_argument('-o', '--port',
                            type=int,
                            help='exporter TCP Port',
                            required=True)
        parser.add_argument('-v', '--verbose',
                            action='store_const', const=True,
                            help='verbose logging',
                            required=False)
        parser.add_argument('-i', '--interval',
                            type=int,
                            help='polling interval',
                            required=True)
        parser.add_argument('-m', '--metric',
                            type=str,
                            help='metrics type (e.g. performance_metrics_by_appliance, space_metrics_by_appliance, performance_metrics_by_file_system...',
                            required=True)
        args = parser.parse_args()

    except KeyboardInterrupt:
        # handle keyboard interrupt #
        return 0

    global hostname, user, password, port, interval, DEBUG
    hostname = args.hostname
    user = args.username
    password = args.password
    port = args.port
    interval = args.interval
    metric = args.metric
    DEBUG = args.verbose



def main():
    """Main entry point"""

    get_argument()
    exporter = Exporter(interval, hostname, user, password, metric)
    start_http_server(port)
    exporter.run_metrics_loop()

if __name__ == "__main__":
    main()
