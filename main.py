from src.server import Server


server_1 = Server("web-01", "192.168.1.10")
server_2 = Server("db-01", "192.168.1.20")

server_1.update_metrics(20, 30, 40)
server_2.update_metrics(70, 80, 90)

print("Before invalid update:")
print(server_1)
print(server_2)

try:
    server_1.update_metrics(50, 150, 60)
except ValueError as error:
    print("\nError:", error)

print("\nAfter invalid update on server_1:")
print(server_1)
print(server_2)