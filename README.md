
# DriftShield-Frontend


![Python](https://img.shields.io/badge/Python-3.13-blue) ![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red) ![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green) ![Docker](https://img.shields.io/badge/Docker-Container-blue) ![AWS](https://img.shields.io/badge/AWS-EC2%20%7C%20RDS%20%7C%20EBS-orange) 
---

# Project Overview

The DriftShield Frontend is a Streamlit-based user interface designed to interact with the DriftShield backend services. It provides an intuitive interface for performing loan default predictions, visualizing data drift reports, viewing AI-generated insights, and managing deployed machine learning models.

Rather than implementing machine learning logic directly, the frontend focuses on delivering a clean and interactive user experience while communicating with the backend through REST APIs. All prediction, monitoring, model management, and AI processing are handled by the backend services.

The application is organized into dedicated pages that guide users through the complete production machine learning lifecycle—from generating predictions to monitoring deployed models and deploying improved model versions.

---

# Key Features

- Interactive Loan Default Prediction Interface
- AI-Powered Loan Recommendation Display
- Interactive Drift Report Visualization
- AI-Generated Drift Analysis
- Model Registry Dashboard
- Dynamic Model Activation
- REST API Integration with FastAPI
- Responsive Streamlit User Interface

---

# Frontend Pages

| Page | Description |
|-------|-------------|
| **Overview** | Landing page introducing DriftShield and its workflow. |
| **Prediction** | Submit loan details and receive prediction results together with AI-generated recommendations. |
| **Drift Detection** | Generate Evidently AI drift reports and visualize AI-generated drift analysis. |
| **Model Registry** | Upload new model artifacts and activate deployed model versions. |

---

# Frontend Architecture

The frontend acts as the presentation layer of DriftShield. User interactions are translated into REST API requests that are sent to the FastAPI backend. The backend performs prediction, drift detection, model management, and AI processing before returning structured responses for visualization.

The frontend itself contains no machine learning logic and remains responsible only for user interaction, API communication, and result presentation.

---

# API Communication

The frontend communicates with the backend exclusively through REST APIs.

```
User
   │
   ▼
Streamlit Interface
   │
   ▼
api_client.py
   │
   ▼
FastAPI Backend
   │
   ▼
Prediction
Drift Detection
Model Registry
```

---

# Related Documentation

The frontend repository contains only the user interface implementation.

For complete backend architecture, machine learning workflow, deployment pipeline, and production infrastructure, refer to the backend repository.

### Backend Repository

https://github.com/mdalishekh/DriftShield

### Backend Project Structure

See:

[Frontend Project Structure](Frontend-Structure.md)

### Deployment Architecture

See:
https://github.com/mdalishekh/DriftShield/blob/main/Deployment.md

---
# 👨‍💻 About 

-  **Portfolio:**  https://mdalishekh.in/  
-  **LinkedIn:**  https://www.linkedin.com/in/mdalishekh/  
-  **GitHub:**  https://github.com/mdalishekh
-  **Email:** mdalishekh.work@gmail.com