# Project Scope

## In Scope
- Project and site master
- Planned and actual milestones
- Milestone and issue SLA
- Issue lifecycle, severity, aging, responsible party, and root cause
- Document submission, approval, rejection, revision, and completeness
- Vendor workload and delivery performance
- Regional and deployment-type comparison
- Daily site progress records
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
- Personally identifiable information
- Real operator or vendor ranking
- Sensitive coordinates
- BigQuery
- Cloud deployment
- CI/CD
- Advanced alerting
- Schema drift outside an advanced development branch

## Initial Project Boundaries
- Geography: West Java
- Period: January 2023–December 2025
- Initial scale: 100 synthetic sites
- Vendors: 5 fictional vendors
- Operational milestones: 9
- Documents: approximately 10 types
- Issues: 3–5 categories
- Progress frequency: Daily reporting records

## Default Milestone Lifecycle
1. Site Identification
2. Survey
3. Land and Permit
4. Design Approval
5. Material Delivery
6. Civil Work
7. Installation
8. Integration and ATP
9. RFI and Handover

`Completed` is treated as a site-level final status, not as a separate operational milestone.

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
- dbt staging, intermediate, and mart models
- Critical data-quality and business-rule tests
- One working Airflow DAG
- Incremental processing without duplicate business records
- Power BI dashboard with at least 6 decision-oriented pages
- SQL, dbt, and Power BI reconciliation
- Rule-based and interpretable risk score
- Data-quality monitoring page
- README, architecture diagram, ERD, KPI dictionary, and project limitations
- Executive findings and business recommendations