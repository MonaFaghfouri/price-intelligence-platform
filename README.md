# 🛍️ Price Intelligence Platform

<p align="center">
  <b>A multi-source product search and price intelligence platform built with Python.</b>
</p>

<p align="center">
  Search • Compare • Normalize • Analyze • Export
</p>

---

## 🚀 Overview

**Price Intelligence Platform** is a Python-based application designed to collect, normalize, and compare product information across multiple e-commerce platforms.

The system combines different data acquisition strategies — including **API integration, web scraping, and browser automation** — and transforms heterogeneous product data into a unified structure suitable for comparison, analysis, and export.

The production version currently integrates **multiple Iranian and international e-commerce sources** through a single Streamlit interface.

> **Note**
>
> This repository contains a limited public demonstration of the project.
> The complete production scraping engines, platform-specific parsers, selectors, and deployment logic remain private.

---

## ✨ Key Features

* 🔎 Multi-source product search
* 💰 Cross-platform price comparison
* 🏷️ Original price and discounted price processing
* 📊 Unified product data structure
* 🌐 API-based data acquisition
* 🕷️ Web scraping
* 🤖 Browser automation with Playwright
* 🧹 Data cleaning and normalization
* 📦 Product and vendor information extraction
* 🔁 Retry and failure handling
* ⚙️ Multi-user execution controls
* 📥 Excel export
* 🎨 Interactive Streamlit interface
* 🌍 Support for Iranian and international marketplaces

---

## 🧠 How It Works

```text
                     ┌──────────────────┐
                     │   User Search    │
                     └────────┬─────────┘
                              │
                              ▼
                     ┌──────────────────┐
                     │ Streamlit UI     │
                     └────────┬─────────┘
                              │
                              ▼
              ┌──────────────────────────────┐
              │ Multi-Source Search Engine   │
              └──────────────┬───────────────┘
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
      ┌────────────┐  ┌─────────────┐  ┌───────────────┐
      │ REST APIs  │  │ Web Scraping│  │ Browser       │
      │            │  │             │  │ Automation    │
      └──────┬─────┘  └──────┬──────┘  └───────┬───────┘
             │               │                 │
             └───────────────┼─────────────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Data Extraction     │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Data Normalization  │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Price Processing    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Unified DataFrame   │
                  └──────────┬──────────┘
                             │
                  ┌──────────┴──────────┐
                  ▼                     ▼
            Interactive             Excel
              Results               Export
```

---

## 🛠️ Tech Stack

| Technology        | Usage                                   |
| ----------------- | --------------------------------------- |
| **Python**        | Core application                        |
| **Streamlit**     | Interactive web interface               |
| **Pandas**        | Data transformation and normalization   |
| **Requests**      | HTTP/API communication                  |
| **BeautifulSoup** | HTML parsing                            |
| **Playwright**    | Browser automation and dynamic scraping |
| **Threading**     | Concurrent execution management         |
| **OpenPyXL**      | Excel generation                        |
| **HTML / CSS**    | Custom interface styling                |

---

## 🔌 Data Acquisition Strategy

Different e-commerce platforms expose their data differently.

Instead of relying on a single collection method, the platform uses several acquisition approaches:

### API Integration

Where structured endpoints are available, product information is collected directly from remote services.

```text
API
 ↓
JSON
 ↓
Parser
 ↓
Normalized Product Data
```

### HTML Scraping

For traditional server-rendered websites:

```text
HTTP Request
 ↓
HTML
 ↓
BeautifulSoup
 ↓
Product Extraction
```

### Browser Automation

Dynamic websites requiring JavaScript rendering are processed using:

```text
Playwright
 ↓
Chromium
 ↓
Dynamic Page
 ↓
Product Cards
 ↓
Structured Data
```

---

## 🔄 Data Normalization

Because every marketplace returns a different structure, the system converts the results into a unified schema.

Example:

