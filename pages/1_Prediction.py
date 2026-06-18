import streamlit as st

from utils.api_client import predict_loan
from utils.helpers import render_prediction_result
from utils.sample_data import (
    EMPLOYMENT_TYPES,
    generate_sample_data
)



st.title("Loan Default Prediction")


# Session State Initialization


if "initialized" not in st.session_state:

    sample_data = generate_sample_data()

    for key, value in sample_data.items():

        st.session_state[f"sample_{key}"] = value

    st.session_state.prediction_result = None

    st.session_state.initialized = True



# Input Fields


col1, col2, col3 = st.columns(3)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=st.session_state.get(
            "sample_age",
            25
        ),
        key="age"
    )

    existing_loans = st.number_input(
        "Existing Loans",
        min_value=0,
        value=st.session_state.get(
            "sample_existing_loans",
            0
        ),
        key="existing_loans"
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=st.session_state.get(
            "sample_loan_amount",
            100000
        ),
        key="loan_amount"
    )

with col2:

    income = st.number_input(
        "Income",
        min_value=1,
        value=st.session_state.get(
            "sample_income",
            50000
        ),
        key="income"
    )

    existing_loan_emi = st.number_input(
        "Existing Loan EMI",
        min_value=0,
        value=st.session_state.get(
            "sample_existing_loan_emi",
            1000
        ),
        key="existing_loan_emi"
    )

    loan_tenure_months = st.number_input(
        "Loan Tenure (Months)",
        min_value=1,
        value=st.session_state.get(
            "sample_loan_tenure_months",
            24
        ),
        key="loan_tenure_months"
    )

with col3:

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=st.session_state.get(
            "sample_credit_score",
            650
        ),
        key="credit_score"
    )

    employed = st.selectbox(
        "Employed",
        options=["Yes", "No"],
        index=["Yes", "No"].index(
            st.session_state.get(
                "sample_employed",
                "Yes"
            )
        ),
        key="employed"
    )

    employment_type = st.selectbox(
        "Employment Type",
        options=EMPLOYMENT_TYPES,
        index=EMPLOYMENT_TYPES.index(
            st.session_state.get(
                "sample_employment_type",
                EMPLOYMENT_TYPES[0]
            )
        ),
        key="employment_type"
    )



# Predict Button


payload = {
    "age": age,
    "income": income,
    "credit_score": credit_score,
    "existing_loans": existing_loans,
    "existing_loan_emi": existing_loan_emi,
    "employed": (
        True
        if employed == "Yes"
        else False
    ),
    "loan_amount": loan_amount,
    "loan_tenure_months": loan_tenure_months,
    "employment_type": employment_type
}

predict_clicked = st.button(
    "Predict Default", type="primary"
)

if predict_clicked:

    try:

        with st.spinner(
            "Predicting default risk and generating AI-powered loan recommendations..."
        ):

            result = predict_loan(
                payload
            )

        st.session_state.prediction_result = result

        st.rerun()

    except Exception as e:

        st.error(str(e))



# Prediction Result

if st.session_state.prediction_result is not None:

    st.markdown("---")

    render_prediction_result(
        st.session_state.prediction_result
    )