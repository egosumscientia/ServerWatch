# ServerWatch --- Phase 2: Server Metrics

## Previous State

**Phase 1 --- Basic Server Model** is complete.

The `Server` class currently exists, defined in `server.py`, with:

-   `hostname`
-   `ip_address`
-   `status`, initialized to `"DOWN"`
-   `mark_up()`
-   `mark_down()`
-   `toggle_status()`
-   `is_up()`
-   `get_info()`
-   `__str__()`

Phase 1 established the basic representation and state management of a
server.

------------------------------------------------------------------------

## Phase 2 Objective

Add basic resource utilization metrics to each server.

The initial metrics will be:

-   `cpu_usage`
-   `memory_usage`
-   `disk_usage`

These metrics will represent utilization percentages.

During this phase, the data will still be **simulated**. Real operating
system information will not be obtained yet.

------------------------------------------------------------------------

## Scope

This phase should progressively make it possible to:

-   represent each server's metrics;
-   keep their values as part of each instance's state;
-   update the metrics;
-   query the metrics;
-   integrate the metrics coherently with the existing `Server` model.

The concrete implementation will be decided step by step during
development.

------------------------------------------------------------------------

## Out of Scope

This phase will not introduce the following ahead of time:

-   range or type validations, unless the plan is explicitly changed;
-   services;
-   automatic health evaluation;
-   alerts;
-   measurement history;
-   files or JSON;
-   persistence;
-   logging;
-   real metric collection from Linux;
-   networking;
-   database;
-   graphical interface.

**Data validation initially belongs to Phase 3**.

------------------------------------------------------------------------

## Development Rules

1.  Work one step at a time.
2.  The user writes all implementation code.
3.  Do not provide solution code initially.
4.  Each step must indicate what to achieve, the expected behavior,
    the restrictions, and the important cases.
5.  Review the user's implementation before moving forward.
6.  Do not move forward while the current step has pending errors.
7.  If the user gets stuck, provide progressive hints before showing a
    solution.
8.  Do not introduce functionality from later phases.
9.  Preserve all correct behavior achieved in Phase 1.
10. Avoid overengineering.
11. When an important design decision has several reasonable
    alternatives, briefly explain the options and ask before deciding.
12. The assistant designs and performs the tests; the user focuses on
    implementing the logic.
13. When introducing new elements, explicitly indicate how to name
    files, classes, methods, attributes, functions, or other components,
    unless choosing the name is deliberately part of the exercise.

------------------------------------------------------------------------

## Starting Point

The first task in Phase 2 will be to add the following attributes to
each `Server` instance:

-   `cpu_usage`
-   `memory_usage`
-   `disk_usage`

Initially, all three metrics will start at `0`.

In this first step, no validations, update methods, or changes to
`get_info()` will be added yet.

------------------------------------------------------------------------

## Principle of the Phase

Metrics will be added in the simplest possible way, and additional
complexity will appear only when a concrete project need justifies it.
