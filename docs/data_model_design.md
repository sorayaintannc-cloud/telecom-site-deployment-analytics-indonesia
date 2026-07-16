# Data Model Design

## Purpose
This document defines the data model for the Telecom Site Deployment Performance and SLA Monitoring in Indonesia project.

The model supports site progress, milestone and SLA monitoring, issue aging, document readiness, vendor performance, risk prioritization, reporting freshness, and data-quality analysis.

## Modelling Approach
The project uses:

- operational tables for source-oriented records;
- dimension tables for descriptive attributes; and
- fact tables for measurable events and daily site progress records.

## Operational Tables

| Table | Level of Detail |
|---|---|
| `project_master` | One row per project |
| `site_master` | One row per telecom site |
| `vendor_master` | One row per fictional vendor |
| `region_reference` | One row per selected region |
| `milestone_reference` | One row per milestone definition |
| `document_type_reference` | One row per document type |
| `issue_category_reference` | One row per issue category |
| `milestone_event` | One row per site per milestone |
| `issue_event` | One row per issue |
| `document_event` | One row per document revision |
| `site_progress_daily` | One row per site per reporting date |
| `pipeline_run` | One row per pipeline run |
| `data_quality_result` | One row per test per pipeline run |

## Dimension Tables

| Table | Level of Detail |
|---|---|
| `dim_project` | One row per project |
| `dim_site` | One row per site |
| `dim_vendor` | One row per vendor |
| `dim_region` | One row per regency or city |
| `dim_date` | One row per calendar date |
| `dim_milestone` | One row per milestone definition |
| `dim_document_type` | One row per document type |
| `dim_issue_category` | One row per issue category |

## Fact Tables

| Table | Type | Level of Detail |
|---|---|---|
| `fact_milestone` | Event Fact Table | One row per site per milestone |
| `fact_issue` | Event Fact Table | One row per issue |
| `fact_document` | Analytical Fact Table | One row per required document per site |
| `fact_site_progress_daily` | Daily Site Progress Fact Table | One row per site per reporting date |
| `fact_pipeline_quality` | Event Fact Table | One row per test per pipeline run |

## Milestone Lifecycle

1. Site Identification
2. Survey
3. Land and Permit
4. Design Approval
5. Material Delivery
6. Civil Work
7. Installation
8. Integration and ATP
9. RFI and Handover

`Completed` is treated as a site-level final status.

## Status Design

### Site Status
- Planned
- In Progress
- On Hold
- Completed
- Cancelled

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

Overdue conditions are represented through `delay_days`, `overdue_flag`, and `sla_status`.

## Business Keys

| Entity | Business Key |
|---|---|
| Project | `project_id` |
| Site | `site_id` |
| Vendor | `vendor_id` |
| Region | Official regional code |
| Milestone | `site_id + milestone_code` |
| Issue | `issue_id` |
| Document revision | `document_id + revision_number` |
| Analytical document | `site_id + document_type_code` |
| Daily site progress record | `site_id + reporting_date` |
| Pipeline run | `run_id` |

## Key Business Rules

- `site_id` must be unique and never reused.
- Planned completion must not be earlier than planned start.
- Actual completion must not be earlier than actual start.
- Completed milestones must have an actual date.
- Closed issues must have a close date.
- Approved documents must have an approval date.
- Progress and risk scores must remain between 0 and 100.
- Stale records must be flagged, not treated as zero progress.
- Daily site progress records are append-only.
- Each site may have only one progress record per reporting date.
- Raw document history stores every revision.
- Risk score is calculated for each site on every reporting date.

## Risk Score

| Component | Weight |
|---|---:|
| Schedule deviation | 30% |
| Issue burden | 25% |
| Document readiness | 15% |
| Vendor performance | 15% |
| Site complexity | 10% |
| Data staleness | 5% |

Risk bands:

- 0–29: Low
- 30–49: Medium
- 50–69: High
- 70–100: Critical

## Initial Design Decisions

| Area | Decision |
|---|---|
| Geography | West Java |
| Initial scale | 100 synthetic sites |
| Operational milestones | 9 |
| Final completion | Site-level status |
| Milestone record level | One row per site per milestone |
| Issue record level | One row per issue |
| Raw document record level | One row per revision |
| Analytical document record level | One row per required document per site |
| Daily site progress record level | One row per site per reporting date |
| Risk method | Rule-based and interpretable |
