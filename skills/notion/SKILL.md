# Notion Agent Skill

## Name

notion

## Version

1.0

## Description

A Notion workspace management skill for creating, updating, searching, and maintaining structured knowledge, tasks, projects, documentation, and operational records.

The agent must enforce structured thinking using **What / Why / Where / When / How** methodology and maintain clear ownership, traceability, and historical context.

---

# Core Responsibilities

The Notion agent is responsible for:

* Creating and managing tasks
* Maintaining project documentation
* Recording technical procedures and MOPs
* Capturing decisions and knowledge
* Updating progress and status
* Searching existing knowledge before creating duplicates
* Maintaining consistent information structure

---

# Operating Principles

## 1. Search Before Create

Before creating a new page, task, or document:

1. Search existing Notion content.
2. Check for similar tasks, projects, documents, or decisions.
3. Update existing records when appropriate.
4. Create a new entry only when no suitable record exists.

---

## 2. Structured Documentation

All technical tasks, projects, and operational documents should follow:

| Section | Purpose                                 |
| ------- | --------------------------------------- |
| What    | What is being done                      |
| Why     | Business or technical reason            |
| Where   | Environment, location, system, scope    |
| When    | Timeline, schedule, milestone           |
| How     | Methodology, procedure, execution steps |

---

# Task Management

When creating a task, capture:

## Task Title

Use a clear action-oriented title.

Examples:

* `MOP — Zoom Webinar UDP/TCP Performance Validation`
* `Configure DCI Link Monitoring Dashboard`
* `Review Fiber Route Acceptance Test`

---

## Required Task Information

Every task should contain:

### What

Describe the activity.

Example:

> Validate Zoom media transport behaviour using packet capture and bandwidth measurement.

---

### Why

Explain the purpose.

Example:

> Establish a baseline for enterprise webinar deployment and troubleshooting.

---

### Where

Specify affected environment.

Example:

> Malaysia host network, Singapore remote participant, Zoom Cloud.

---

### When

Specify:

* Planned date
* Deadline
* Maintenance window
* Milestone

---

### How

Include:

* Procedure
* Tools
* Commands
* Validation steps
* Expected outcome

---

# Technical Documentation Rules

For MOP, SOP, test plans, and implementation documents:

Use this structure:

```
# Title

## Overview

## What

## Why

## Where

## When

## How

## Prerequisites

## Implementation Steps

## Validation

## Rollback Plan

## Evidence

## Result / Findings

## Lessons Learned
```

---

# Network Engineering Documentation

For network-related work, capture:

## Architecture

Include:

* Topology
* Devices
* Interfaces
* IP addressing
* Connectivity path

Example:

```
Site A
 |
WAN / DCI
 |
Site B
```

---

## Validation

Always document:

* Expected result
* Actual result
* Measurement method
* Evidence collected

Examples:

Tools:

* ping
* traceroute
* iperf3
* Wireshark
* SNMP
* CLI outputs

---

# Task Status Management

Use consistent states:

| Status      | Meaning                  |
| ----------- | ------------------------ |
| Inbox       | Newly captured item      |
| To Do       | Planned work             |
| In Progress | Currently being executed |
| Blocked     | Waiting for dependency   |
| Review      | Pending validation       |
| Done        | Completed                |
| Archived    | Historical reference     |

---

# Knowledge Capture

When discovering reusable knowledge:

Create documentation instead of leaving information inside tasks.

Examples:

Convert:

```
Troubleshooting steps discovered during incident
```

Into:

```
KB — Troubleshooting High Packet Loss on WAN Links
```

---

# Decision Records

For important decisions:

Create:

```
ADR — Architecture Decision Record
```

Structure:

```
# Decision

## Context

## Options Considered

## Decision Made

## Reason

## Impact

## Follow-up Actions
```

---

# Change Management

For configuration changes:

Document:

* Current state
* Proposed state
* Change steps
* Validation
* Rollback

Example:

```
Before:
Interface MTU 1500

Change:
Set MTU 9000

After:
Verify jumbo frame support using ping -f
```

---

# Avoid

Do not:

* Create duplicate pages without checking
* Create vague task titles
* Store important decisions only in chat
* Create tasks without context
* Remove historical information
* Overwrite completed records without preserving history

---

# Agent Behaviour

When receiving a request:

1. Identify intent:

   * Task creation
   * Documentation
   * Search
   * Update
   * Knowledge capture

2. Search existing Notion records.

3. Apply correct structure.

4. Create or update content.

5. Confirm:

   * What was created
   * Location
   * Status
   * Next action

---

# Example Task Template

```
Task:
MOP — Network Performance Validation Test

Status:
To Do

What:
Perform network performance validation.

Why:
Confirm service readiness.

Where:
Production network environment.

When:
Scheduled maintenance window.

How:
1. Run baseline tests.
2. Capture traffic.
3. Validate results.
4. Document findings.

Evidence:
- Test results
- Screenshots
- Logs

Result:
Pending execution.
```