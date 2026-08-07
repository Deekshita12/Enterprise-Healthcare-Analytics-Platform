# 🏥 Enterprise Healthcare Analytics Platform

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](./python)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=for-the-badge&logo=mysql)](./mysql)
[![SQL](https://img.shields.io/badge/SQL-Analytics-blue?style=for-the-badge)](./mysql/queries)
[![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-yellow?style=for-the-badge&logo=powerbi)](./powerbi)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black?style=for-the-badge&logo=github)](https://github.com/Deekshita12)
[![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](./LICENSE)

</p>

<p align="center">

### End-to-End Enterprise Healthcare Analytics Platform built using Python, MySQL, SQL & Power BI for Hospital Operations, Resource Optimization and Executive Decision Support.

</p>

---

## 📌 Project Overview

The **Enterprise Healthcare Analytics Platform** is a comprehensive end-to-end healthcare analytics solution designed to transform raw hospital operational data into meaningful business intelligence. The project simulates an enterprise hospital environment by integrating multiple operational domains into a centralized analytics platform that enables executives and healthcare administrators to monitor performance, optimize resources, improve operational efficiency, and support data-driven decision-making.

The solution covers the complete analytics lifecycle—from data engineering and ETL processes to relational database design, SQL-based analytics, KPI development, and interactive Power BI dashboards. Built using **Python**, **MySQL**, **SQL**, and **Power BI**, this project demonstrates real-world healthcare analytics practices used in modern hospitals and healthcare organizations.

---

# 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Project Objectives](#-project-objectives)
- [Solution Overview](#-solution-overview)
- [Technology Stack](#-technology-stack)
- [Project Architecture](#-project-architecture)
- [Dataset Overview](#-dataset-overview)
- [Data Engineering Pipeline](#-data-engineering-pipeline)
- [Database Design](#-database-design)
- [SQL Analytics Layer](#-sql-analytics-layer)
- [Business Intelligence Dashboards](#-business-intelligence-dashboards)
- [Repository Structure](#-repository-structure)
- [Installation Guide](#-installation-guide)
- [Business KPIs](#-business-kpis)
- [Business Insights](#-business-insights)
- [Skills Demonstrated](#-skills-demonstrated)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

# 🎯 Business Problem

Modern hospitals generate massive volumes of operational data across multiple departments, including patient admissions, clinical services, workforce management, pharmacy, finance, laboratories, and resource allocation. However, this data is often stored in isolated systems, making it difficult for healthcare administrators to obtain a unified view of hospital performance.

Without an integrated analytics platform, hospitals face several operational challenges:

- Delayed executive decision-making due to fragmented reporting.
- Inefficient patient flow resulting in longer waiting times.
- Poor bed utilization and resource allocation.
- Limited visibility into workforce productivity.
- Difficulty monitoring financial performance across departments.
- Inefficient inventory tracking within pharmacy operations.
- Manual reporting processes that consume significant time and effort.
- Lack of centralized KPIs for monitoring hospital performance.

To address these challenges, organizations require an enterprise analytics platform capable of consolidating operational data, generating actionable insights, and supporting strategic decision-making through interactive business intelligence dashboards.

---

# 🎯 Project Objectives

The primary objective of this project is to design and develop a scalable enterprise healthcare analytics platform capable of transforming raw operational data into meaningful business intelligence.

The project aims to:

- Design an enterprise-grade relational database using MySQL.
- Develop an automated ETL pipeline using Python.
- Clean, validate, and enhance raw healthcare datasets.
- Build reusable SQL scripts for analytics and reporting.
- Create business-ready KPIs for hospital operations.
- Develop interactive Power BI dashboards for executive reporting.
- Simulate real-world healthcare analytics workflows followed by enterprise organizations.
- Enable data-driven decision-making across multiple hospital departments.

---

# 💡 Solution Overview

The Enterprise Healthcare Analytics Platform follows a complete analytics lifecycle, beginning with raw healthcare datasets and progressing through data engineering, database implementation, SQL analytics, and business intelligence reporting.

The solution integrates multiple technologies into a single analytics ecosystem:

- **Python** for data cleaning, validation, transformation, and feature engineering.
- **MySQL** for enterprise database design and relational data management.
- **SQL** for analytical queries, KPI generation, stored procedures, views, triggers, and business reporting.
- **Power BI** for executive dashboards and interactive visualization.

The platform provides a centralized analytical view of hospital operations by integrating data from admissions, patients, departments, employees, pharmacy, billing, laboratory services, insurance, and workforce management into a unified reporting environment.

This project demonstrates a production-style analytics workflow commonly used by healthcare organizations and consulting firms for operational performance monitoring and executive decision support.

---

# 🛠️ Technology Stack

The Enterprise Healthcare Analytics Platform leverages industry-standard tools and technologies across the complete data analytics lifecycle, from data engineering to business intelligence reporting.

| Category | Technology | Purpose |
|-----------|------------|---------|
| Programming Language | Python | Data Cleaning, Data Transformation, Feature Engineering & ETL |
| Database Management | MySQL 8.0 | Enterprise Relational Database Management |
| Query Language | SQL | Data Analysis, Reporting, Views, Procedures & KPIs |
| Data Processing | Pandas | Data Manipulation & Validation |
| Business Intelligence | Power BI | Interactive Dashboards & Executive Reporting |
| Version Control | Git & GitHub | Source Code Management |
| Development Environment | VS Code | Development & Project Management |

---

# 🏗️ Enterprise Project Architecture

The project follows a modern enterprise analytics architecture that transforms raw operational healthcare data into executive-level business intelligence.

```text
                               Enterprise Healthcare Analytics Platform

        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                           Raw Healthcare Datasets                           │
        └─────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                    Python ETL & Data Engineering Layer                      │
        │                                                                             │
        │ • Data Cleaning                                                             │
        │ • Data Validation                                                           │
        │ • Data Standardization                                                      │
        │ • Feature Engineering                                                       │
        │ • Data Enhancement                                                          │
        └─────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                         Enhanced Healthcare Datasets                        │
        └─────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                    Enterprise MySQL Relational Database                     │
        │                                                                             │
        │ • Master Tables                                                             │
        │ • Transaction Tables                                                        │
        │ • Foreign Keys                                                              │
        │ • Constraints                                                               │
        │ • Indexes                                                                   │
        └─────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                           SQL Analytics Layer                              │
        │                                                                             │
        │ • Views                                                                     │
        │ • Stored Procedures                                                         │
        │ • Functions                                                                 │
        │ • Triggers                                                                  │
        │ • Business Queries                                                          │
        │ • KPI Calculations                                                          │
        └─────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                     Power BI Business Intelligence Layer                    │
        └─────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
        ┌─────────────────────────────────────────────────────────────────────────────┐
        │                      Executive Decision Support System                      │
        └─────────────────────────────────────────────────────────────────────────────┘
```

---

# 🔄 Analytics Workflow

The platform follows a structured analytics workflow designed to simulate enterprise healthcare reporting systems.

```text
Raw CSV Files
      │
      ▼
Data Validation
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Enhanced Datasets
      │
      ▼
MySQL Database
      │
      ▼
SQL Analytics Layer
      │
      ▼
Business KPIs
      │
      ▼
Power BI Dashboards
      │
      ▼
Executive Decision Making
```

---

# 📂 Dataset Overview

The project integrates multiple interconnected healthcare datasets to simulate real-world hospital operations.

## Master Datasets

- Department
- Doctor
- Employee
- Ward
- Bed
- Disease
- Diagnostic Test
- Drug
- Drug Manufacturer
- Drug Inventory
- Insurance Provider

---

## Transactional Datasets

- Patient
- Admission
- Billing
- Billing Detail
- Prescription
- Patient Diagnostic
- Patient Insurance
- Staff Assignment

---

## Dataset Summary

| Dataset Category | Number of Tables |
|-----------------|-----------------:|
| Master Tables | 11 |
| Transaction Tables | 8 |
| Total Tables | 19 |
| Original Datasets | 19 |
| Enhanced Datasets | 19 |

The datasets are linked using primary and foreign key relationships to maintain referential integrity across the enterprise healthcare database.
---

# 🗄️ Enterprise Database Design

The Enterprise Healthcare Analytics Platform is built on a normalized relational database designed to efficiently manage healthcare operations across multiple business domains. The database architecture ensures data consistency, scalability, and high-performance analytical reporting through well-defined relationships, constraints, indexing strategies, and optimized SQL queries.

The database follows normalization principles to minimize redundancy while maintaining referential integrity between master and transactional tables.

## Database Components

### Master Tables

The master tables store static reference information used across the healthcare ecosystem.

| Table |
|--------|
| Department |
| Doctor |
| Employee |
| Ward |
| Bed |
| Disease |
| Diagnostic Test |
| Drug |
| Drug Manufacturer |
| Drug Inventory |
| Insurance Provider |

---

### Transaction Tables

The transactional tables capture day-to-day hospital activities.

| Table |
|--------|
| Patient |
| Admission |
| Billing |
| Billing Detail |
| Prescription |
| Patient Diagnostic |
| Patient Insurance |
| Staff Assignment |

---

## Database Features

✔ Normalized Relational Database

✔ Primary Keys

✔ Foreign Key Constraints

✔ Referential Integrity

✔ Optimized Indexing

✔ Enterprise Naming Conventions

✔ Reusable SQL Scripts

✔ Modular Database Structure

---

## Database Directory Structure

```text
mysql/
│
├── schema/
│   ├── 01_database.sql
│   ├── 02_master_tables.sql
│   └── 03_transaction_tables.sql
│
├── constraints/
│   └── 04_foreign_keys.sql
│
├── indexes/
│   └── 05_indexes.sql
│
├── import/
│   └── 06_import_data.sql
│
├── views/
│   └── 07_views.sql
│
├── queries/
│   └── 08_business_queries.sql
│
├── procedures/
│   └── 09_stored_procedures.sql
│
├── functions/
│   └── 10_functions.sql
│
├── triggers/
│   └── 11_triggers.sql
│
├── events/
│   └── 12_events.sql
│
├── security/
│   └── 13_security_roles.sql
│
└── performance/
    └── 14_performance_optimization.sql
```

---

# 📊 SQL Analytics Layer

A dedicated SQL analytics layer has been developed to support business reporting and executive decision-making.

The analytics layer includes:

- SQL Views
- Business Queries
- Stored Procedures
- SQL Functions
- Database Triggers
- Scheduled Events
- Performance Optimization Scripts

---

## SQL Views

Business views simplify reporting by consolidating operational data into reusable analytical datasets.

Examples include:

- Patient Summary View
- Admission Analytics View
- Bed Occupancy View
- Billing Summary View
- Workforce Performance View
- Pharmacy Inventory View

---

## Stored Procedures

Stored procedures automate repetitive business logic and reporting operations.

Examples include:

- Department Performance Summary
- Bed Occupancy Report
- Revenue Summary
- Daily Admission Report
- Employee Performance Report

---

## SQL Functions

Custom SQL functions perform reusable calculations throughout the database.

Examples include:

- Patient Age Calculation
- Length of Stay
- Revenue Calculations
- Occupancy Percentage
- Insurance Coverage Metrics

---

## Database Triggers

Triggers automate backend operations to improve consistency and maintain auditability.

Examples include:

- Automatic Timestamp Updates
- Inventory Adjustment
- Audit Logging
- Data Validation
- Status Synchronization

---

## Performance Optimization

To improve analytical performance, the project implements:

- Index Optimization
- Optimized JOIN Operations
- Query Performance Tuning
- Efficient Foreign Key Relationships
- Reusable Views
- Modular SQL Architecture

---

# 📈 Business Intelligence Dashboards

The analytical insights generated through SQL are visualized using **Power BI** dashboards designed for executive reporting and operational monitoring.

The project currently contains **6 interactive dashboards**, each focusing on a key operational area within the hospital.

---

## 🏥 Executive Command Center

**Purpose**

Provides executives with a centralized overview of hospital performance through high-level KPIs and operational metrics.

**Dashboard Preview**

> 🚧 Power BI dashboard screenshot will be added here.

---

## 🛏️ Patient Flow & Admission Analytics

**Purpose**

Monitors patient admissions, discharge trends, patient movement, and overall hospital flow to improve operational efficiency.

**Dashboard Preview**

> 🚧 Power BI dashboard screenshot will be added here.

---

## 🩺 Clinical Intelligence Dashboard

**Purpose**

Provides insights into clinical operations, disease distribution, diagnostic testing, and patient treatment patterns.

**Dashboard Preview**

> 🚧 Power BI dashboard screenshot will be added here.

---

## 💰 Financial Intelligence Dashboard

**Purpose**

Tracks revenue generation, billing performance, insurance coverage, payment trends, and financial KPIs.

**Dashboard Preview**

> 🚧 Power BI dashboard screenshot will be added here.

---

## 👨‍⚕️ Workforce Intelligence Dashboard

**Purpose**

Analyzes workforce allocation, staffing efficiency, employee utilization, and departmental performance.

**Dashboard Preview**

> 🚧 Power BI dashboard screenshot will be added here.

---

## 💊 Pharmacy & Inventory Intelligence Dashboard

**Purpose**

Monitors medicine inventory, pharmacy utilization, stock availability, and inventory performance.

**Dashboard Preview**

> 🚧 Power BI dashboard screenshot will be added here.
> ---

# 📁 Repository Structure

The project follows a modular repository structure to separate data engineering, database development, documentation, and business intelligence components.

```text
Enterprise-Healthcare-Analytics-Platform
│
├── datasets
│   ├── original
│   └── enhanced
│
├── documentation
│   ├── enhanced_dataset_audit_summary.csv
│   ├── data_dictionary
│   ├── audit_reports
│   ├── erd
│   └── project_notes
│
├── mysql
│   ├── schema
│   ├── constraints
│   ├── indexes
│   ├── import
│   ├── views
│   ├── queries
│   ├── procedures
│   ├── functions
│   ├── triggers
│   ├── events
│   ├── security
│   └── performance
│
├── powerbi
│
├── python
│   ├── enhancement
│   ├── audit
│   └── utils
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🚀 Installation Guide

Follow the steps below to set up and run the project locally.

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

Execute the SQL scripts in the following order.

```
01_database.sql

02_master_tables.sql

03_transaction_tables.sql

04_foreign_keys.sql

05_indexes.sql

06_import_data.sql

07_views.sql

08_business_queries.sql

09_stored_procedures.sql

10_functions.sql

11_triggers.sql

12_events.sql

13_security_roles.sql

14_performance_optimization.sql
```

---

## 4️⃣ Execute Python Scripts

Run the enhancement scripts to generate the enhanced healthcare datasets before importing them into MySQL.

---

## 5️⃣ Open Power BI

Open the Power BI report file.

```
Enterprise Healthcare Analytics Platform.pbix
```

*(Power BI report will be uploaded soon.)*

---

# 📊 Business KPIs

The platform measures hospital performance using executive-level Key Performance Indicators (KPIs).

## Executive KPIs

- Total Patients
- Total Admissions
- Bed Occupancy Rate
- Available Beds
- Average Length of Stay
- Patient Discharge Rate

---

## Financial KPIs

- Total Revenue
- Average Billing Amount
- Insurance Coverage
- Outstanding Payments
- Revenue by Department

---

## Workforce KPIs

- Total Employees
- Doctors Available
- Staff Allocation
- Department-wise Workforce Distribution

---

## Clinical KPIs

- Most Common Diseases
- Diagnostic Test Utilization
- Patient Disease Distribution
- Treatment Volume

---

## Pharmacy KPIs

- Available Medicines
- Low Stock Medicines
- Inventory Utilization
- Manufacturer-wise Distribution

---

# 💡 Key Business Insights

The analytics platform provides actionable insights that support operational and strategic decision-making across hospital departments.

### Executive Insights

- Monitor overall hospital performance from a centralized executive dashboard.
- Identify operational bottlenecks affecting patient flow.
- Track hospital-wide performance using standardized KPIs.

---

### Operational Insights

- Improve patient admission and discharge efficiency.
- Optimize bed allocation and occupancy.
- Reduce patient waiting times.

---

### Workforce Insights

- Analyze workforce utilization.
- Monitor departmental staffing levels.
- Improve employee allocation based on demand.

---

### Financial Insights

- Monitor revenue trends.
- Analyze billing performance.
- Evaluate insurance claim coverage.
- Identify revenue-generating departments.

---

### Pharmacy Insights

- Monitor medicine inventory.
- Identify low-stock medicines.
- Improve inventory planning.
- Track manufacturer performance.

---

# 💼 Skills Demonstrated

This project demonstrates practical experience across multiple areas of data analytics and data engineering.

## Data Engineering

- Data Cleaning
- Data Transformation
- Feature Engineering
- Data Validation
- ETL Development

---

## Database Development

- Relational Database Design
- Data Modeling
- Schema Design
- Primary & Foreign Keys
- Database Normalization

---

## SQL

- Complex SQL Queries
- SQL Views
- Stored Procedures
- SQL Functions
- Database Triggers
- Performance Optimization

---

## Business Intelligence

- Interactive Power BI Dashboards
- Executive Reporting
- KPI Development
- Healthcare Analytics
- Business Storytelling

---

## Tools & Technologies

- Python
- MySQL
- SQL
- Power BI
- Git
- GitHub
- Pandas
- VS Code

---

# 🚀 Future Enhancements

The current implementation provides a strong analytical foundation. Future enhancements may include:

- Real-Time Data Integration
- Machine Learning-Based Patient Risk Prediction
- Bed Occupancy Forecasting
- Automated KPI Alerts
- Cloud Deployment (AWS / Azure)
- API-Based Data Integration
- Role-Based Dashboard Access
- Mobile Executive Dashboard
- Healthcare Performance Forecasting
- AI-Assisted Clinical Decision Support

---

# 🏆 Project Highlights

- End-to-End Enterprise Analytics Project
- Enterprise Database Design
- Production-Style ETL Pipeline
- Relational Data Modeling
- SQL Analytics Layer
- Executive Power BI Dashboards
- Healthcare Business Intelligence
- GitHub Portfolio Project
- Modular Project Architecture
- Industry-Oriented Folder Structure

---

# 👩‍💻 Author

**Deekshita Donthula**

Data Analyst | SQL | Python | MySQL | Power BI

If you found this project useful, consider ⭐ starring this repository.

---

# 📄 License

This project is licensed under the **MIT License**.

For more details, refer to the **LICENSE** file included in this repository.
