# KPI Dictionary

## Purpose
This document defines the core KPIs used in the Telecom Site Deployment Performance and SLA Monitoring in Indonesia project.

Each KPI must use a consistent definition across SQL, dbt, and Power BI.

## KPI Definitions

| KPI | Definition | Calculation | Main Use |
|---|---|---|---|
| Total Sites | Total number of unique sites in the selected scope | `COUNT(DISTINCT site_id)` | Measure portfolio size |
| Active Sites | Sites currently in active delivery status | Count of sites with `site_status = In Progress` | Monitor current workload |
| Completion Rate | Percentage of sites completed from all planned sites | `Completed Sites / Total Sites` | Measure delivery progress |
| On-Time Completion Rate | Percentage of completed sites finished on or before the planned completion date | `On-Time Completed Sites / Completed Sites` | Measure schedule reliability |
| Average Delay Days | Average positive delay among delayed completed sites | `AVG(delay_days)` where `delay_days > 0` | Measure lateness severity |
| Milestone SLA Compliance | Percentage of completed applicable milestones delivered within SLA | `Milestones Within SLA / Applicable Completed Milestones` | Evaluate process discipline |
| Open Issue Count | Number of unresolved issues | Count of issues with open or active status | Monitor unresolved workload |
| Critical Issue Aging | Number of days critical issues remain unresolved | `reporting_date - open_date` | Support escalation |
| Document Completeness | Percentage of required documents approved | `Approved Required Documents / Required Documents` | Measure handover readiness |
| Progress Variance | Difference between actual and planned progress | `actual_progress_pct - planned_progress_pct` | Identify schedule deviation |
| Vendor Backlog | Number of active or overdue sites assigned to a vendor | Count of active or overdue sites per vendor | Monitor vendor workload |
| Risk-Weighted Backlog | Total backlog adjusted by site risk | Sum of backlog records weighted by normalized risk score | Prioritize intervention |
| Reporting Freshness | Number of days since the latest valid site update | `reporting_date - latest_valid_update_date` | Identify stale records |
| Data Quality Pass Rate | Percentage of executed tests that pass | `Passed Tests / Executed Tests` | Monitor trust in analytical outputs |

## KPI Rules

### Total Sites
- Uses unique `site_id`.
- Cancelled sites remain visible but must be reported separately.
- Filters must follow the selected project, region, vendor, and period.

### Active Sites
- Includes sites with `site_status = In Progress`.
- Sites marked `On Hold` are reported separately.
- Completed and cancelled sites are excluded.

### Completion Rate
- Numerator: completed sites with a valid `actual_completion_date`.
- Denominator: all planned sites in scope.
- Cancelled sites must not be silently removed from reporting.

### On-Time Completion Rate
- A site is on time when `actual_completion_date <= planned_completion_date`.
- Only completed sites are included in the denominator.
- Early completion is counted as on time.

### Average Delay Days
- Delay days cannot be negative.
- Early completion is not included as negative delay.
- Active overdue sites should be analyzed separately from completed delayed sites.

### Milestone SLA Compliance
- Includes only completed and applicable milestones.
- Cancelled or exempt milestones are excluded.
- `Within SLA` is the numerator.
- `Within SLA` and `Breached` completed milestones form the denominator.

### Open Issue Count
Included statuses:
- Open
- In Progress
- Waiting External

Excluded statuses:
- Resolved
- Closed
- Cancelled

### Critical Issue Aging
- Includes only unresolved issues with `severity = Critical`.
- Uses `reporting_date` as the evaluation date.
- Closed critical issues use resolution duration instead of active aging.

### Document Completeness
- Includes only required and applicable documents.
- `Not Required` documents are excluded.
- Only `Approved` documents count as complete.

### Progress Variance
- Positive value: actual progress is ahead of plan.
- Zero: actual progress matches plan.
- Negative value: actual progress is behind plan.

### Vendor Backlog
- Includes active sites and sites past planned completion.
- Vendor results must be interpreted with site complexity and workload context.

### Risk-Weighted Backlog
Recommended initial calculation:

```text
SUM(risk_score / 100)
```

for active or overdue sites.

This KPI is used for prioritization and is not a financial measure.

### Reporting Freshness
- Calculated from the latest valid update.
- Active sites exceeding the freshness threshold must be flagged as stale.
- Stale records must not be treated as zero progress.

### Data Quality Pass Rate
- Includes passed, warning, and failed test executions in the audit table.
- Recommended calculation:

```text
Passed Tests / (Passed Tests + Warning Tests + Failed Tests)
```

- Skipped tests are excluded from the denominator.

## KPI Ownership

| KPI Group | Suggested Owner |
|---|---|
| Site progress and completion | Project Manager |
| Milestone SLA | Project Controller |
| Issue aging | Project Manager |
| Document completeness | Document Control |
| Vendor backlog and performance | Vendor Management |
| Risk prioritization | Project Manager |
| Reporting freshness | Project Controller |
| Data Quality Pass Rate | Data/BI Team |

## Governance Requirements

Each KPI must have:

- one approved definition;
- one documented calculation;
- a defined level of detail;
- inclusion and exclusion rules;
- a source analytical model;
- a refresh frequency; and
- reconciliation between SQL, dbt, and Power BI.
