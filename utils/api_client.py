import requests
import streamlit as st
from config.config import ENV


# Authentication
def login_user(login_id: str, password: str) -> dict:

    try:
        response = requests.post(
            f"{ENV.BASE_URL}/api/v2/auth/login",
            json={
                "login_id": login_id,
                "password": password
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Login request failed: {str(e)}")


def get_auth_headers() -> dict:

    token = st.session_state.get("access_token")
    if not token:
        return {}

    return {
        "Authorization": f"Bearer {token}"
    }


# Prediction
def predict_loan(payload: dict) -> dict:

    try:
        response = requests.post(
            f"{ENV.BASE_URL}/api/v2/prediction",
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(
            f"Prediction API request failed: {str(e)}"
        )


# Model Registry
def get_models():

    try:
        response = requests.get(
            f"{ENV.BASE_URL}/api/v2/models/list",
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Model list request failed: {str(e)}")


def activate_model(model_id: int):

    try:
        response = requests.put(
            f"{ENV.BASE_URL}/api/v2/models/activate/{model_id}",
            headers=get_auth_headers(),
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Model activation request failed: {str(e)}")


def delete_model(model_id: int):

    try:
        response = requests.delete(
            f"{ENV.BASE_URL}/api/v2/models/delete/{model_id}",
            headers=get_auth_headers(),
            timeout=30
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Model deletion request failed: {str(e)}")


def upload_model(
    model_file,
    metrics_file,
    reference_csv_file
):

    files = {
        "model_file": (
            model_file.name,
            model_file,
            "application/octet-stream"
        ),
        "metrics_file": (
            metrics_file.name,
            metrics_file,
            "application/json"
        ),
        "reference_csv": (
            reference_csv_file.name,
            reference_csv_file,
            "text/csv"
        )
    }

    try:
        response = requests.post(
            f"{ENV.BASE_URL}/api/v2/models/upload",
            files=files,
            headers=get_auth_headers(),
            timeout=120
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"Model upload request failed: {str(e)}")


# Drift
def generate_drift_report():

    try:
        response = requests.post(
            f"{ENV.BASE_URL}/api/v2/drift/report",
            timeout=300
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }


def generate_drift_insights():

    try:
        response = requests.post(
            f"{ENV.BASE_URL}/api/v2/drift/insights",
            timeout=300
        )

        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }