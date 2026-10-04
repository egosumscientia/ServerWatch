class Server:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = "DOWN"

    def mark_up(self):
        self.status = "UP"

    def mark_down(self):
        self.status = "DOWN"

    def get_info(self) -> dict:
        return {
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "status": self.status
        }

    def toggle_status(self):
        if self.status == "DOWN":
            self.mark_up()
        elif self.status == "UP":
            self.mark_down()

    def is_up(self):
        return self.status == "UP"

    def __str__(self):
        return f"{self.hostname} ({self.ip_address}) - {self.status}"