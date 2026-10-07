# Phase 3 - Metric Validation

## Objective

Add basic validation to `Server` metrics so the object cannot accept
invalid CPU, memory, or disk values.

This phase starts from the metrics system built in Phase 2 and must
preserve all behavior achieved previously.

---

## Initial State

Each `Server` instance currently has the following metrics:

- `cpu_usage`
- `memory_usage`
- `disk_usage`

All three start at `0`.

The method:

`update_metrics(cpu_usage, memory_usage, disk_usage)`

updates all three metrics.

The method:

`simulate_metrics()`

generates random integer values between `0` and `100` and uses
`update_metrics()` to store them.

The metrics represent percentages.

---

## Functional Objective

Metrics must remain within the valid range:

`0 <= value <= 100`

This applies to:

- CPU
- memory
- disk

During this phase, the necessary rules will be added progressively to
prevent `Server` from ending up with invalid metrics.

---

## Scope

This phase must progressively cover:

1. Validation of the allowed metric range.
2. Definition of the behavior when a metric is outside the range.
3. Data type validation when appropriate.
4. Protection against partial updates: if a joint update contains any
   invalid value, the object must not be left partially updated.
5. Boundary value checks.
6. Invalid input checks.
7. Verification that `simulate_metrics()` continues to work with the new
   rules.
8. Preservation of the behavior achieved in Phases 1 and 2.

---

## Boundary Values

The values:

- `0`
- `100`

must be considered valid.

Values below `0` or above `100` must be considered invalid.

The exact policy for reacting to invalid values will be decided during
development before it is implemented.

---

## Design Restrictions

The validation introduced in this phase will be limited to metrics.

Do not implement yet:

- `hostname` validation;
- `ip_address` validation;
- real IP address validation;
- server health states;
- `HEALTHY`;
- `WARNING`;
- `CRITICAL`;
- configurable thresholds;
- alerts;
- metrics history;
- timestamps;
- persistence;
- JSON;
- configuration files;
- logging;
- real Linux metrics;
- new classes without a clear need.

Do not use external libraries to solve validation.

The implementation must remain simple and aligned with the current
ServerWatch scope.

---

## Compatibility With Previous Phases

Phase 3 must not break existing behavior.

The following must continue to work:

- independent creation of servers;
- initial `DOWN` state;
- `mark_up()`;
- `mark_down()`;
- `toggle_status()`;
- `is_up()`;
- `get_info()`;
- `__str__()`;
- `update_metrics()`;
- `simulate_metrics()`.

Each instance must continue to keep its own state and metrics
independently.

---

## Simulation

`simulate_metrics()` must continue to generate valid metrics.

The simulation must respect the same validation rules used by normal
updates and must continue reusing `update_metrics()`.

---

## Update Integrity

A call to `update_metrics()` represents a joint update of CPU, memory,
and disk.

By the end of this phase, an invalid update must not leave the object in
a partially updated state.

If any of the provided values invalidates the complete update, the
previous metrics must be preserved.

The concrete strategy for achieving this behavior will be decided during
implementation.

---

## Out of Scope

This phase does NOT yet determine whether a server is doing well or
poorly according to its metrics.

For example, CPU usage of `95%` can be a valid metric, even if a later
phase may consider it a problematic state.

Phase 3 answers only the question:

**Is the received data valid as a metric?**

It does not yet answer:

**Does the metric indicate that the server is healthy?**

---

## Completion Criteria

Phase 3 will be complete when:

- CPU, memory, and disk accept only the values defined as valid;
- the limits `0` and `100` work correctly;
- values outside the range are rejected according to the chosen policy;
- the accepted data types are clearly defined and checked;
- an invalid update does not partially modify the metrics;
- `simulate_metrics()` keeps working;
- `get_info()` and `__str__()` keep working;
- the `UP`/`DOWN` state remains independent from the metrics;
- the functionality from Phases 1 and 2 remains intact.

---

## Implementation Methodology

The phase will be developed incrementally.

Only one step will be implemented at a time.

Each step will be reviewed before continuing to the next one.

Functionality from later phases will not be introduced ahead of time.
