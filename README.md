# Telecom Site Deployment Performance and SLA Monitoring in Indonesia

An end-to-end analytics project designed to monitor telecom site deployment progress, milestone completion, SLA compliance, issue aging, document readiness, vendor performance, reporting freshness, and escalation risk.

The project combines public regional data from West Java with realistically simulated telecom project-delivery records. It demonstrates Data Analyst capabilities with exposure to Analytics Engineering and Data Engineering practices.

## Business Problem

Telecom project-delivery information is often distributed across spreadsheets, issue trackers, document logs, email updates, and management reports. This fragmentation can lead to inconsistent KPI calculations, delayed escalation, weak vendor accountability, and limited visibility into project risks.

This project develops a governed analytical platform that consolidates these data domains into a reliable monitoring and decision-support system.

## Initial Project Scope

- Geography: West Java, Indonesia
- Period: January 2023–December 2025
- Initial scale: 100 synthetic telecom deployment sites
- Vendors: 5 fictional vendors
- Operational milestones: 9 deployment stages
- Documents: approximately 10 document types
- Issues: 3–5 issue categories
- Daily site progress records
- Dashboard: at least 6 decision-oriented Power BI pages

## Data Strategy

Public data is used to provide geographic and regional context.

Operational records covering sites, milestones, vendors, issues, documents, daily site progress, SLA performance, and risk scoring are synthetically generated from documented telecom project-delivery rules.

The synthetic operational data does not represent any real telecom operator, vendor, employer, or confidential project.

## Planned Architecture

```text
Public Regional Data
        +
Synthetic Operational Data
        ↓
Python Ingestion
        ↓
PostgreSQL Raw Layer
        ↓
dbt Staging, Intermediate, and Mart Models
        ↓
Airflow Orchestration
        ↓
Power BI Dashboard
```