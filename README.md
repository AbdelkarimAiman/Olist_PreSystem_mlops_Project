# Olist E-Commerce Late Delivery Prediction - MLOps Inference Service

An end-to-end MLOps production-ready inference service that predicts whether an e-commerce order will be delivered late, using the Olist Brazilian E-Commerce dataset.

## 🚀 Project Overview
This project takes trained model artifacts (Random Forest model, scalers, and preprocessing objects) from previous pipeline notebooks and deploys them into a production-grade inference service using **FastAPI**, containerized with **Docker & Docker Compose**, tracked via **MLflow**, versioned with **DVC**, and validated using **Great Expectations**.

## 📂 Repository Structure
```text
├── app/                  # FastAPI service and API routes
├── config/               # Centralized configuration files (YAML/JSON)
├── data/                 # Data and DVC tracking files
├── models/               # Saved model artifacts (.pkl files)
├── notebooks/            # Original exploratory notebooks (for reference)
├── src/                  # Modular Python code (preprocessing, inference)
├── tests/                # Unit and integration tests (Pytest)
├── Dockerfile            # Container configuration for the API
├── docker-compose.yml    # Multi-container setup (Database + API + Storage)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

## How to Run from Zero

1.Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-folder>


2.Install dependencies:
```bash
pip install -r requirements.txt


3.Run tests:
```bash
pytest


4.Run with Docker Compose:
```bash
docker-compose up --build






Tech Stack
Python, Pandas, Scikit-Learn
FastAPI & Uvicorn
Docker & Docker Compose
MLflow & DVC   Pytest   