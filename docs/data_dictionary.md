# Data Dictionary

## Purpose
This document defines the main fields used in the operational and analytical data models for the Telecom Site Deployment Performance and SLA Monitoring in Indonesia project.

The dictionary will be refined during PostgreSQL and dbt implementation.

## `project_master`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `project_id` | String | Unique project identifier | Required and unique |
| `project_name` | String | Project or deployment program name | Required |
| `project_start_date` | Date | Planned project start date | Required |
| `project_end_date` | Date | Planned project end date | Must not precede start date |
| `project_status` | String | Current project status | Planned, Active, Completed, Cancelled |
| `target_site_count` | Integer | Planned number of sites | Must be greater than 0 |

## `site_master`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `site_id` | String | Unique telecom site identifier | Required, unique, never reused |
| `project_id` | String | Related project identifier | Required |
| `vendor_id` | String | Assigned fictional vendor | Required for active assigned sites |
| `region_code` | String | Official regional code | Required |
| `site_name` | String | Synthetic site name | Required |
| `deployment_type` | String | Type of deployment activity | Governed reference value |
| `technology` | String | Main technology classification | Governed reference value |
| `site_priority` | String | Business priority | Low, Medium, High, Critical |
| `site_complexity` | String | Site complexity classification | Low, Medium, High |
| `accessibility_class` | String | Site access difficulty | Easy, Moderate, Difficult |
| `urban_rural_class` | String | Regional classification | Urban, Peri-Urban, Rural |
| `restricted_area_flag` | Boolean | Indicates restricted-area complexity | True or False |
| `planned_start_date` | Date | Planned site start date | Required |
| `planned_completion_date` | Date | Planned site completion date | Must not precede planned start |
| `actual_start_date` | Date | Actual site start date | Nullable for planned sites |
| `actual_completion_date` | Date | Actual completion date | Required for completed sites |
| `site_status` | String | Current site-level status | Planned, In Progress, On Hold, Completed, Cancelled |
| `current_milestone_code` | String | Current operational stage | Must match milestone reference |
| `latest_update_date` | Date | Latest valid operational update | Used for reporting freshness |

## `vendor_master`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `vendor_id` | String | Unique fictional vendor identifier | Required and unique |
| `vendor_name` | String | Fictional vendor name | Must not match a real vendor |
| `vendor_tier` | String | Vendor capacity classification | Tier 1, Tier 2, Tier 3 |
| `primary_region_code` | String | Main assigned region | Nullable |
| `contract_start_date` | Date | Synthetic contract start date | Required |
| `contract_end_date` | Date | Synthetic contract end date | Must not precede start date |
| `vendor_status` | String | Vendor status | Active, Inactive |

## `region_reference`

Reference table containing public population, population density, and
administrative information for the 27 regencies and cities in West Java.

**Level of Detail:** One row per regency or city.

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `region_code` | String | Official BPS code for a regency or city | Required, unique, and four characters long |
| `regency_city_name` | String | Official name of the regency or city | Required and must match the official regional-code reference |
| `region_type` | String | Administrative area type derived from the region name | `Regency` or `City` |
| `population` | Integer | Total population in people | Required, non-negative, and converted from the original source unit of thousand people |
| `population_density` | Integer | Population density in people per square kilometre | Required and non-negative |
| `density_class` | String | Analytical population-density classification | `Low`, `Medium`, `High`, or `Very High` |
| `reference_year` | Integer | Year represented by the population and population-density values | Required; current implementation uses `2025` |

**Business key:**

```text
region_code
```

## `milestone_event`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `site_id` | String | Related site identifier | Required |
| `milestone_code` | String | Milestone identifier | Required |
| `planned_date` | Date | Planned milestone completion date | Required |
| `actual_date` | Date | Actual milestone completion date | Required when completed |
| `milestone_status` | String | Workflow status | Governed status value |
| `sla_status` | String | SLA evaluation status | Within SLA, At Risk, Breached, Not Applicable |
| `delay_days` | Integer | Positive delay beyond SLA due date | Minimum 0 |
| `blocked_flag` | Boolean | Indicates milestone blockage | True or False |
| `updated_at` | Timestamp | Latest source update | Required |

Business key:

```text
site_id + milestone_code
```

