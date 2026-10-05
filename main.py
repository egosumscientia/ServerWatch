from src.server import Server


server = Server("web-01", "192.168.1.10")

server.simulate_metrics()
print(server)

server.mark_up()
print(server)

server.mark_down()
print(server)

print(server.get_info())