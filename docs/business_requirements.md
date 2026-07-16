# Business Requirements Document

## Project Title
Telecom Site Deployment Performance and SLA Monitoring in Indonesia

## Positioning
Primary role: Data Analyst  
Secondary exposure: Analytics Engineering / Data Engineering

## Business Problem
Project stakeholders lack a single, reliable, and timely view of site progress, overdue milestones, SLA compliance, unresolved issues, document completeness, vendor workload, reporting freshness, and sites requiring escalation.

## Objective
Build a reproducible analytics platform that combines Indonesian public regional context with realistically simulated telecom project-delivery records to support monitoring, bottleneck analysis, SLA governance, and escalation prioritization.

## Primary Users
- Project Manager
- Project Controller

## Supporting Stakeholders
- Project Director
- Regional Manager
- Vendor Management
- Document Control
- Data/BI Team

## Initial Project Scope
West Java, Indonesia.

## Project Period
January 2023–December 2025.

## Initial Implementation Scale
- 100 synthetic telecom deployment sites
- 5 fictional vendors
- 9 operational milestones
- Approximately 10 document types
- 3–5 issue categories
- Daily site progress records
- At least 6 decision-oriented Power BI pages

## Data Strategy
Public data is used only for geographic and regional context.

Operational project records are synthetically generated for sites, milestones, vendors, issues, documents, daily site progress, SLA performance, and risk scoring.

The synthetic operational data must not represent any real telecom operator, vendor, employer, or confidential project.

## Core Business Questions
1. How many sites are planned, active, completed, overdue, and at risk?
2. What percentage of completed sites were finished on time?
3. Which milestones are the most frequent bottlenecks?
4. Which issue categories contribute the most delay?
5. Which vendors have the strongest and weakest SLA performance?
6. Which regions or deployment types have the highest backlog?
7. Which sites are technically complete but blocked by documents?
8. Which sites should management prioritize this week?
9. Is progress improving or deteriorating?
10. Are data-quality failures distorting KPIs?

## Core KPIs
- Total Sites
- Active Sites
- Completion Rate
- On-Time Completion Rate
- Average Delay Days
- Milestone SLA Compliance
- Open Issue Count
- Critical Issue Aging
- Document Completeness
- Progress Variance
- Vendor Backlog
- Risk-Weighted Backlog
- Reporting Freshness
- Data Quality Pass Rate

## Technical Architecture
Public and simulated sources → Python ingestion → PostgreSQL raw layer → dbt staging, intermediate, and mart models → Airflow orchestration → Power BI.

## Success Criteria
The initial implementation is considered successful when it includes a reproducible 100-site dataset, a working PostgreSQL database, documented dbt staging, intermediate, and mart models, critical data-quality and business-rule tests, one working Airflow DAG, a reconciled Power BI dashboard with at least six decision-oriented pages, an interpretable rule-based risk score, and a clear public case study.