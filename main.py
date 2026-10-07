from src.server import Server


def check(description, actual, expected):
    if actual == expected:
        print(f"PASS | {description}")
    else:
        print(f"FAIL | {description}")
        print(f"       Expected: {expected}")
        print(f"       Actual:   {actual}")


server = Server("web-01", "192.168.1.10")

# Test 1: A DOWN server must be CRITICAL.
check("DOWN server", server.evaluate_health(), "CRITICAL")

# Bring the server UP for the remaining tests.
server.mark_up()

# Test 2: All metrics HEALTHY.
server.update_metrics(20, 30, 40)

check("All healthy", server.evaluate_health(), "HEALTHY")
check("No unhealthy metrics", server.get_unhealthy_metrics(), [])
check("Unhealthy count is zero", server.count_unhealthy_metrics(), 0)
check("No unhealthy metrics detected", server.has_unhealthy_metrics(), False)

# Test 3: One WARNING metric.
server.update_metrics(75, 30, 40)

check("One warning", server.evaluate_health(), "WARNING")
check("Warning metrics", server.get_warning_metrics(), ["cpu"])
check("No critical metrics", server.get_critical_metrics(), [])
check("Unhealthy count is one", server.count_unhealthy_metrics(), 1)
check("Unhealthy metrics detected", server.has_unhealthy_metrics(), True)

# Test 4: Mixed WARNING and CRITICAL.
server.update_metrics(90, 75, 95)

check("Critical priority", server.evaluate_health(), "CRITICAL")
check("Warning metrics in mixed state", server.get_warning_metrics(), ["memory"])
check("Critical metrics in mixed state", server.get_critical_metrics(), ["cpu", "disk"])
check(
    "All unhealthy metrics",
    set(server.get_unhealthy_metrics()),
    {"cpu", "memory", "disk"},
)
check("Unhealthy count is three", server.count_unhealthy_metrics(), 3)

# Test 5: Boundary values.
for value, expected in [
    (0, "HEALTHY"),
    (69, "HEALTHY"),
    (70, "WARNING"),
    (84, "WARNING"),
    (85, "CRITICAL"),
    (100, "CRITICAL"),
]:
    check(
        f"Metric boundary {value}",
        Server.evaluate_metric_health(value),
        expected,
    )

# Test 6: Invalid health filter.
try:
    server.get_metrics_by_health("HEALTHY")
    print("FAIL | Invalid health filter")
except ValueError as error:
    check(
        "Invalid health filter",
        str(error),
        "Health must be WARNING or CRITICAL",
    )

print("\nPhase 5 tests completed.")