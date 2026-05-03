# 📊 API to Power BI Data Pipeline Project

## 🚀 Project Overview

This project is a simple end-to-end **data pipeline** that extracts data from an API, processes and transforms it using Python (Pandas), and generates structured datasets for **Power BI reporting and visualization**.

It demonstrates the complete flow of:
**Data Collection → Data Transformation → Data Aggregation → BI Reporting**

---

## 🎯 Objective

To build a basic data engineering pipeline that:

* Fetches data from an external API
* Cleans and transforms raw data using Python
* Performs aggregations for business insights
* Exports processed data into CSV format
* Uses Power BI for interactive dashboards and reporting

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas (Data transformation & aggregation)
* Requests (API data extraction)
* CSV Files (Intermediate storage)
* Power BI (Data visualization)

---

## 📂 Project Workflow

### 1. Data Extraction

* Data is fetched from a public API using Python (`requests`)
* Raw JSON response is converted into a DataFrame

### 2. Data Transformation

* Handled missing values
* Converted data types
* Cleaned and structured dataset using Pandas

### 3. Data Aggregation

* Grouped data for meaningful insights
* Calculated KPIs such as:

  * totals
  * averages
  * trends over time

### 4. Data Export

* Final cleaned dataset is exported as CSV:

```
output_data.csv
```

### 5. Power BI Reporting

* CSV file imported into Power BI
* Built interactive dashboards:

  * KPI cards
  * Trend charts
  * Category-wise breakdowns
  * Filters and slicers

---

## 📊 Key Insights Generated

* Performance trends over time
* Category-wise comparisons
* Aggregated KPIs for business decisions

---
---
