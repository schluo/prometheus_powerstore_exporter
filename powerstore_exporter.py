#!/usr/bin/env python3
# encoding: utf-8


import os
import time
import urllib3
from powerstore import PowerStore

from prometheus_client import start_http_server, Gauge

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEBUG = True


class Exporter:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    powerstore metrics into Prometheus metrics.
    """

    def __init__(self, polling_interval_seconds=5):

        self.polling_interval_seconds = polling_interval_seconds
        # Prometheus metrics to collect

        powerstore_hostname = str(os.getenv("POWERSTORE_HOSTNAME", "172.21.16.150"))
        powerstore_user = str(os.getenv("POWERSTORE_USER", "admin"))
        powerstore_password = str(os.getenv("POWERSTORE_PASSWORD", "Noah2407!"))
        powerstore_perfstats_type = str(os.getenv("POWERSTORE_PERF_TYPE", "appliance"))

        self.powerstore = PowerStore(hostname=powerstore_hostname,
                                     user=powerstore_user,
                                     password=powerstore_password,
                                     perfstats_type=powerstore_perfstats_type)
        self.powerstore.send_request_stats()
        self.powerstore.process_stats()

        self.values = []
        for perf_key, perf_value in self.powerstore.last_stats.items():
            self.values.append(Gauge(perf_key, perf_key))

    def get_metrics_index(self, metric_name):
        i = 0
        for metric in self.values:
            if metric._name == metric_name:
                return i
            i += 1

    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.powerstore.send_request_stats()
            self.powerstore.process_stats()
            for perf_key, perf_value in self.powerstore.last_stats.items():
                try:
                    print(perf_key, perf_value)
                    self.values[self.get_metrics_index(perf_key)].set(perf_value)
                except:
                    self.values[self.get_metrics_index(perf_key)].set(-1)
            time.sleep(self.polling_interval_seconds)

def main():
    """Main entry point"""

    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "5"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))
    exporter = Exporter(polling_interval_seconds=polling_interval_seconds)

    start_http_server(exporter_port)
    exporter.run_metrics_loop()

if __name__ == "__main__":
    main()