| Store         | Product   | Original Price | Final Price | Vendor   | Link |
| ------------- | --------- | -------------: | ----------: | -------- | ---- |
| Marketplace A | Product A |     12,500,000 |  11,900,000 | Vendor X | URL  |
| Marketplace B | Product B |     13,200,000 |  12,100,000 | Vendor Y | URL  |
| Marketplace C | Product C |              — |  12,450,000 | Vendor Z | URL  |

This unified structure enables easier:

* comparison
* filtering
* analysis
* reporting
* exporting

---

## 🏗️ Production-Oriented Design

The production version includes mechanisms designed for real-world deployment.

### Resource Management

Browser-based searches may create full Chromium instances.

The application therefore includes controls for managing simultaneous browser processes and preventing excessive CPU/RAM consumption.

### Retry Handling

Temporary network failures and rate limits are handled using retry and backoff mechanisms.

### Multi-Source Error Isolation

A failure in one marketplace does not necessarily stop the entire search process.

Successful sources can continue returning results independently.

---

## 📊 Example Workflow

```text
Search Query
    │
    ▼
"Industrial Pump"
    │
    ▼
Search Multiple Marketplaces
    │
    ▼
Extract Product Information
    │
    ▼
Normalize Different Schemas
    │
    ▼
Compare Prices
    │
    ▼
Display Results
    │
    ▼
Export to Excel
```

---

## 📸 Screenshots

### Home

<p align="center">
  <img src="screenshots/home.png" width="850">
</p>

### Product Search

<p align="center">
  <img src="screenshots/search.png" width="850">
</p>

### Results

<p align="center">
  <img src="screenshots/results.png" width="850">
</p>

---

## 📁 Repository Structure

```text
price-intelligence-platform/
│
├── README.md
│
├── demo_app.py
│
├── requirements.txt
│
├── .gitignore
│
├── screenshots/
│   ├── home.png
│   ├── search.png
│   └── results.png
│
└── sample_data/
    └── sample_results.csv
```

---

## 🎯 Public Demo vs Production Version

This repository is intentionally designed as a **technical showcase**.

### Included in the public repository

* Project architecture
* Technology stack
* Demonstration interface
* Sample dataset
* Screenshots
* Example workflow

### Not publicly distributed

The production implementation contains proprietary components including:

* platform-specific scraping engines
* production selectors
* internal API handling logic
* platform-specific parsers
* advanced browser automation routines
* concurrency implementation
* deployment configuration
* production optimization logic

These components are intentionally excluded from the public repository.

---

## 🔐 Source Availability

The complete production source code is **not open source**.

This repository is provided for:

* portfolio demonstration
* technical evaluation
* research and engineering showcase
* recruitment and academic application purposes

Commercial and production implementation details remain private.

---

## 💡 Engineering Challenges

Some of the main technical challenges addressed in this project include:

* integrating platforms with completely different structures
* processing both static and JavaScript-rendered websites
* normalizing heterogeneous pricing formats
* handling discounted and original prices
* preventing duplicate product records
* handling rate limits and temporary network errors
* controlling resource-intensive browser processes
* supporting multiple concurrent users
* generating clean Excel outputs

---

## 🗺️ Future Development

Potential future extensions include:

* 📈 historical price tracking
* 🔔 price-drop alerts
* 🤖 AI-powered product matching
* 🧠 semantic product similarity
* 📊 price trend visualization
* 🌐 additional marketplace integrations
* 🗄️ database-backed historical storage
* 🔍 advanced search filters
* ⚡ parallelized data collection

---

## 👩‍💻 Author

**Mona Faghfouri Azar**

Data Analytics • AI • Automation • Web Data Engineering

[GitHub](https://github.com/MonaFaghfouri)

---

## ⚠️ Disclaimer

This repository demonstrates the architecture and engineering concepts of the project.

Users of web data collection technologies are responsible for complying with the terms of service, robots policies, applicable laws, and access restrictions of any external websites they interact with.

---

<p align="center">
  <b>Python • Data Engineering • Web Automation • Price Intelligence</b>
</p>

<p align="center">
  © 2026 Mona Faghfouri Azar. All rights reserved.
</p>

