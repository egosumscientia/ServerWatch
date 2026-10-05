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
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.disk_usage = disk_usage

    def simulate_metrics(self):
        self.update_metrics(random.randint(0, 100), random.randint(0, 100), random.randint(0,100))

    def __str__(self):
        return f"{self.hostname} ({self.ip_address}) - {self.status} | CPU: {self.cpu_usage}% | Memory: {self.memory_usage}% | Disk: {self.disk_usage}%"
