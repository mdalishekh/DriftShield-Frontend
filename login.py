import streamlit as st
from utils.api_client import login_user


st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# Hide sidebar and navigation on login page
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }

        [data-testid="stSidebarNav"] {
            display: none;
        }

        .block-container {
            max-width: 420px;
            padding-top: 8rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.toast(
    "Please login with ID & Password to get full access. [id: admin  pass: admin123]",
    duration="long"
)


st.title("DriftShield")
st.subheader("Login")


login_id = st.text_input(
    "Email or Username",
    placeholder="Enter your email or username"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter your password"
)


login_clicked = st.button(
    "Login",
    type="primary",
    use_container_width=True
)

guest_clicked = st.button(
    "Continue as Guest?",
    use_container_width=True
)


if login_clicked:
    if not login_id or not password:
        st.warning("Please enter ID and Password.")
    else:
        try:
            response = login_user(login_id, password)

            st.session_state.access_token = response["access_token"]
            st.session_state.logged_in = True

            st.rerun()

        except Exception:
            st.error("Invalid username/email or password.")


if guest_clicked:
    st.session_state.access_token = None
    st.session_state.logged_in = True

    st.rerun()