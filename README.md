# 🚀 FinDoc-AI

![FinDoc-AI Banner](FinDoc-Ai.png)

**FinDoc-AI** is an AI-powered financial document intelligence platform that transforms complex corporate PDFs into actionable investment insights — powered by cutting-edge LLMs, real-time market data, and interactive visualizations.

---

[![YouTube](https://img.shields.io/badge/Watch-YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/your-video-link)

---

## 🔍 Overview

FinDoc-AI lets users upload financial documents such as earnings reports, SEC filings, and press releases in PDF format, then automatically:

- Extracts detailed financial data & metrics using Meta LLaMA 3.2 via HuggingFace Inference API  
- Enriches analysis with live market data fetched from Yahoo Finance & YahooQuery  
- Enables natural language Q&A about financials through a smart chat interface  
- Generates professional PDF reports combining document insights & market trends  
- Visualizes key metrics with beautiful charts for quick interpretation  

Designed for investors, analysts, and portfolio managers seeking fast, accurate, and comprehensive financial analysis.

---

## ✨ Features

- **Document Upload & Parsing** — Upload any PDF and extract full financial data  
- **AI-Powered Extraction** — Advanced financial info parsed by LLaMA 3.2 model  
- **Live Market Data Integration** — Real-time company data and stock info  
- **Interactive Q&A** — Ask complex questions in natural language  
- **Automated Report Generation** — Detailed, visually rich PDF reports  
- **Data Visualization** — Bar charts and metric dashboards  
- **CORS Enabled** — Smooth backend-frontend interaction  

---

## 🛠️ Technologies Used

| Backend                                    | Frontend             | Others                    |
|--------------------------------------------|---------------------|---------------------------|
| ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) | ![Next.js](https://img.shields.io/badge/Next.js-13-black?logo=next.js) | ![Docker](https://img.shields.io/badge/Docker-Containers-blue?logo=docker) |
| ![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey?logo=flask) | ![React](https://img.shields.io/badge/React-18-blue?logo=react) | ![HuggingFace](https://img.shields.io/badge/HuggingFace-Inference-orange?logo=huggingface) |
| ![PyMuPDF](https://img.shields.io/badge/PyMuPDF-PDF-yellow) |                     | ![Yahoo Finance](https://img.shields.io/badge/Yahoo-Finance-purple) |
| ![ReportLab](https://img.shields.io/badge/ReportLab-PDF--Generation-red) |                     | ![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue) |

---

## 📦 Getting Started

### Prerequisites

- Python 3.8 or newer  
- HuggingFace API key ([Get one here](https://huggingface.co/settings/tokens))  
- (Optional) Node.js and npm/yarn for frontend  

### Backend Setup

```bash
git clone https://github.com/yourusername/FinDoc-AI.git
cd FinDoc-AI/backend

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
