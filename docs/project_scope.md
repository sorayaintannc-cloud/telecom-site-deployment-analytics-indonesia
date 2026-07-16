# Project Scope

## In Scope
- Project and site master
- Planned and actual milestones
- Milestone and issue SLA
- Issue lifecycle, severity, aging, responsible party, and root cause
- Document submission, approval, rejection, revision, and completeness
- Vendor workload and delivery performance
- Regional and deployment-type comparison
- Daily or weekly progress snapshots
- Reporting freshness
- Data-quality monitoring
- Rule-based risk and escalation prioritization
- Power BI dashboard and exportable action list

## Out of Scope for the Initial Implementation
- Network KPIs such as throughput, latency, and dropped calls
- Real-time streaming
- Finance, invoice, and accounting analytics
- Predictive machine learning
- Confidential employer data
- PII
- Real operator or vendor ranking
- Sensitive coordinates
- BigQuery
- Cloud deployment
- CI/CD
- Advanced alerting
- Schema drift outside an advanced branch

## Initial Project Boundaries
- Geography: West Java
- Period: January 2023–December 2025
- Prototype: 100 sites
- Vendors: 5 fictional vendors
- Milestones: 9–12
- Documents: about 10 types
- Issues: 3–5 categories

## Default Milestone Lifecycle
1. Site Identification
2. Survey
3. Land/Permit
4. Design Approval
5. Material Delivery
6. Civil Work
7. Installation
8. Integration/ATP
9. RFI/Handover
10. Completed

## Scope Change Rule
Every proposed feature must be classified as one of the following:
- Required for the Initial Implementation
- Optional Enhancement
- Future Release / Version 2
- Out of Scope

## Definition of Done
- Versioned 100-site hybrid dataset
- Synthetic-data configuration and methodology
- PostgreSQL raw layer
- dbt staging, intermediate, and marts
- Critical tests
- One Airflow DAG
- Incremental processing without duplicate business records
- Power BI dashboard with at least 6 pages
- SQL/dbt/Power BI reconciliation
- Rule-based risk score
- Data-quality page
- README, architecture, ERD, KPI dictionary, and limitations
- Executive findings and recommendations
