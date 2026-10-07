import random

class Server:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = "DOWN"
        self.cpu_usage = 0
        self.memory_usage = 0
        self.disk_usage = 0

    def mark_up(self):
        self.status = "UP"

    def mark_down(self):
        self.status = "DOWN"

    def get_info(self) -> dict:
        return {
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "status": self.status,
            "cpu_usage": self.cpu_usage,
            "memory_usage": self.memory_usage,
            "disk_usage": self.disk_usage
        }

    def toggle_status(self):
        if self.status == "DOWN":
            self.mark_up()
        elif self.status == "UP":
            self.mark_down()

    def is_up(self):
        return self.status == "UP"

    def update_metrics(self, cpu_usage, memory_usage, disk_usage):
        if self.are_metrics_numeric(cpu_usage, memory_usage, disk_usage):
            if self.are_metrics_in_range(cpu_usage, memory_usage, disk_usage):
                self.cpu_usage = cpu_usage
                self.memory_usage = memory_usage
                self.disk_usage = disk_usage
            else:
                raise ValueError("Metrics must be between 0 and 100")
        else:
            raise ValueError("Metrics must be int or float")

    def simulate_metrics(self):
        self.update_metrics(random.randint(0, 100), random.randint(0, 100), random.randint(0,100))

    def evaluate_health(self):
        if not self.is_up():
            return "CRITICAL"
        metrics = [self.cpu_usage, self.memory_usage, self.disk_usage]
        has_warning = False
        for metric in metrics:
            current_metric = self.evaluate_metric_health(metric)
            if current_metric == "CRITICAL":
                return "CRITICAL"
            if current_metric == "WARNING":
                has_warning = True
        if has_warning:
            return "WARNING"
        else:
            return "HEALTHY"

    def get_unhealthy_metrics(self):
        warnings = self.get_warning_metrics()
        critical = self.get_critical_metrics()
        unhealthy_metrics = warnings + critical
        return unhealthy_metrics

    def count_unhealthy_metrics(self):
        counter = len(self.get_unhealthy_metrics())
        return counter

    def has_unhealthy_metrics(self):
        counter = self.count_unhealthy_metrics()
        return counter > 0

    def get_metrics_by_health(self, health):
        if health not in ["WARNING", "CRITICAL"]:
            raise ValueError("Health must be WARNING or CRITICAL")
        filtered_metrics = []
        metrics = {"cpu": self.cpu_usage, "memory": self.memory_usage, "disk": self.disk_usage}
        for metric, measurement in metrics.items():
            current_metric_status = self.evaluate_metric_health(measurement)
            if current_metric_status == health:
                filtered_metrics.append(metric)
        return filtered_metrics

    def get_warning_metrics(self):
        return self.get_metrics_by_health("WARNING")

    def get_critical_metrics(self):
        return self.get_metrics_by_health("CRITICAL")


    '''Static methods'''

    @staticmethod
    def are_metrics_in_range(cpu_usage, memory_usage, disk_usage):
        return (100 >= cpu_usage >= 0) and (100 >= memory_usage >= 0) and (100 >= disk_usage >= 0)

    @staticmethod
    def are_metrics_numeric(cpu_usage, memory_usage, disk_usage):
        return (isinstance(cpu_usage, (int, float)) and isinstance(memory_usage, (int, float)) and isinstance(disk_usage, (int, float))
                and not isinstance(cpu_usage,bool) and not isinstance(memory_usage, bool) and not isinstance(disk_usage, bool))

    @staticmethod
    def evaluate_metric_health(metric):
        if 0 <= metric <= 69:
            return 'HEALTHY'
        elif 70 <= metric <= 84:
            return "WARNING"
        else:
            return "CRITICAL"

    def __str__(self):
        return f"{self.hostname} ({self.ip_address}) - {self.status} | CPU: {self.cpu_usage}% | Memory: {self.memory_usage}% | Disk: {self.disk_usage}%"
