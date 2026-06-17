import streamlit as st
import streamlit.components.v1 as components

from utils.api_client import (
    generate_drift_report,
    generate_drift_insights
)

from utils.helpers import get_drift_report_html


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.title("Drift Monitoring")


# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------

if "drift_html" not in st.session_state:
    st.session_state.drift_html = None

if "drift_status" not in st.session_state:
    st.session_state.drift_status = None

if "drift_llm_response" not in st.session_state:
    st.session_state.drift_llm_response = None


# --------------------------------------------------
# Status Color Mapping
# --------------------------------------------------

STATUS_COLORS = {
    "HEALTHY": "green",
    "MODERATE": "orange",
    "WARNING": "#FFD700",
    "CRITICAL": "red"
}


def render_status(status: str):
    color = STATUS_COLORS.get(status.upper(), "white")

    st.markdown(
        f"""
        <h2 style="
            color:{color};
            font-weight:bold;
            margin-top:20px;
        ">
            {status}
        </h2>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# Generate Report Button
# --------------------------------------------------

if st.button("Generate Report", type="primary"):

    # -------------------------
    # Report Generation
    # -------------------------

    with st.spinner("Generating report with Evidently AI..."):

        report_response = generate_drift_report()

    if report_response.get("status") != "success":
        st.error(report_response.get("message", "Failed to generate report."))
        st.stop()

    html_content = get_drift_report_html()

    if html_content is None:
        st.error("drift_report.html not found.")
        st.stop()

    st.session_state.drift_html = html_content

    # -------------------------
    # Insights Generation
    # -------------------------

    with st.spinner("Getting Insights from Groq LLM..."):

        insight_response = generate_drift_insights()

    if insight_response.get("status") != "success":
        st.error(
            insight_response.get(
                "message",
                "Failed to generate drift insights."
            )
        )

    else:
        st.session_state.drift_status = insight_response.get(
            "drift_status",
            "UNKNOWN"
        )

        st.session_state.drift_llm_response = insight_response.get(
            "llm_response",
            ""
        )

    st.success("Drift analysis completed successfully.")


# --------------------------------------------------
# Render Report
# --------------------------------------------------

if st.session_state.drift_html:

    st.subheader("Drift Report")

    components.html(
        st.session_state.drift_html,
        height=1200,
        scrolling=True
    )

    st.divider()

    # -------------------------
    # Status
    # -------------------------

    if st.session_state.drift_status:

        render_status(
            st.session_state.drift_status
        )

    # -------------------------
    # LLM Insights
    # -------------------------

    if st.session_state.drift_llm_response:

        st.markdown(
            st.session_state.drift_llm_response
        )