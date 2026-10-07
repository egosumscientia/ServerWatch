from src.server import Server
from src.server_manager import ServerManager


manager = ServerManager()

print("EMPTY MANAGER")
print("Count:", manager.count_servers())
print("Has servers:", manager.has_servers())

server1 = Server("web-01", "192.168.1.10")
server2 = Server("db-01", "192.168.1.20")
server3 = Server("backup-01", "192.168.1.30")

server1.mark_up()
server3.mark_up()

manager.add_server(server1)
manager.add_server(server2)
manager.add_server(server3)

print("\nAFTER ADDING")
print("Count:", manager.count_servers())
print("UP:", manager.count_servers_by_status("UP"))
print("DOWN:", manager.count_servers_by_status("DOWN"))
print("Has servers:", manager.has_servers())

print("\nINVALID STATUS")
try:
    manager.get_servers_by_status("RUNNING")
except ValueError as error:
    print(error)

print("\nAFTER CLEAR")
manager.clear_servers()
print("Count:", manager.count_servers())
print("UP:", manager.count_servers_by_status("UP"))
print("DOWN:", manager.count_servers_by_status("DOWN"))
print("Has servers:", manager.has_servers())
print("Servers:", manager.get_servers())