## `issue_event`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `issue_id` | String | Unique issue identifier | Required and unique |
| `site_id` | String | Related site identifier | Required |
| `issue_category_code` | String | Issue category | Required |
| `severity` | String | Issue severity | Low, Medium, High, Critical |
| `issue_status` | String | Current issue status | Governed status value |
| `open_date` | Date | Issue opening date | Required |
| `close_date` | Date | Issue closure date | Required when closed |
| `responsible_party` | String | Responsible team or vendor | Required |
| `root_cause` | String | Primary issue cause | Governed reference value |
| `resolution_days` | Integer | Days from open to close | Non-negative |
| `aging_days` | Integer | Current unresolved age | Non-negative |
| `sla_status` | String | Issue SLA status | Governed status value |
| `delay_contribution_days` | Integer | Estimated delay contribution | Non-negative |
| `updated_at` | Timestamp | Latest source update | Required |

## `document_event`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `document_id` | String | Unique document identifier | Required |
| `site_id` | String | Related site identifier | Required |
| `document_type_code` | String | Document type | Required |
| `revision_number` | Integer | Revision sequence | Starts at 1 |
| `submission_date` | Date | Submission or resubmission date | Nullable before submission |
| `review_date` | Date | Review decision date | Nullable |
| `approval_date` | Date | Final approval date | Required when approved |
| `document_status` | String | Current revision status | Governed status value |
| `rejection_reason` | String | Reason for rejection | Required when rejected |
| `required_flag` | Boolean | Indicates document applicability | True or False |
| `updated_at` | Timestamp | Latest source update | Required |

Business key:

```text
document_id + revision_number
```

## `site_progress_daily`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `site_id` | String | Related site identifier | Required |
| `reporting_date` | Date | Daily reporting date | Required |
| `planned_progress_pct` | Decimal | Expected progress percentage | 0–100 |
| `actual_progress_pct` | Decimal | Reported progress percentage | 0–100 |
| `progress_variance_pct` | Decimal | Actual minus planned progress | Calculated |
| `completed_milestone_count` | Integer | Number of completed milestones | 0–9 |
| `overdue_milestone_count` | Integer | Number of overdue milestones | Non-negative |
| `open_issue_count` | Integer | Number of unresolved issues | Non-negative |
| `open_critical_issue_count` | Integer | Number of unresolved critical issues | Non-negative |
| `document_completeness_pct` | Decimal | Approved required documents percentage | 0–100 |
| `days_since_last_update` | Integer | Reporting freshness measure | Non-negative |
| `stale_record_flag` | Boolean | Indicates stale operational data | True or False |
| `risk_score` | Decimal | Rule-based site risk score | 0–100 |
| `risk_band` | String | Risk classification | Low, Medium, High, Critical |
| `site_status` | String | Site status on reporting date | Governed status value |
| `current_milestone_code` | String | Current stage on reporting date | Required for active sites |

Business key:

```text
site_id + reporting_date
```

## `pipeline_run`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `run_id` | String | Unique pipeline run identifier | Required and unique |
| `started_at` | Timestamp | Pipeline start time | Required |
| `ended_at` | Timestamp | Pipeline end time | Nullable while running |
| `run_status` | String | Pipeline result | Running, Success, Failed |
| `input_row_count` | Integer | Source rows processed | Non-negative |
| `loaded_row_count` | Integer | Rows successfully loaded | Non-negative |
| `rejected_row_count` | Integer | Rows rejected by validation | Non-negative |
| `error_message` | String | Failure detail | Nullable |

## `data_quality_result`

| Column | Data Type | Description | Rule |
|---|---|---|---|
| `run_id` | String | Related pipeline run | Required |
| `test_id` | String | Unique test identifier | Required |
| `test_name` | String | Test description | Required |
| `model_name` | String | Tested table or model | Required |
| `quality_dimension` | String | Data-quality category | Governed category |
| `test_status` | String | Test result | Passed, Warning, Failed, Skipped |
| `failing_row_count` | Integer | Number of failing rows | Non-negative |
| `total_row_count` | Integer | Number of evaluated rows | Non-negative |
| `pass_rate` | Decimal | Percentage of passing records | 0–100 |
| `executed_at` | Timestamp | Test execution time | Required |

## Standard Audit Columns

Raw operational tables should include:

- `ingestion_run_id`
- `source_file_name`
- `source_row_number`
- `ingested_at`
- `source_updated_at`
- `record_hash`
- `is_deleted`
- `data_quality_status`
