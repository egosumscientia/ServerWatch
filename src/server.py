class Server:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        self.status = "DOWN"

    def mark_up(self):
        self.status = "UP"

    def mark_down(self):
        self.status = "DOWN"