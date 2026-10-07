# Phase 5 — Server Health Evaluation

## Objective

Add the ability to evaluate the health of a server using the information already available in the `Server` object.

At this point, ServerWatch can:

- represent individual servers;
- manage `UP` and `DOWN` operational states;
- store CPU, memory, and disk metrics;
- validate metrics;
- manage multiple servers through `ServerManager`.

Phase 5 will begin interpreting this information to determine whether a server is operating normally or experiencing a problematic condition.

The implementation will remain progressive and focused primarily on Python logic.

---

## Initial State

Each `Server` object currently contains:

- `hostname`;
- `ip_address`;
- `status`;
- `cpu_usage`;
- `memory_usage`;
- `disk_usage`.

The current operational states are:

- `UP`;
- `DOWN`.

Metrics represent percentages and accept numeric values between `0` and `100`, inclusive.

`ServerManager` is responsible for managing a collection of `Server` objects.

---

## Functional Objective

During this phase, ServerWatch will progressively introduce the concept of **server health**.

The health states to be considered are:

- `HEALTHY`;
- `WARNING`;
- `CRITICAL`.

Health states are different from the operational `UP`/`DOWN` state.

For example:

- `UP` indicates that the server is available according to the current model;
- `HEALTHY`, `WARNING`, and `CRITICAL` describe the condition of the server according to health evaluation rules.

The exact relationship between availability, metrics, and health will be decided progressively before implementation.

---

## Topics to Develop Progressively

This phase will work through problems such as:

1. Define what makes a server `HEALTHY`.
2. Define which conditions produce `WARNING`.
3. Define which conditions produce `CRITICAL`.
4. Establish thresholds for CPU, memory, and disk usage.
5. Evaluate multiple metrics together.
6. Determine which condition takes priority when different metrics produce different health levels.
7. Determine how the `UP`/`DOWN` operational state affects overall health.
8. Provide a way to query the health of an individual server.
9. Apply health evaluation to servers managed by `ServerManager` if a concrete need arises.
10. Preserve all correct behavior from previous phases.

---

## Pending Design Decisions

The following decisions are intentionally not defined in advance and must be resolved during development when they become necessary:

- exact threshold values;
- whether all metrics use the same thresholds;
- whether threshold boundaries are inclusive or exclusive;
- what health state should correspond to a `DOWN` server;
- whether health should be stored as an attribute or calculated when requested;
- exact method names when multiple reasonable alternatives exist;
- how to resolve situations where different metrics produce different health levels;
- whether `ServerManager` needs health-related methods and which ones are actually necessary.

No new abstraction should be introduced until a concrete need appears.

---

## Responsibilities

`Server` will continue to represent and control the behavior of an individual server.

`ServerManager` will continue to manage multiple `Server` objects.

Health evaluation should be placed according to these responsibilities.

Do not use inheritance between `Server` and `ServerManager`.

Do not create additional classes solely to anticipate future requirements.

---

## Design Constraints

Keep the implementation simple.

Do not overengineer.

Health rules must be introduced progressively and only when required by the current step.

Reuse existing behavior where appropriate instead of duplicating logic.

Correct behavior from previous phases must remain intact.

---

## Out of Scope

During Phase 5, do NOT implement:

- alerts;
- notifications;
- metric history;
- timestamps;
- persistence;
- JSON;
- configuration files;
- logging;
- CLI;
- GUI;
- API;
- database integration;
- real operating system metrics;
- network connections;
- remote monitoring;
- threads;
- multiprocessing;
- `asyncio`;
- external libraries;
- email delivery;
- external service integrations.

Thresholds will initially remain part of the Python logic. Configuration through files or other mechanisms belongs to a later phase if it becomes necessary.

---

## Compatibility With Previous Phases

Phase 5 must preserve existing behavior.

The following `Server` functionality must continue to work:

- independent `Server` instances;
- initial `DOWN` state;
- `mark_up()`;
- `mark_down()`;
- `toggle_status()`;
- `is_up()`;
- `get_info()`;
- `__str__()`;
- metric updates;
- metric simulation;
- numeric validation;
- range validation;
- rejection of invalid metrics;
- independent state and metrics between different `Server` objects.

All `ServerManager` functionality must also continue to work:

- adding servers;
- retrieving managed servers;
- searching by hostname;
- rejecting duplicate hostnames;
- removing servers by hostname;
- filtering by operational state;
- retrieving `UP` servers;
- retrieving `DOWN` servers;
- counting servers;
- counting servers by operational state;
- checking whether servers exist;
- clearing the managed collection.

---

## Important Principle

A valid metric is not necessarily a healthy metric.

For example, a CPU usage value of `95` is valid because it is within the allowed range from `0` to `100`.

However, during this phase, that same value may be classified as a `WARNING` or `CRITICAL` condition.

Therefore:

**Validation determines whether the data is allowed to exist.**

**Health evaluation determines what that data means.**

These responsibilities must remain separate.

---

## Implementation Methodology

The phase will be developed incrementally.

Only one step will be worked on at a time.

For each step:

1. Provide one concrete implementation task.
2. The student writes all implementation code.
3. Do not provide solution code initially.
4. Review the implementation before continuing.
5. If errors exist, the student corrects them before moving forward.
6. Provide progressive hints when the student is stuck.
7. Do not introduce functionality from future steps.
8. Make important design decisions only when a real need appears.
9. Prioritize writing and reasoning about Python logic over auxiliary work.
10. Tests should be limited to what is necessary to verify the implemented behavior.

When temporary code in `main.py` is required for verification, provide the complete contents of `main.py`.

---

## Completion Criteria

Phase 5 will be complete when:

- ServerWatch can consistently evaluate the health of a server;
- clear rules exist for `HEALTHY`, `WARNING`, and `CRITICAL`;
- CPU, memory, and disk metrics participate correctly in health evaluation;
- boundary conditions are clearly defined and verified;
- the relationship between `UP`/`DOWN` and health is clearly defined;
- multiple metrics can be evaluated together;
- validation and health evaluation remain separate responsibilities;
- unnecessary logic duplication is avoided;
- functionality from Phases 1 through 4 remains operational;
- the necessary tests confirm the expected behavior.

---

## Project Principle

Complexity should emerge from real needs rather than being designed prematurely.

Phase 5 must remain focused on **interpreting the current state of servers through Python logic**, without prematurely turning ServerWatch into an alerting, persistence, or real monitoring system.