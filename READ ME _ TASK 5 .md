# Life Sciences Research Intelligence Dashboard

## Project Overview

The Life Sciences Research Intelligence Dashboard is an interactive analytics application developed using Python, Pandas, and Streamlit. The dashboard enables users to explore biomarker research data through data visualization, searching, filtering, business metrics, and analytical insights.

The project demonstrates the practical application of data analytics in the life sciences domain and supports research intelligence activities through an intuitive user interface.

---

## Developed By

Ananya Kapoor

Internship Project – Excelra

---

## Domain

Biomarker Analytics

---

## Technologies Used

* Python
* Pandas
* Streamlit

---

## Dataset

Dataset Name:

biomarker_dataset.csv

The dataset contains biomarker research information including:

* Biomarker Name
* Disease
* Researcher Name
* Validation Status
* Country
* Priority
* Expression Level
* Sample Count

---

## Features Implemented

### Task 1 – Home Dashboard

Displays:

* Total Records
* Total Fields
* Total Diseases
* Total Researchers
* Dataset Overview

### Task 2 – View Data

Provides:

* Complete dataset view
* Scrollable data table
* Dataset download option

### Task 3 – Search Functionality

Allows users to search records using:

* Biomarker Name
* Disease
* Researcher Name

### Task 4 – Filter Functionality

Allows filtering based on:

* Validation Status
* Country
* Priority

### Task 5 – Metrics Dashboard

Displays:

* Total Biomarkers
* Validated Biomarkers
* Pending Biomarkers
* High Priority Biomarkers
* Total Sample Count

### Task 6 – Insights Dashboard

Generates insights such as:

* Most Studied Disease
* Most Active Researcher
* Top Country
* Highest Expression Biomarker
* Highest Sample Count Biomarker

### Task 7 – Biomarker Health Score

Calculates a custom Health Score using:

Health Score =
(Expression Level × 0.6)
+
((Sample Count ÷ 10) × 0.4)

Classification:

* High
* Medium
* Low

---

## Project Structure

Life_Sciences_Dashboard/

├── Life_Sciences_Dashboard_Cleaned.py

├── biomarker_dataset.csv

├── technology_choice.doc

├── README.md

└── Screenshots/

  ├── Home_Screen.png

  ├── Search_Screen.png

  ├── Filter_Screen.png

  ├── Metrics_Screen.png

  └── Insights_Screen.png

---

## Installation

Install required packages:

pip install streamlit pandas

---

## Running the Application

Execute the following command:

streamlit run Life_Sciences_Dashboard_Cleaned.py

The dashboard will launch in the browser at:

http://localhost:8501

---

## Deliverables

Included Deliverables:

* Source Code
* Dataset
* Technology Justification Document
* README File
* Dashboard Screenshots

---

## Business Value

This solution helps researchers and analysts:

* Explore biomarker datasets efficiently
* Identify important research trends
* Analyze validation status and priorities
* Monitor biomarker performance
* Generate actionable research insights

---

## Future Enhancements

* Advanced visualizations
* Real-time database connectivity
* Clinical trial integration
* Biomarker trend forecasting
* Machine learning-based predictions
* Cloud deployment support

---

## Conclusion

The Life Sciences Research Intelligence Dashboard successfully demonstrates the use of Python-based analytics for biomarker research intelligence. The solution combines data exploration, analytical reporting, and interactive visualization into a single platform, providing valuable support for research-driven decision making.

---

Developed by Ananya Kapoor

Excelra Internship Project

2026
