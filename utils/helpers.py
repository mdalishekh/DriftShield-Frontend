import streamlit as st
import time
from pathlib import Path
import pandas as pd


def render_llm_response(
    text: str,
    speed: float = 0.01
) -> None:

    placeholder = st.empty()

    rendered_text = ""

    for char in text:

        rendered_text += char

        placeholder.markdown(
            rendered_text + "▌"
        )

        time.sleep(speed)

    placeholder.markdown(
        rendered_text
    )


def render_prediction_result(
    result: dict
) -> None:

    default_data = result["prediction"]
    default_status = ("Yes" if default_data["default"] else "No")

    st.subheader("Prediction Result")

    st.markdown(f"### Default Status : **{default_status}**")

    st.markdown(f"### Default Probability : **{default_data['probability']} %**")

    st.divider()

    st.subheader("LLM Suggestion")

    render_llm_response(result["llm_response"])
    
    



def prepare_models_dataframe(
    models: list
):

    df = pd.DataFrame(models)

    if df.empty:
        return df
    
    for col in ["uploaded_at", "activated_at"]:

        df[col] = pd.to_datetime(
            df[col]
        ).dt.strftime(
            "%Y-%m-%d %H:%M:%S"
        )


    df = df.rename(
        columns={
            "id": "ID",
            "model_name": "Model Name",
            "scaler_name": "Scaler Name",
            "metrics_name": "Metrics File",
            "reference_csv_name" : "Reference CSV",
            "uploaded_at": "Uploaded At",
            "activated_at": "Activated At",
            "is_active": "Active"
        }
    )

    return df   




def get_drift_report_html():
    """
    Check if reports/drift_report.html exists
    and return its HTML content.
    """

    report_path = Path("reports") / "drift_report.html"

    if not report_path.exists():
        return None

    try:
        with open(report_path, "r", encoding="utf-8") as file:
            return file.read()

    except Exception:
        return None