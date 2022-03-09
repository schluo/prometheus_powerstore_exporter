import time

import urllib3
from prometheus_client import Gauge

from powerstore import PowerStore

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Exporter:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    powerstore metrics into Prometheus metrics.
    """

    def __init__(self, polling_interval, hostname, user, password):

        self.polling_interval = polling_interval

        self.powerstore = PowerStore(hostname=hostname,
                                     user=user,
                                     password=password,
                                     perfstats_type="appliance")

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
            time.sleep(self.polling_interval)
