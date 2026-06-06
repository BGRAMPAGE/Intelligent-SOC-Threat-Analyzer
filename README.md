# Intelligent SOC Threat Analyzer

## Overview

Intelligent SOC Threat Analyzer is a Python-based cybersecurity analytics platform designed to process large-scale security logs and generate actionable threat intelligence. The system analyzes over 6 million cybersecurity events, identifies suspicious activities, calculates risk scores, detects security tools, and generates automated reports with visualizations.

## Features

### Threat Analysis

* Threat label distribution analysis
* Benign, Suspicious, and Malicious event classification
* Top attacker identification
* Most blocked IP analysis

### Security Tool Detection

* Nmap detection
* SQLMap detection
* Curl activity detection

### Risk Scoring Engine

* Dynamic risk scoring based on threat severity
* Top risk IP identification
* Threat prioritization

### Severity Classification

* CRITICAL
* HIGH
* MEDIUM
* LOW

### Visualization

* Threat Distribution Graph
* Protocol Distribution Graph
* Top Risk IP Analysis

### Automated Reporting

* Executive Summary
* Threat Statistics
* Risk Analysis
* Security Intelligence Report

---

## Dataset

Dataset: Cybersecurity Threat Detection Logs

Dataset Size:

* 6,000,000+ log events

Fields:

* timestamp
* source_ip
* dest_ip
* protocol
* action
* threat_label
* log_type
* bytes_transferred
* user_agent
* request_path

---

## Project Structure

```text
SOC_LOG_ANALYZER/

├── data/
│   └── cybersecurity_threat_detection_logs.csv
│
├── src/
│   ├── loader.py
│   ├── profiler.py
│   ├── analyzer.py
│   ├── risk_scoring.py
│   ├── severity.py
│   ├── visualizer.py
│   └── report_generator.py
│
├── reports/
│   └── security_report.txt
│
├── graphs/
│   ├── threat_distribution.png
│   ├── protocol_distribution.png
│   └── top_risk_ips.png
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd SOC_LOG_ANALYZER
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python main.py
```

Generated Outputs:

### Graphs

* threat_distribution.png
* protocol_distribution.png
* top_risk_ips.png

### Reports

* security_report.txt

---

## Results

### Dataset Statistics

* Total Logs Analyzed: 6,000,000
* Benign Events: 5,517,611
* Suspicious Events: 360,883
* Malicious Events: 121,506

### Security Analytics

* Threat Profiling
* Risk Scoring
* Protocol Analysis
* Security Tool Detection
* Incident Reporting

---

## Technologies Used

* Python
* Pandas
* Matplotlib

---

## Future Improvements

* Real-time log monitoring
* Streamlit dashboard
* Threat intelligence integration
* Multi-format log support
* Machine learning anomaly detection
* SIEM integration

---

## Author

Cybersecurity and AI Portfolio Project
