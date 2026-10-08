import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "access_token" not in st.session_state:
    st.session_state.access_token = None


if not st.session_state.logged_in:
    login = st.Page("login.py", title="Login", icon="🔐")
    st.navigation([login], position="hidden").run()
else:
    overview = st.Page("pages/1_Overview.py", title="Overview")
    prediction = st.Page("pages/2_Prediction.py", title="Prediction")
    drift = st.Page("pages/3_Drift_Detection.py", title="Drift Detection")
    models = st.Page("pages/4_Model_Registry.py", title="Model Registry")

    pg = st.navigation([
        overview,
        prediction,
        drift,
        models
    ])

    pg.run()