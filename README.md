# 🏥 Enterprise Healthcare Analytics Platform

### Transforming Healthcare Data into Executive Business Intelligence using Python • MySQL • SQL • Power BI

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.x-orange?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Analytics-yellow?logo=powerbi&logoColor=black)](https://www.microsoft.com/power-platform/products/power-bi)
[![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)](https://github.com/Deekshita12)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An end-to-end, enterprise-style healthcare analytics platform that transforms hospital operational data into actionable business intelligence through **Python ETL, MySQL database engineering, SQL analytics, and Power BI dashboards**.

---

## 📑 Table of Contents

- [⭐ Executive Summary](#-executive-summary)
- [📊 Project at a Glance](#-project-at-a-glance)
- [✨ Why This Project](#-why-this-project)
- [🚀 Key Features](#-key-features)
- [🔄 End-to-End Analytics Workflow](#-end-to-end-analytics-workflow)
- [🏗️ Enterprise Architecture](#️-enterprise-architecture)
- [⚙️ ETL Pipeline](#️-etl-pipeline)
- [🗄️ Enterprise Database Design](#️-enterprise-database-design)
- [🧩 Data Model](#-data-model)
- [📈 Business Intelligence Dashboards](#-business-intelligence-dashboards)
- [📁 Repository Structure](#-repository-structure)
- [🚀 Installation Guide](#-installation-guide)
- [📊 Business KPIs](#-business-kpis)
- [💡 Business Insights](#-business-insights)
- [💼 Skills Demonstrated](#-skills-demonstrated)
- [📖 Project Documentation](#-project-documentation)
- [🗺️ Project Roadmap](#️-project-roadmap)
- [🚀 Future Enhancements](#-future-enhancements)
- [🌟 Why This Project Stands Out](#-why-this-project-stands-out)
- [🤝 Acknowledgements](#-acknowledgements)
- [👩‍💻 Author](#-author)
- [📄 License](#-license)

---
# ⭐ Executive Summary

The **Enterprise Healthcare Analytics Platform** is a production-style healthcare analytics solution built to simulate a real-world hospital analytics environment.

The platform integrates:

- Patient admissions and hospital operations
- Clinical and diagnostic activity
- Workforce management
- Bed and resource utilization
- Pharmacy and inventory operations
- Billing and financial performance
- Insurance information
- Executive-level KPI reporting

The solution demonstrates the complete analytics lifecycle:

**Raw Healthcare Data → Python ETL → Enhanced Datasets → MySQL → SQL Analytics → Power BI → Executive Decision Support**

The project is designed as a portfolio-grade implementation for demonstrating practical capabilities in **Data Analytics, Data Engineering, SQL, Business Intelligence, and Healthcare Operations Analytics**.

---
# 📊 Project at a Glance

| Category | Details |
|---|---|
| 🏥 Domain | Healthcare Analytics |
| 📂 Healthcare Datasets | 19 |
| 🗄️ Database Tables | 19 |
| 🧱 Master Tables | 11 |
| 🔄 Transaction Tables | 8 |
| 🐍 Python Scripts | 20+ |
| ⚙️ SQL Modules | 14 |
| 📊 Power BI Dashboards | 6 |
| 📈 Business KPIs | 40+ |
| 🗄️ Database | MySQL 8.x |
| 🐍 Data Engineering | Python / Pandas |
| 📊 Visualization | Power BI |
| 💻 Version Control | Git & GitHub |

---
# ✨ Why This Project

Unlike a dashboard-only project, this platform demonstrates the complete path from **raw operational data to executive business intelligence**.

### 🏥 Healthcare Domain

End-to-end analysis of hospital operations, patients, admissions, clinical activity, workforce, pharmacy, billing, insurance, and resources.

### 🐍 Python Data Engineering

Data cleaning, validation, transformation, feature engineering, dataset enhancement, and preparation for database ingestion.

### 🗄️ Enterprise Database

A normalized MySQL relational database with primary keys, foreign keys, constraints, indexes, and modular SQL development.

### ⚙️ SQL Analytics

Business-focused views, queries, stored procedures, functions, triggers, events, and performance-oriented SQL development.

### 📊 Business Intelligence

Six Power BI dashboards designed around operational, clinical, financial, workforce, pharmacy, and executive decision-making needs.

---
# 🚀 Key Features

## 📂 Data Engineering

- Python-based ETL workflow
- Data cleaning
- Data validation
- Missing-value handling
- Feature engineering
- Dataset enhancement
- Analytics-ready CSV generation
- Data quality auditing

## 🗄️ Database Engineering

- MySQL 8.x
- Normalized relational schema
- Third Normal Form (3NF)
- Primary keys
- Foreign keys
- Referential integrity
- Constraints
- Index optimization
- Modular SQL architecture
- Enterprise naming conventions

## 📊 SQL Analytics

- SQL views
- Business queries
- Stored procedures
- SQL functions
- Database triggers
- Scheduled database events
- KPI calculations
- Performance optimization

## 📈 Business Intelligence

- Executive reporting
- Interactive Power BI dashboards
- Hospital KPI monitoring
- Operational analytics
- Clinical intelligence
- Financial intelligence
- Workforce analytics
- Pharmacy and inventory analytics
- Decision-support reporting

---
# 🔄 End-to-End Analytics Workflow

```text
                ┌──────────────────────────────┐
                │  Healthcare Operational Data │
                │        19 Datasets           │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │     Python Data Engineering  │
                │ Cleaning • Validation • ETL  │
                │ Feature Engineering          │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │    Enhanced Healthcare Data  │
                │     Analytics-Ready CSVs     │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │      Enterprise MySQL       │
                │ Tables • Keys • Constraints  │
                │ Indexes • Referential        │
                │ Integrity                    │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │       SQL Analytics Layer    │
                │ Views • Queries • Procedures │
                │ Functions • Triggers • Events│
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │       Power BI Layer         │
                │ 6 Executive & Operational    │
                │ Dashboards                   │
                └──────────────┬───────────────┘
                               │
                               ▼
                ┌──────────────────────────────┐
                │   Executive Decision Support │
                │ KPI Monitoring • Trends      │
                │ Operational Insights         │
                └──────────────────────────────┘
````

### 7. Enterprise Architecture — **image will show**

```markdown
# 🏗️ Enterprise Architecture

The platform follows a modular architecture separating **data engineering, database development, analytics, visualization, and decision support**.

## Architecture Components

| Layer | Description |
|---|---|
| 📂 Data Sources | Original healthcare CSV datasets |
| 🐍 Data Engineering | Python ETL, validation, cleaning, feature engineering |
| 📂 Enhanced Data | Analytics-ready healthcare datasets |
| 🗄️ Database | Enterprise MySQL relational database |
| 📊 Analytics | SQL views, queries, procedures, functions, triggers and KPIs |
| 📈 Visualization | Power BI dashboards |
| 👨‍⚕️ Decision Support | Executive and operational reporting |

## Architecture Diagram

![Enterprise Architecture](documentation/images/architecture.png)

---
# ⚙️ ETL Pipeline

The ETL layer prepares raw hospital datasets for reliable analytical use.

## ETL Workflow

| Stage | Description |
|---|---|
| **Extract** | Import raw healthcare datasets |
| **Validate** | Perform data quality and structural checks |
| **Clean** | Handle inconsistencies and missing values |
| **Transform** | Engineer and enrich analytical attributes |
| **Load** | Import enhanced datasets into MySQL |
| **Analyze** | Generate KPIs, business views, and reports |

## ETL Pipeline Diagram

![ETL Pipeline](documentation/images/etl_pipeline.png)

---
# 🗄️ Enterprise Database Design

The database follows a normalized relational design intended to support cross-functional hospital analytics.

## Database Highlights

| Feature | Status |
|---|:---:|
| Third Normal Form (3NF) | ✅ |
| Primary Keys | ✅ |
| Foreign Keys | ✅ |
| Referential Integrity | ✅ |
| Constraints | ✅ |
| Index Optimization | ✅ |
| Modular SQL Scripts | ✅ |
| Enterprise Naming Convention | ✅ |

## Database Modules

| Module | Purpose |
|---|---|
| Schema | Database creation |
| Master Tables | Core hospital entities |
| Transaction Tables | Operational healthcare transactions |
| Constraints | Primary and foreign key enforcement |
| Indexes | Query optimization |
| Import | Enhanced dataset loading |
| Views | Business reporting |
| Queries | Analytical SQL |
| Procedures | Reusable database operations |
| Functions | Business calculations |
| Triggers | Event-driven automation |
| Events | Scheduled database jobs |
| Security | Roles and permissions |
| Performance | Query and database optimization |

---
# 🧩 Data Model

The analytical data model integrates hospital entities and operational transactions across:

- Patients
- Admissions
- Departments
- Doctors
- Employees
- Wards
- Beds
- Diseases
- Diagnostic tests
- Patient diagnostics
- Billing
- Billing details
- Insurance providers
- Drug manufacturers
- Drugs
- Drug inventory
- Pharmacy-related transactions

The model is designed to support cross-functional reporting while maintaining relational integrity between operational entities.

## ER Diagram

![Entity Relationship Diagram](documentation/images/er_diagram.png)

## Data Model

![Healthcare Data Model](documentation/images/data_model.png)

---
# 📈 Business Intelligence Dashboards

The platform contains **six Power BI dashboards**, each designed for a specific decision-making layer of hospital operations.

---

## 🏥 Executive Command Center

Provides a high-level view of hospital-wide performance and executive KPIs.

### Key Areas

- Total patients
- Total admissions
- Bed occupancy
- Average length of stay
- Discharge performance
- Revenue
- Workforce
- Pharmacy indicators
- Operational trends

![Executive Command Center](documentation/images/dashboard_1.png)

---

## 🛏️ Patient Flow & Admission Analytics

Focuses on patient movement and admission operations.

### Key Areas

- Admission volume
- Patient flow
- Department-level activity
- Bed utilization
- Length of stay
- Discharge trends
- Operational bottlenecks

![Patient Flow & Admission Analytics](documentation/images/dashboard_2.png)

---

## 🩺 Clinical Intelligence Dashboard

Provides analytical visibility into clinical and diagnostic activity.

### Key Areas

- Disease patterns
- Diagnostic utilization
- Clinical activity
- Treatment-related trends
- Patient clinical distribution
- Department-level clinical performance

![Clinical Intelligence Dashboard](documentation/images/dashboard_3.png)

---

## 💰 Financial Intelligence Dashboard

Provides visibility into hospital financial performance.

### Key Areas

- Total revenue
- Billing performance
- Department revenue
- Average billing amount
- Insurance contribution
- Outstanding payments
- Financial trends

![Financial Intelligence Dashboard](documentation/images/dashboard_4.png)

---

## 👨‍⚕️ Workforce Intelligence Dashboard

Analyzes workforce distribution and staffing across hospital departments.

### Key Areas

- Total employees
- Active doctors
- Workforce distribution
- Department staffing
- Staff allocation
- Staff availability
- Workforce utilization

![Workforce Intelligence Dashboard](documentation/images/dashboard_5.png)

---

## 💊 Pharmacy & Inventory Intelligence Dashboard

Provides visibility into pharmacy operations and medicine inventory.

### Key Areas

- Medicine inventory
- Low-stock medicines
- Inventory utilization
- Manufacturer distribution
- Prescription volume
- Pharmacy performance
- Stock availability

![Pharmacy & Inventory Intelligence Dashboard](documentation/images/dashboard_6.png)

---
# 📁 Repository Structure

The repository follows a modular enterprise structure separating datasets, documentation, Python engineering, MySQL development, and Power BI reporting.

```text
Enterprise-Healthcare-Analytics-Platform/
│
├── 📂 datasets/
│   ├── 📂 original/
│   └── 📂 enhanced/
│
├── 📂 documentation/
│   ├── 📂 images/
│   │   ├── 🖼️ project_banner.png
│   │   ├── 🖼️ architecture.png
│   │   ├── 🖼️ etl_pipeline.png
│   │   ├── 🖼️ er_diagram.png
│   │   ├── 🖼️ data_model.png
│   │   ├── 🖼️ dashboard_1.png
│   │   ├── 🖼️ dashboard_2.png
│   │   ├── 🖼️ dashboard_3.png
│   │   ├── 🖼️ dashboard_4.png
│   │   ├── 🖼️ dashboard_5.png
│   │   └── 🖼️ dashboard_6.png
│   │
│   ├── 📄 Business_Requirements_Document.md
│   ├── 📄 Data_Dictionary.md
│   ├── 📄 KPI_Definitions.md
│   ├── 📄 System_Architecture.md
│   ├── 📄 Project_Workflow.md
│   └── 📄 enhanced_dataset_audit_summary.csv
│
├── 📂 mysql/
│   ├── 📂 schema/
│   ├── 📂 constraints/
│   ├── 📂 indexes/
│   ├── 📂 import/
│   ├── 📂 views/
│   ├── 📂 queries/
│   ├── 📂 procedures/
│   ├── 📂 functions/
│   ├── 📂 triggers/
│   ├── 📂 events/
│   ├── 📂 security/
│   └── 📂 performance/
│
├── 📂 powerbi/
│   ├── 📄 Enterprise Healthcare Analytics Platform.pbix
│   └── 📄 README.md
│
├── 📂 python/
│   ├── 📂 enhancement/
│   └── 📂 audit/
│
├── 📄 README.md
├── 📄 LICENSE
├── 📄 CHANGELOG.md
├── 📄 CONTRIBUTING.md
├── 📄 CODE_OF_CONDUCT.md
└── 📄 SECURITY.md
````
---

# 🚀 Installation Guide

Follow the steps below to set up the Enterprise Healthcare Analytics Platform in your local development environment.

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Deekshita12/Enterprise-Healthcare-Analytics-Platform.git
```

---

## 2️⃣ Navigate to the Project Directory

```bash
cd Enterprise-Healthcare-Analytics-Platform
```

---

## 3️⃣ Create the Database

Execute the SQL scripts in the following sequence.

| Order | SQL Module |
|-------:|------------|
| 01 | Database Creation |
| 02 | Master Tables |
| 03 | Transaction Tables |
| 04 | Foreign Keys |
| 05 | Indexes |
| 06 | Import Enhanced Datasets |
| 07 | SQL Views |
| 08 | Business Queries |
| 09 | Stored Procedures |
| 10 | SQL Functions |
| 11 | Database Triggers |
| 12 | Scheduled Events |
| 13 | Security Roles |
| 14 | Performance Optimization |

---

## 4️⃣ Execute Python ETL Scripts

Run the Python enhancement scripts to clean, validate, enrich, and export analytics-ready healthcare datasets before importing them into MySQL.

---

## 5️⃣ Open the Power BI Report

The Power BI dashboard file will be available inside the **powerbi** directory.

> 🚧 **Power BI report will be uploaded after dashboard completion.**

---

# 📊 Business KPIs

The platform provides executive-level KPIs across multiple hospital departments.

<table>

<tr>

<td width="50%">

### 🏥 Executive KPIs

- Total Patients
- Total Admissions
- Bed Occupancy Rate
- Average Length of Stay
- Discharge Rate
- Available Beds

</td>

<td width="50%">

### 💰 Financial KPIs

- Total Revenue
- Billing Performance
- Insurance Coverage
- Department Revenue
- Average Billing Amount
- Outstanding Payments

</td>

</tr>

<tr>

<td>

### 👨‍⚕️ Workforce KPIs

- Total Employees
- Active Doctors
- Staff Allocation
- Department Utilization
- Workforce Distribution
- Staff Availability

</td>

<td>

### 💊 Pharmacy KPIs

- Medicine Inventory
- Low Stock Medicines
- Inventory Utilization
- Manufacturer Distribution
- Prescription Volume
- Pharmacy Performance

</td>

</tr>

</table>

---

# 💡 Key Business Insights

The Enterprise Healthcare Analytics Platform enables hospital leadership to make informed, data-driven decisions by transforming operational data into actionable business intelligence.

### Executive Insights

- Monitor hospital-wide operational performance.
- Track organizational KPIs in real time.
- Identify performance trends across departments.
- Support strategic decision-making using executive dashboards.

### Operational Insights

- Improve patient admission and discharge efficiency.
- Optimize hospital bed utilization.
- Reduce operational bottlenecks.
- Enhance resource allocation.

### Financial Insights

- Monitor revenue performance.
- Analyze billing efficiency.
- Evaluate insurance contribution.
- Track department-wise financial performance.

### Clinical Insights

- Analyze disease patterns.
- Monitor diagnostic utilization.
- Evaluate treatment trends.
- Improve patient care reporting.

### Workforce Insights

- Optimize employee allocation.
- Improve departmental staffing.
- Monitor workforce productivity.
- Analyze doctor availability.

### Pharmacy Insights

- Track medicine inventory.
- Monitor stock availability.
- Improve procurement planning.
- Reduce inventory shortages.

---
---

# 💼 Skills Demonstrated

This project demonstrates practical expertise across the complete data analytics lifecycle, from data engineering and database development to business intelligence and executive reporting.

<div align="center">

| 🐍 Data Engineering | 🗄 Database Engineering | 📊 SQL Analytics | 📈 Business Intelligence |
|:------------------:|:----------------------:|:----------------:|:------------------------:|
| ETL Development | Relational Database Design | SQL Views | Power BI Dashboards |
| Data Cleaning | Database Normalization | Stored Procedures | Executive Reporting |
| Data Validation | Primary & Foreign Keys | SQL Functions | KPI Development |
| Feature Engineering | Constraints & Indexes | Database Triggers | Data Storytelling |
| Data Transformation | Performance Optimization | Business Queries | Operational Analytics |

</div>

---

# 📖 Project Documentation

Comprehensive documentation has been prepared to provide a complete understanding of the project's architecture, implementation, and analytical workflow.

| 📄 Document | 📌 Description | Status |
|-------------|---------------|:------:|
| Business Requirements Document | Functional and business objectives | 🚧 Coming Soon |
| Data Dictionary | Description of all datasets and attributes | 🚧 Coming Soon |
| System Architecture | End-to-End solution architecture | 🚧 Coming Soon |
| KPI Definitions | Business metrics and calculation logic | 🚧 Coming Soon |
| Project Workflow | Complete implementation workflow | 🚧 Coming Soon |
| ER Diagram Documentation | Database relationship documentation | 🚧 Coming Soon |

> **Note:** These documents will be uploaded in future updates as the project continues to evolve.

---

# 🗺️ Project Roadmap

The current implementation provides a complete analytics solution. Future releases will extend the platform with additional enterprise capabilities.

| Version | Planned Enhancement | Status |
|----------|---------------------|:------:|
| Version 1.0 | Enterprise Database Design | 
| Version 1.0 | Python ETL Pipeline | 
| Version 1.0 | SQL Analytics Layer |
| Version 1.0 | Power BI Dashboards | 
| Version 1.1 | Documentation Suite | 
| Version 1.2 | Interactive Architecture Diagrams | 
| Version 1.3 | Predictive Healthcare Analytics | 
| Version 2.0 | Cloud-Based Deployment | 

---

# 🚀 Future Enhancements

The Enterprise Healthcare Analytics Platform has been designed with scalability in mind. Future enhancements may include:

- Machine Learning-based Patient Risk Prediction
- Bed Occupancy Forecasting
- Hospital Resource Optimization Models
- Automated KPI Alerting
- Cloud Deployment using Microsoft Azure or AWS
- Real-Time Data Integration
- REST API Integration
- Mobile Executive Dashboard
- AI-Powered Clinical Decision Support
- Advanced Predictive Healthcare Analytics

---

# 🌟 Why This Project Stands Out

Unlike conventional dashboard projects, this repository demonstrates a complete enterprise analytics workflow.

✅ End-to-End Data Analytics Solution

✅ Enterprise Database Design

✅ Automated Python ETL Pipeline

✅ Production-Style SQL Development

✅ Executive Power BI Dashboards

✅ Healthcare Business Intelligence

✅ Modular Project Architecture

✅ GitHub Portfolio Ready

---

# 🤝 Acknowledgements

This project was developed as an enterprise-style portfolio project to simulate real-world healthcare analytics practices commonly used by hospitals, consulting firms, and business intelligence teams.

Special focus was placed on:

- Enterprise database architecture
- Data engineering best practices
- Business-oriented KPI development
- Executive dashboard design
- Professional project documentation

---

# 👩‍💻 Author

<div align="center">

# Deekshita Donthula

### Data Analyst | Python | SQL | MySQL | Power BI

Passionate about transforming complex healthcare data into meaningful business intelligence through analytics, automation, and interactive reporting.

---

### 📬 Connect With Me

💼 LinkedIn: *(Add LinkedIn Profile)*

📧 Email: *(Add Professional Email)*

🐙 GitHub: https://github.com/Deekshita12

</div>

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the MIT License.

For more details, please refer to the **LICENSE** file included in this repository.

---

<div align="center">

# 🏥 Enterprise Healthcare Analytics Platform

### End-to-End Hospital Operations Intelligence System

---

### Built with

🐍 Python • 🗄️ MySQL • 📊 SQL • 📈 Power BI • 💻 GitHub

---

⭐ **If you found this project useful, please consider giving it a Star!**

---

**© 2026 Deekshita Donthula**

</div>

<img src="documentation/images/dashboard_6.png" width="100%">

</p>

---
