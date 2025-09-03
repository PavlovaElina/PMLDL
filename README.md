# MLOps Project: Model Deployment & Automated Pipeline

This repository contains the solution for the PMLDL Assignment 1. It demonstrates core MLOps practices by deploying a machine learning model via a web API and application, and optionally, by building a fully automated pipeline for data processing, model training, and deployment.

**Original Assignment:** [PMLDL Assignment 1: Deployment](https://datapaf.yonote.ru/share/a449539b-79dc-46c9-9b8d-21330e675c11/doc/pmldl-assignment-1-deployment-h7sqXwQo9g)

## 📋 Project Overview

The project is divided into two main parts:
1.  **Main Task**: A containerized deployment of a machine learning model using FastAPI and a Streamlit web app, orchestrated with Docker Compose.
2.  **Extra Task (Bonus)**: An automated MLOps pipeline built with DVC, MLflow, and Airflow that runs every 5 minutes to handle data processing, model training, and deployment.
---

## Repository Structure

### For the Main Task
├── code/
│ ├── models/ # Scripts for model training
│ └── deployment/
│ ├── api/
│ │ ├── main.py # FastAPI application
│ │ └── Dockerfile # API container definition
│ ├── app/
│ │ ├── app.py # Streamlit application
│ │ └── Dockerfile # App container definition
│ └── docker-compose.yml # Orchestrates multi-container setup
├── models/ # Directory for persisted model files (e.g., .pkl)
└── data/ # Directory for datasets (if needed for training)

### For the Extra Task (Bonus)
The structure extends to support the automated pipeline:
├── code/
│ ├── datasets/ # Scripts for data loading/cleaning/splitting (DVC pipelines)
│ ├── models/ # Scripts for feature engineering, training, logging (MLflow)
│ └── deployment/ # API and App code and Dockerfiles (as in Main Task)
├── data/
│ ├── raw/ # Original, immutable data dump
│ └── processed/ # Cleaned, split data for modeling (train/test sets)
├── models/ # Persisted trained models
├── services/
│ └── airflow/
│ └── dags/ # Airflow DAGs defining the automated pipeline
├── requirements.txt # The requirements file for reproducing the Python environment
└── (Other pipeline metadata files: dvc.yaml, params.yaml, mlruns/, etc.)


## Quick Start: Main Task (Model Deployment)

This section gets the core model API and web application up and running.

### Prerequisites
- **Docker** and **Docker Compose** must be installed on your system.
- A trained model file (e.g., `model.pkl`) placed in the `./models` directory. *(Note: The model file is not versioned in Git if it's too large)*.

### Steps to Run
1.  **Clone the repository** and navigate to its root directory.
    ```bash
    git clone <your-repo-url>
    cd <repository-name>
    ```

2.  **Build and launch the containers** using Docker Compose from the `code/deployment` directory.
    ```bash
    cd code/deployment
    docker-compose up --build
    ```
    This command will:
    - Build the Docker images for the API and the web app.
    - Start both containers.

3.  **Access the application**:
    - **Model API (FastAPI)**: Open your browser and go to `http://localhost:8000`. You will see the automatic interactive API documentation (Swagger UI).
    - **Web App (Streamlit)**: Open your browser and go to `http://localhost:8501`. You can use the form inputs to make predictions.

4.  **To stop the containers**, press `Ctrl+C` in the terminal where they are running, or run:
    ```bash
    docker-compose down
    ```

---

## Extra Task: Automated MLOps Pipeline

The bonus task implements a scheduled pipeline that automates the entire ML workflow.

### Pipeline Stages
1.  **Data Engineering (DVC/Airflow)**: Loads raw data from `data/raw/`, cleans it, handles missing values/outliers, and splits it into train/test sets saved to `data/processed/`.
2.  **Model Engineering (MLflow)**: Performs feature engineering, trains a model on the processed data, evaluates it on the test set, logs metrics (e.g., accuracy), and packages the best model to `models/`.
3.  **Deployment (Docker)**: Builds new Docker images for the API and app (incorporating the newly trained model) and deploys them using Docker Compose.

### How to Run the Pipeline
The pipeline is defined as an Airflow DAG located in `services/airflow/dags/`.

1.  **Start Airflow**: Ensure Airflow services (scheduler, webserver) are running.
2.  **Trigger the DAG**: The pipeline is scheduled to run every 5 minutes. You can also trigger it manually from the Airflow web UI (`http://localhost:8080`).
3.  **Monitor Runs**: Check the Airflow UI for DAG run status and logs. View model metrics and artifacts in the MLflow tracking UI (`http://localhost:5000` if running).

---

## Model & Dataset

- **Model**: [e.g., Scikit-learn Random Forest Classifier]
- **Dataset**: [e.g., Wine Quality Dataset from UCI ML Repo]
- **Task**: [e.g., Multi-class classification]

*Note: The Iris dataset was intentionally avoided to meet assignment requirements.*

---

## Tools & Technologies

- **Containerization**: Docker, Docker Compose
- **Web Framework**: FastAPI
- **Web Application**: Streamlit
- **Pipeline Automation (Extra Task)**: Apache Airflow, DVC, MLflow
- **Machine Learning**: Scikit-learn, Pandas, NumPy

---

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed for academic use within the PMLDL course.
