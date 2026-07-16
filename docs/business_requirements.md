# Business Requirements Document

## Project Overview

**Project title:** Telecom Site Deployment Performance and SLA Monitoring in Indonesia

**Positioning:**  
Primary role: Data Analyst  
Secondary exposure: Analytics Engineering / Data Engineering

## Business Problem

Project stakeholders lack a single, reliable, and timely view of site progress, overdue milestones, SLA compliance, unresolved issues, document completeness, vendor workload, reporting freshness, and sites requiring escalation.

## Objective

Build a reproducible analytics platform that combines public regional context from West Java with realistically simulated telecom project-delivery records to support monitoring, bottleneck analysis, SLA governance, and escalation prioritization.

## Users

**Primary users**
- Project Manager
- Project Controller

**Supporting stakeholders**
- Project Director
- Regional Manager
- Vendor Management
- Document Control
- Data/BI Team

## Initial Project Scope

- Geography: West Java, Indonesia
- Period: January 2023–December 2025
- Initial scale: 100 synthetic telecom deployment sites
- Vendors: 5 fictional vendors
- Operational milestones: 9
- Documents: approximately 10 types
- Issues: 3–5 categories
- Daily site progress records
- Dashboard: at least 6 decision-oriented Power BI pages

## Data Strategy

Public data is used only for geographic and regional context.

Operational records covering sites, milestones, vendors, issues, documents, daily site progress, SLA performance, and risk scoring are synthetically generated from documented telecom project-delivery rules.

The synthetic data does not represent any real operator, vendor, employer, or confidential project.

## Business Questions and Decision Mapping

| ID | Business Question | Decision Supported | KPI / Output |
|---|---|---|---|
| BQ-01 | How many sites are planned, active, completed, overdue, and at risk? | Assess portfolio health | Total Sites, Active Sites, Completion Rate, High-Risk Sites |
| BQ-02 | What percentage of completed sites were finished on time? | Evaluate schedule reliability | On-Time Completion Rate |
| BQ-03 | Which milestones are the main bottlenecks? | Prioritize intervention | Overdue milestones, delay days, SLA compliance |
| BQ-04 | Which issue categories contribute most to delay? | Target recurring causes | Aging, resolution days, delay contribution |
| BQ-05 | Which vendors have strong or weak SLA performance? | Correct performance and balance capacity | Vendor SLA, backlog, completion rate |
| BQ-06 | Which regions or deployment types have the highest backlog? | Allocate support | Backlog, completion rate, progress variance |
| BQ-07 | Which technically complete sites are blocked by documents? | Prioritize document recovery | Completeness, rejection, revision |
| BQ-08 | Which sites should be prioritized this week? | Create an escalation list | Risk score, issue aging, reporting freshness |
| BQ-09 | Is progress improving or deteriorating? | Evaluate delivery trajectory | Planned versus actual progress trend |
| BQ-10 | Are data-quality failures distorting KPIs? | Protect reporting trust | Data Quality Pass Rate, freshness, rejected rows |

Every dashboard visual must answer at least one documented business question.

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

The initial implementation is considered successful when it includes:

- a reproducible 100-site dataset;
- a working PostgreSQL database;
- documented dbt staging, intermediate, and mart models;
- critical data-quality and business-rule tests;
- one working Airflow DAG;
- a reconciled Power BI dashboard with at least six decision-oriented pages;
- an interpretable rule-based risk score; and
- a clear public case study.
