import requests
from config.config import ENV




def predict_loan(payload: dict) -> dict:

    try:

        response = requests.post(
            f"{ENV.BASE_URL}/api/v1/prediction",
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        raise Exception(
            f"Prediction API request failed: {str(e)}"
        )
        
        
        
def get_models():

    response = requests.get(
        f"{ENV.BASE_URL}/api/v1/models/list",
        timeout=30
    )

    response.raise_for_status()

    return response.json()



def activate_model(model_id: int):

    response = requests.put(
        f"{ENV.BASE_URL}/api/v1/models/activate/{model_id}",
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def delete_model(model_id: int):

    response = requests.delete(
        f"{ENV.BASE_URL}/api/v1/models/delete/{model_id}",
        timeout=30
    )

    response.raise_for_status()

    return response.json()


def upload_model(
    model_file,
    scaler_file,
    metrics_file,
    reference_csv_file
):

    files = {
        "model_file": (
            model_file.name,
            model_file,
            "application/octet-stream"
        ),
        "scaler_file": (
            scaler_file.name,
            scaler_file,
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

    response = requests.post(
        f"{ENV.BASE_URL}/api/v1/models/upload",
        files=files,
        timeout=120
    )

    response.raise_for_status()

    return response.json()        




def generate_drift_report():
    """
    Generate Evidently drift report.
    """

    try:
        response = requests.post(
            f"{ENV.BASE_URL}/api/v1/drift/report",
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
    """
    Generate LLM drift insights.
    """

    try:
        response = requests.post(
            f"{ENV.BASE_URL}/api/v1/drift/insights",
            timeout=300
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }