# Phase 6 — Server Health Reporting

## Objective

Extend ServerWatch with reporting capabilities that provide a consolidated view of the health of all monitored servers.

Phase 5 introduced health evaluation for individual servers. Phase 6 will use those existing capabilities to analyze the entire server collection managed by `ServerManager`.

## Scope

### 1. Server Health Summary

Implement functionality in `ServerManager` to summarize the health of registered servers.

The summary should include:

- Total number of registered servers.
- Number of `HEALTHY` servers.
- Number of `WARNING` servers.
- Number of `CRITICAL` servers.

### 2. Filter Servers by Health

Allow servers to be retrieved according to their evaluated health status.

Supported health levels:

- `HEALTHY`
- `WARNING`
- `CRITICAL`

Filtering must reuse the existing `Server.evaluate_health()` method.

### 3. Identify Unhealthy Servers

Provide a way to retrieve servers requiring attention.

A server is considered unhealthy when its evaluated health status is either `WARNING` or `CRITICAL`.

### 4. Overall Infrastructure Health

Determine the overall health of the monitored infrastructure using the following priority:

1. `CRITICAL` — At least one server is critical.
2. `WARNING` — No server is critical, but at least one server has a warning.
3. `HEALTHY` — All registered servers are healthy.

The behavior for an empty server collection will be defined before implementation.

### 5. Reporting Output

Generate a structured report containing:

- Overall infrastructure health.
- Server counts by health level.
- Individual server information.
- Health status of each server.
- Metrics requiring attention.

The report should use standard Python data structures and remain independent of presentation formats such as JSON, HTML, or dashboards.

## Implementation Guidelines

- Extend the existing `ServerManager` class.
- Reuse the methods implemented during Phase 5.
- Avoid duplicating health evaluation logic.
- Use Python standard library functionality where appropriate.
- Keep methods focused on clear responsibilities.
- Avoid unnecessary abstractions and external dependencies.
- Preserve existing behavior from previous phases.

## Testing

Validate the implementation using servers with different combinations of health states.

Tests should cover:

- Empty server collections.
- Collections containing only healthy servers.
- Mixed healthy, warning, and critical servers.
- Servers marked as `DOWN`.
- Health filtering and server counts.
- Overall infrastructure health.
- Consistency between individual server evaluations and consolidated reports.

## Expected Outcome

By the end of Phase 6, ServerWatch should be able to evaluate and summarize the health of multiple servers, identify those requiring attention, and produce a structured infrastructure health report.

This phase establishes the foundation for future monitoring, alerting, and visualization capabilities.

## Learning Approach

Implementation will proceed incrementally.

Each step will focus on one clearly defined programming task. The learner will write the code, review its behavior, and validate the result before moving forward.

The emphasis will remain on practical Python programming, code reuse, data structures, conditional logic, and working with existing classes.