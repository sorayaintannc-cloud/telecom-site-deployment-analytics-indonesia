# Project Rules

## Purpose
This document combines the milestone definitions and SLA rules used in the Telecom Site Deployment Performance and SLA Monitoring in Indonesia project.

The values are project assumptions for synthetic data generation and do not represent any specific operator or vendor contract.

## Milestone and SLA Matrix

| Code | Milestone | Main Prerequisite | Target Duration | Warning Window | Common Delay Drivers |
|---|---|---|---:|---:|---|
| `MS-01` | Site Identification | Project wave opened | 7 days | 2 days | Candidate scarcity, priority changes, incomplete initial information |
| `MS-02` | Survey | Site Identification completed | 10 days | 3 days | Access constraints, rescheduling, incomplete field information |
| `MS-03` | Land and Permit | Survey completed | 30 days | 7 days | Negotiation delays, incomplete documents, approval backlog |
| `MS-04` | Design Approval | Survey results available | 14 days | 4 days | Design revision, technical constraints, approval delay |
| `MS-05` | Material Delivery | Design and material requirements approved | 21 days | 5 days | Stock shortage, logistics delay, vendor workload |
| `MS-06` | Civil Work | Permit available and required materials ready | 30 days | 7 days | Weather, access issues, community constraints, crew capacity |
| `MS-07` | Installation | Civil Work completed | 14 days | 4 days | Crew capacity, missing equipment, site readiness issues |
| `MS-08` | Integration and ATP | Installation completed | 10 days | 3 days | Power issues, transmission dependency, configuration errors |
| `MS-09` | RFI and Handover | ATP passed and required documents available | 14 days | 4 days | Document rejection, outstanding punch list, incomplete handover package |

## Site Completion Rule
`Completed` is a site-level final status, not a separate milestone.

A site may be marked as `Completed` only when:

- all required milestones are completed;
- `RFI and Handover` is completed;
- mandatory documents are approved or formally exempted;
- no unresolved critical blocker remains; and
- `actual_completion_date` is available.

## Status Rules

### Milestone Status
- Not Started
- In Progress
- Completed
- Blocked
- Cancelled

### SLA Status
- Within SLA
- At Risk
- Breached
- Not Applicable

Milestone status and SLA status are stored separately.

## SLA Logic

```text
sla_due_date = sla_start_date + target_duration_days
delay_days = MAX(actual_or_reporting_date - sla_due_date, 0)
```

- `Within SLA`: completed on or before the due date.
- `At Risk`: still open and already within the warning window.
- `Breached`: completed late or still open after the due date.
- `Not Applicable`: cancelled, exempted, or not required.

The initial implementation uses calendar days.

## Additional SLA Rules

### Issue Resolution

| Severity | Target | Warning Window |
|---|---:|---:|
| Low | 14 days | 3 days |
| Medium | 7 days | 2 days |
| High | 3 days | 1 day |
| Critical | 1 day | 0 days |

### Document Review

| Activity | Target |
|---|---:|
| Initial review | 5 days |
| Resubmission after rejection | 7 days |

## Core Business Rules

- A completed milestone must have an `actual_date`.
- Open records are evaluated using `reporting_date`.
- Early completion does not create negative delay days.
- Cancelled activities are excluded from SLA compliance.
- A downstream milestone cannot be completed before its prerequisite unless an approved overlap rule exists.
- Each site may have only one governed record per milestone.

## Record Identification

```text
site_id + milestone_code
```
