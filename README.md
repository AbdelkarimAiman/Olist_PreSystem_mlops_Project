# Olist MLOps & Pre-System Project

A comprehensive Machine Learning Operations (MLOps) project built on the Olist e-commerce dataset, covering the complete end-to-end lifecycle including data preprocessing, training, experiment tracking, API serving, containerization, and continuous integration.

---

## 🚀 Project Overview
This project provides an engineering system to build and manage a predictive model using industry-standard MLOps tools. Key components include:
1. **Data Version Control (DVC):** For tracking dataset versions and ensuring data reproducibility.
2. **Experiment Tracking (MLflow):** For logging model metrics, parameters, and artifact management.
3. **API Serving (FastAPI):** To provide a robust REST API for real-time model inference.
4. **Containerization (Docker & Docker Compose):** To ensure isolated and consistent deployment across environments.
5. **Continuous Integration (GitHub Actions CI/CD):** For automated code testing on every push.

---

## 📂 Project Structure
```text
Olist_PreSystem_mlops_Project/
│
├── .github/
│   └── workflows/
│       └── ci.yml             # Automated CI/CD pipeline configuration
├── data/                      # Data directory (raw and processed)
├── models/                    # Saved trained machine learning models
├── src/                       # Core source code
│   ├── api.py                 # FastAPI application
│   ├── preprocessing.py       # Data cleaning and pipeline processing
│   ├── train.py               # Model training script with MLflow integration
│   └── config_loader.py       # Centralized configuration loader
├── tests/                     # Automated test suites (Pytest)
├── Dockerfile                 # API container configuration
├── docker-compose.yml         # Multi-container orchestration
├── requirements.txt           # Python dependencies
└── dvc.yaml                   # DVC pipeline stages
```

## 🛠️ Prerequisites

    Ensure you have the following installed on your machine:

    Python 3.9+

    Docker & Docker Compose

    Git

## ⚙️ Local Setup & Execution
## 1. Clone the repository and install dependencies:

```Bash
git clone <repository-url>
cd Olist_PreSystem_mlops_Project
pip install -r requirements.txt
```

## 2.Run training and log experiments with MLflow:

```Bash
python src/train.py
```

    To launch the local MLflow tracking UI:

```Bash
mlflow ui
```

    Then open your browser at: http://127.0.0.1:5000

## 3.Run automated local tests:

```Bash
PYTHONPATH=. pytest
```

## 🐳 Docker Deployment
To build and run the entire system inside an isolated container:

```Bash
docker-compose up --build
```
Once the container is running, access the interactive API documentation (Swagger UI) at:http://localhost:8000/docs

## 🤖 CI/CD Pipeline
The project includes a GitHub Actions workflow (.github/workflows/ci.yml) that automatically executes:

 - Environment setup and dependency installation.
