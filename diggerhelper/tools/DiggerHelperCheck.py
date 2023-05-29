import re
import sys

class DiggerHelperCheck:
    def __init__(self):
        self.valid_metrics = []

    def check_metric(self, metric):
        lowercase_metric = metric.lower().replace(' ', '_')
        if metric in self.valid_metrics:
            return lowercase_metric
        else:
            raise ValueError(f"Invalid metric: {metric}")

    def check_time(self, time):
        pattern = r"\d{4}-\d{2}"
        if re.match(pattern, time) or time == '*':
            return time
        else:
            raise ValueError(f"Invalid time format: {time}. Time format should be YYYY-MM.")

    def network_check(self, metric, time):
        network_metrics = []
        # 网络指标是没有时间的
        with open('diggerhelper/tools/network.csv', 'r') as file:
            for line in file:
                metrics = line.strip().split(',')
                network_metrics.extend(metrics)
        if metric in network_metrics and time != '*':
            raise ValueError(f"Network has not time.just nodes & edges.")
        

    def run(self, metric, time):
        self.valid_metrics = self.load_valid_metrics()

        try:
            checked_metric = self.check_metric(metric)
            checked_time = self.check_time(time)
            self.network_check(metric, time)
            return checked_metric, checked_time
            # print(f"Valid metric: {checked_metric}")
            # print(f"Valid time: {checked_time}")
        except ValueError as e:
            print(str(e))
            sys.exit(1)

    def load_valid_metrics(self):
        valid_metrics = []
        with open('diggerhelper/tools/metric.csv', 'r') as file:
            for line in file:
                metrics = line.strip().split(',')
                valid_metrics.extend(metrics)
        return valid_metrics

