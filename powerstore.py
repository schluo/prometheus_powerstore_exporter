import datetime
import json
import requests


class PowerStore:

    # This class permit to connect of the PowerStore's API

    def __init__(self, hostname, user, password, perfstats_type):
        self.hostname = hostname
        self.user = user
        self.password = password
        self.perfstats_type = perfstats_type

    def send_request_stats(self):
        # send a request and get the result as dict

        try:

            # try to get token
            url = 'https://' + self.hostname + '/api/rest/cluster?select=name,state'
            r = requests.get(url, verify=False, auth=(self.user, self.password))

            # if DEBUG:
            #    print(r, r.headers)

            # read access token from returned header
            powerstore_token = r.headers['DELL-EMC-TOKEN']

        except Exception as err:
            print(self.get_time() + ": Not able to get token: " + str(err))
            exit(1)

        try:
            # try to get stats using token
            url = 'https://' + self.hostname + '/api/rest/metrics/generate'
            r = requests.post(url, verify=False, auth=(self.user, self.password),
                              headers={"DELL-EMC-TOKEN": powerstore_token},
                              json={"entity": "performance_metrics_by_" + self.perfstats_type, "entity_id": "A1",
                                    "interval": "Five_Mins"})

            # if DEBUG:
            #    print(r, r.headers)

            # prepare return to analyse
            self.stats = json.loads(r.content)

            # if DEBUG:
            #    print(r, r.content)

        except Exception as err:
            print(self.get_time() + ": Not able to get stats: " + str(err))
            exit(1)

    def process_stats(self):

        try:
            # just take last data set
            self.last_stats = self.stats[-1]

        except Exception as err:
            print(self.get_time() + ": Error while generating result output: " + str(err))
            exit(1)

    def get_time(self):
        return datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
