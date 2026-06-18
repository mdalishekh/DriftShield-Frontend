import streamlit as st
import streamlit.components.v1 as components
from utils.api_client import (
    generate_drift_report,
    generate_drift_insights
)
from utils.helpers import get_drift_report_html



st.set_page_config(
    page_title="Drift Monitoring",
    layout="wide"
)

st.title("Drift Detection")


# Session State Initialization


if "drift_html" not in st.session_state:
    st.session_state.drift_html = None

if "drift_status" not in st.session_state:
    st.session_state.drift_status = None

if "drift_llm_response" not in st.session_state:
    st.session_state.drift_llm_response = None



# Generate Report Button


if st.button(
    "Generate Report",
    type="primary"
):

    
    # Generate Drift Report
    

    with st.spinner(
        "Generating Drift Detection Report With Evidently AI..."
    ):

        report_response = generate_drift_report()

    if report_response.get("status") != "success":

        st.error(
            report_response.get(
                "message",
                "Failed to generate drift report."
            )
        )

        st.stop()

    html_content = get_drift_report_html()

    if html_content is None:

        st.error(
            "drift_report.html not found."
        )

        st.stop()

    st.session_state.drift_html = html_content

    
    # Generate Insights
    

    with st.spinner(
        "Getting AI Insights for Drift Detection..."
    ):

        insight_response = generate_drift_insights()

    if insight_response.get("status") != "success":

        st.error(
            insight_response.get(
                "message",
                "Failed to generate drift insights."
            )
        )

    else:

        st.session_state.drift_status = (
            insight_response.get(
                "drift_status",
                "UNKNOWN"
            )
        )

        st.session_state.drift_llm_response = (
            insight_response.get(
                "llm_response",
                ""
            )
        )

    st.rerun()



# Render Drift Report


if st.session_state.drift_html:

    components.html(
    st.session_state.drift_html,
    height=1200,
    width=None,
    scrolling=True
)

    st.divider()

    
    # Drift Status
    

    if st.session_state.drift_status:

        status = (
            st.session_state.drift_status
            .upper()
        )

        if status == "HEALTHY":

            st.success(
                f"Drift Status : {status}"
            )

        elif status == "MODERATE":

            st.info(
                f"Drift Status : {status}"
            )

        elif status == "WARNING":

            st.warning(
                f"Drift Status : {status}"
            )

        elif status == "CRITICAL":

            st.error(
                f"Drift Status : {status}"
            )

        else:

            st.info(
                f"Drift Status : {status}"
            )

    
    # LLM Insights
    

    if st.session_state.drift_llm_response:

        st.markdown(
            st.session_state.drift_llm_response
        )