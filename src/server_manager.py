class ServerManager:
    def __init__(self):
        self.servers = []

    def add_server(self, server):
        if self.find_by_hostname(server.hostname) is None:
            self.servers.append(server)
        else:
            raise ValueError("Server already exists")

    def get_servers(self) -> list:
        return self.servers

    def find_by_hostname(self, hostname):
        for server in self.servers:
            if hostname == server.hostname:
                return server
        return None

    def remove_by_hostname(self, hostname):
        var_server = self.find_by_hostname(hostname)
        if var_server is None:
            raise ValueError("Server not found")
        self.servers.remove(var_server)

    def get_servers_by_status(self, status):
        if status not in ["UP", "DOWN"]:
            raise ValueError("Status must be UP or DOWN")
        filtered_servers = []
        for server in self.servers:
            if server.status == status:
                filtered_servers.append(server)
        return filtered_servers

    def get_up_servers(self):
        return self.get_servers_by_status("UP")

    def get_down_servers(self):
        return self.get_servers_by_status("DOWN")

    def count_servers(self):
        return len(self.servers)

    def count_servers_by_status(self, status):
        return len(self.get_servers_by_status(status))

    def has_servers(self):
        current_servers = self.count_servers()
        return current_servers > 0

    def clear_servers(self):
        self.servers.clear()


