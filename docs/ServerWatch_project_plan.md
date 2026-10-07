# ServerWatch --- Project Plan

## General Objective

Progressively develop a small server monitoring system in Python.

The project is oriented toward practical learning: complexity will be
added only when there is a real need. Initially, the project will work
with simulated data and, as it progresses, files, JSON, logging, Linux
interaction, processes, networking, or other concepts may be added if
they fit naturally into the development.

The phase plan acts as a general guide and may be adjusted if better
design decisions appear during development.

------------------------------------------------------------------------

## Phase 1 --- Basic Server Model

**Objective:** create the first representation of a server.

The system will begin by handling basic information such as:

-   hostname;
-   IP address;
-   UP/DOWN state.

This phase will make it possible to work with classes, objects,
attributes, and basic methods without introducing metrics or other
responsibilities yet.

------------------------------------------------------------------------

## Phase 2 --- Server Metrics

**Objective:** represent basic information about a server's resource
usage.

Metrics such as the following will be added progressively:

-   CPU usage;
-   memory usage;
-   disk usage.

The project will work with updating and querying these metrics using
simulated data at first.

------------------------------------------------------------------------

## Phase 3 --- Data Validation

**Objective:** prevent system objects from ending up in invalid states.

Validations will be introduced for data that already exists in the
project, such as metrics outside reasonable ranges or unsupported
states.

Validations will be added only when there is a concrete need derived
from previous phases.

------------------------------------------------------------------------

## Phase 4 --- Services

**Objective:** represent the services that run on a server.

The system will be able to associate services with each server and query
relevant information about them, including their state.

This phase will make it possible to work with collections and
relationships between different domain elements.

------------------------------------------------------------------------

## Phase 5 --- Health Evaluation

**Objective:** allow ServerWatch to determine a server's overall health
state.

The evaluation may consider information such as:

-   server availability;
-   metrics;
-   the state of its services.

The concrete rules will be defined when we reach this phase.

------------------------------------------------------------------------

## Phase 6 --- Alerts

**Objective:** automatically detect abnormal conditions.

The system will be able to identify situations such as:

-   high CPU usage;
-   high memory usage;
-   low available disk space;
-   stopped services;
-   unavailable server.

Alerts will be introduced into the system based on these conditions.

------------------------------------------------------------------------

## Phase 7 --- Monitoring Multiple Servers

**Objective:** evolve from monitoring a single server to managing several
servers.

ServerWatch must be able to maintain a collection of servers and perform
operations on them.

In this phase, the need for an entity representing the monitoring system
itself may arise naturally.

------------------------------------------------------------------------

## Phase 8 --- Measurement History

**Objective:** preserve information from previous measurements.

Up to this point, metrics may mainly represent the current state. In
this phase, the project will study how to record measurements over time.

This will make it possible to begin observing changes and historical
behavior.

------------------------------------------------------------------------

## Phase 9 --- Persistence

**Objective:** preserve information between different executions of the
program.

The use of the following will be evaluated:

-   files;
-   JSON;
-   reading and writing data.

The concrete structure will be decided according to the real state of
the project when this phase is reached.

------------------------------------------------------------------------

## Phase 10 --- Console Interface

**Objective:** allow ServerWatch to be operated from a terminal.

The interface may offer operations such as:

-   query servers;
-   query metrics;
-   query services;
-   view states;
-   query alerts.

A complex interface will not be defined ahead of time; it will be built
from the functionality that already exists.

------------------------------------------------------------------------

## Phase 11 --- Logging and Error Handling

**Objective:** improve the application's observability and robustness.

The project may add:

-   logging;
-   exception handling;
-   file error handling;
-   invalid data handling;
-   recording relevant events.

This phase should take advantage of real situations that appeared during
previous development.

------------------------------------------------------------------------

## Phase 12 --- Real Monitoring

**Objective:** begin replacing some simulated data with information
obtained from the real system.

Depending on how ServerWatch has evolved, concepts such as the following
may be explored:

-   real CPU information;
-   memory;
-   disk;
-   processes;
-   Linux services;
-   connectivity;
-   networking.

The exact scope will be decided only when this phase is reached.

------------------------------------------------------------------------

## Possible Extensions

The following features are **not a mandatory part of the project**:

-   automated testing;
-   database;
-   API;
-   graphical interface;
-   remote monitoring;
-   concurrency;
-   other integrations.

They will be added only if there is a concrete reason to do so and they
add value to ServerWatch's learning goals or functionality.

------------------------------------------------------------------------

## Development Methodology

The project will be developed under the following rules:

1.  Only one phase will be worked on at a time.
2.  Within each phase, only one step will be worked on at a time.
3.  The student will write all implementation code.
4.  Solution code will not be provided initially.
5.  Each step will indicate what must be achieved, the expected
    behavior, the restrictions, and the important cases.
6.  After each step, the implementation will be reviewed before
    continuing.
7.  The project will not move forward while the current step has pending
    errors.
8.  When difficulties arise, progressive hints will be provided before
    showing a solution.
9.  Important design decisions with several reasonable alternatives will
    be discussed before choosing one.
10. Functionality from future phases will not be added.
11. The correct behavior achieved in previous phases will be preserved.
12. The project structure will be reorganized only when the real
    complexity justifies it.
13. The plan may be adjusted during development if a clear technical or
    pedagogical reason appears.

------------------------------------------------------------------------

## Project Principle

**Complexity should appear as the consequence of a real need, not because
it was designed ahead of time.**
