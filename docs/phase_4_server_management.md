# Phase 4 - Multiple Server Management

## Objective

Turn ServerWatch from a model capable of representing an individual
server into a system capable of managing multiple servers.

This phase will be mainly focused on writing new Python logic.

A class responsible for maintaining and operating on a collection of
`Server` objects will be introduced, reusing everything built during
Phases 1, 2, and 3.

---

## Initial State

The following currently exists:

`src/server.py`

with the class:

`Server`

Each instance keeps:

- `hostname`
- `ip_address`
- `status`
- `cpu_usage`
- `memory_usage`
- `disk_usage`

It also has behavior to:

- change the state between `UP` and `DOWN`;
- check whether the server is `UP`;
- update metrics;
- simulate metrics;
- validate metric types and ranges;
- obtain information through `get_info()`;
- represent the server through `__str__()`.

Metrics accept `int` and `float`, reject `bool`, and must remain between
`0` and `100`.

An invalid update raises `ValueError` and does not partially modify the
metrics.

All of that behavior must be preserved.

---

## New Responsibility

During this phase, the following file will be created:

`src/server_manager.py`

with a class:

`ServerManager`

`ServerManager` will be responsible for managing a set of `Server`
objects.

The `Server` class will continue to represent an individual server.

The `ServerManager` class will represent the collection and the
operations related to several servers.

This separation will make it possible to practice composition between
objects without introducing inheritance or unnecessary architectures.

---

## Phase 4 Scope

The phase will be developed progressively and will cover:

1. Create `ServerManager`.
2. Keep an internal collection of servers.
3. Add `Server` objects to the collection.
4. Query the managed servers.
5. Search for a server by `hostname`.
6. Define and handle the behavior for duplicate servers.
7. Remove servers.
8. Filter servers by their operational state.
9. Get `UP` servers.
10. Get `DOWN` servers.
11. Perform simple operations on the collection when needed to
    consolidate the management logic.
12. Fully preserve the existing behavior of `Server`.

Everything will not be implemented at the same time.

Each capability will be introduced through small steps.

---

## Python Concepts to Practice

This phase should mainly be used to practice:

- creating and using classes;
- composition between objects;
- collections;
- lists and/or dictionaries depending on the design decisions;
- storing objects inside collections;
- iteration;
- searching;
- conditions;
- returning objects;
- filtering;
- removing elements;
- instance methods;
- responsibilities between classes;
- control flow;
- handling cases where a search produces no results;
- preventing inconsistent states.

The objective is not only to make ServerWatch work, but also to write and
reason about this logic manually.

---

## Initial Names

New file:

`src/server_manager.py`

New class:

`ServerManager`

During the phase, methods related to operations such as the following
will be introduced progressively:

- adding servers;
- searching for servers;
- removing servers;
- getting servers;
- filtering by state.

The concrete method names will be indicated when the corresponding step
begins.

They must not all be created ahead of time.

---

## Relationship Between `ServerManager` and `Server`

`ServerManager` will work with existing `Server` instances.

Conceptually:

`Server` represents a server.

`ServerManager` manages several `Server` objects.

Inheritance will not be used between these classes.

`ServerManager` must not duplicate internal logic that already belongs to
`Server`.

For example, the logic for changing a server to `UP` will continue to
belong to `Server`.

---

## Design Decisions That Must Be Discussed Before Implementation

If a decision with several reasonable alternatives appears during the
phase, it must be explained before one is chosen.

In particular, do not automatically decide:

- whether the internal collection should start as a list or a dictionary
  when both alternatives are reasonable;
- what should happen when trying to add a duplicate server;
- what criterion exactly defines a duplicate;
- what should happen when searching for a nonexistent server;
- what should happen when trying to remove a nonexistent server;
- whether certain methods should return objects, booleans, or another
  result when several reasonable options exist.

These decisions will be made during development, not ahead of time.

---

## Compatibility With Previous Phases

Phase 4 must not break or replace the behavior achieved previously.

The following must continue to work:

- independent creation of `Server` objects;
- initial `DOWN` state;
- `mark_up()`;
- `mark_down()`;
- `toggle_status()`;
- `is_up()`;
- independent metrics per server;
- `update_metrics()`;
- metric validation;
- `simulate_metrics()`;
- `get_info()`;
- `__str__()`.

Do not retroactively modify `Server` unless a concrete and justified
reason appears.

---

## Out of Scope

During this phase, do NOT implement:

- health states such as `HEALTHY`, `WARNING`, or `CRITICAL`;
- thresholds;
- alerts;
- metrics history;
- timestamps;
- persistence;
- files;
- JSON;
- database;
- configuration files;
- logging;
- CLI interface;
- graphical interface;
- API;
- real operating system metrics;
- network connections;
- remote monitoring;
- concurrency;
- threads;
- multiprocessing;
- `asyncio`;
- additional new classes without a clear need;
- external libraries.

Phase 4 must remain focused on managing `Server` objects in memory.

---

## Testing During This Phase

Tests will not be the main objective of Phase 4.

The assistant will design small checks when needed to verify that the
written logic works before moving forward.

The user will not have to develop a test suite or test files.

When it is necessary to use `main.py` temporarily, the assistant will
provide the complete file content.

After verifying a behavior, development will continue with new logic.

---

## Completion Criteria

Phase 4 will be complete when ServerWatch can correctly manage multiple
`Server` objects and perform the management operations defined during
development.

At minimum, by the end it must be possible to:

- create a `ServerManager`;
- add servers;
- keep several servers independent;
- query the collection;
- search for servers;
- prevent or correctly handle duplicates according to the chosen policy;
- remove servers;
- get `UP` servers;
- get `DOWN` servers;
- fully preserve each object's individual metrics and states;
- keep the behavior achieved in Phases 1, 2, and 3 intact.

---

## Required Methodology

The phase will be developed using the same methodology as before:

1. Work on only one phase at a time.
2. Within the phase, work on only one step at a time.
3. The user writes all implementation code.
4. Do not provide solution code initially.
5. Explain in words what must be implemented, its behavior,
   restrictions, and important cases.
6. The user pastes their implementation after each step.
7. Review the implementation before moving forward.
8. If it is correct, provide only the next step.
9. If it contains errors, explain the problem and allow the user to fix
   it.
10. Do not move forward while the current step is not correct.
11. If the user gets stuck, provide progressive hints before showing a
    solution.
12. Do not implement functionality from later steps ahead of time.
13. Do not overengineer.
14. Consult the user before resolving important design decisions with
    several reasonable alternatives.
15. Always preserve the correct behavior achieved previously.
16. Conceptual questions are answered without losing the exact point of
    development.
17. The assistant designs the tests; the user focuses on the logic.
18. If temporary code is needed in `main.py`, the assistant provides the
    complete file.
19. When something new is introduced, explicitly indicate the
    corresponding file, class, method, attribute, or function name,
    unless choosing the name is part of the exercise.

---

## Expected Result

By the end of this phase, ServerWatch will have moved from representing
isolated servers to having a first real layer for managing multiple
servers.

The logic will remain simple and entirely in memory, but it will provide
the foundation for later phases where the system can interpret metrics,
monitor groups of servers, and add more advanced functionality
progressively.
