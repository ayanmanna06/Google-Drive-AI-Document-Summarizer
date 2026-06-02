# 🚀 Google Drive AI Document Summarizer

An AI-powered document summarization system that integrates with Google Drive, automatically downloads documents, extracts text, and generates intelligent summaries using **Google Gemini 2.5 Flash**.

---

## 📌 Project Overview

This application connects to a specified Google Drive folder, retrieves supported documents, extracts their contents, and generates concise AI-powered summaries.

The generated summaries are displayed through a modern Flask web dashboard and can also be exported as a CSV report.

---

## ✨ Features

### 🔗 Google Drive Integration

* Connects to Google Drive using a Service Account
* Accesses a specified folder
* Downloads supported documents automatically

### 📄 Document Processing

Supports:

* PDF (`.pdf`)
* Microsoft Word (`.docx`)
* Text Files (`.txt`)

### 🤖 AI-Powered Summarization

* Powered by Google Gemini 2.5 Flash
* Generates professional executive summaries
* Extracts key information from documents

### 📊 Dashboard Interface

* Modern Flask-based UI
* Document summary cards
* Processing status indicators
* Responsive design

### 📥 Report Export

* Download generated summaries as CSV
* Easy reporting and sharing

---

## 🏗️ Project Structure

```text
Google Drive Document Summarizer/

│
├── controller/
│   ├── drive_controller.py
│   ├── parser_controller.py
│   ├── summarizer_controller.py
│   └── report_controller.py
│
├── templates/
│   └── index.html
│
├── downloads/
├── reports/
│
├── .env
├── app.py
├── requirements.txt
└── credentials.json
```

---

## ⚙️ Technologies Used

### Backend

* Python
* Flask

### AI

* Google Gemini 2.5 Flash

### Google APIs

* Google Drive API
* Google Service Account Authentication

### Document Processing

* PyMuPDF
* python-docx

### Data Processing

* Pandas

---

## 🔄 Application Workflow

Generate AI Summary
│
▼
Display on Dashboard
│
▼
Export CSV Report

````

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/ayanmanna06/Google-Drive-AI-Document-Summarizer.git
cd Google-Drive-AI-Document-Summarizer
````

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
MODEL_NAME=gemini-2.5-flash
GOOGLE_DRIVE_FOLDER_ID=YOUR_FOLDER_ID
```

---

## ☁️ Google Drive Setup

1. Create a Google Cloud Project
2. Enable Google Drive API
3. Create a Service Account
4. Download the JSON credentials file
5. Rename it to:

```text
credentials.json
```

6. Share the target Google Drive folder with the Service Account email

---

## ▶️ Run Application

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```

---

## 📈 Sample Output

| File Name   | Summary                        |
| ----------- | ------------------------------ |
| sample.pdf  | AI-generated executive summary |
| report.docx | AI-generated executive summary |
| notes.txt   | AI-generated executive summary |

---

## 🎯 Assignment Objectives Achieved

* Google Drive Integration
* Document Downloading
* PDF Parsing
* DOCX Parsing
* TXT Parsing
* AI Summarization
* Flask Web Interface
* CSV Report Generation

---

## 🔮 Future Improvements

* PDF Report Export
* Multi-folder Support
* User Authentication
* Summary Search & Filtering
* Batch Processing
* Database Integration

---

## 👨‍💻 Author

**Ayan Manna**

* GitHub: https://github.com/ayanmanna06
* Email: [ayancse2023@gmail.com](mailto:ayancse2023@gmail.com)

---



