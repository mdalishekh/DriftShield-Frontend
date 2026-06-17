import streamlit as st

from utils.api_client import (
    get_models,
    upload_model,
    activate_model,
    delete_model
)

from utils.helpers import (
    prepare_models_dataframe
)


st.title("Model Registry")


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "refresh_models" not in st.session_state:
    st.session_state.refresh_models = True

if "models_data" not in st.session_state:
    st.session_state.models_data = []


# --------------------------------------------------
# Load Models
# --------------------------------------------------

if st.session_state.refresh_models:

    try:

        response = get_models()

        st.session_state.models_data = (
            response["models"]
        )

        st.session_state.refresh_models = False

    except Exception as e:

        st.error(f"Failed to load models: {e}")


# --------------------------------------------------
# Upload Section
# --------------------------------------------------

st.subheader("Upload New Model")


with st.form("upload_form"):

    model_file = st.file_uploader(
        "Model File (.pkl)",
        type=["pkl"],
        key="model_file"
    )

    scaler_file = st.file_uploader(
        "Scaler File (.pkl)",
        type=["pkl"],
        key="scaler_file"
    )

    metrics_file = st.file_uploader(
        "Metrics File (.json)",
        type=["json"],
        key="metrics_file"
    )
    
    reference_csv_file = st.file_uploader(
        "Reference CSV File (.csv)",
        type=["csv"],
        key="reference_csv"
    )

    upload_btn = st.form_submit_button("Upload Model")

    if upload_btn:

        if (
            model_file is None
            or scaler_file is None
            or metrics_file is None
            or reference_csv_file is None
        ):

            st.warning("Please select all files.")

        else:

            try:

                upload_model(
                    model_file=model_file,
                    scaler_file=scaler_file,
                    metrics_file=metrics_file,
                    reference_csv_file=reference_csv_file
                )

                st.success("Model uploaded successfully.")

                st.session_state.refresh_models = True

                st.rerun()

            except Exception as e:
                st.error(f"Upload failed: {e}")


st.divider()


# --------------------------------------------------
# Models Table
# --------------------------------------------------

st.subheader("Registered Models")


models = st.session_state.models_data


if not models:

    st.info("No models available.")

else:

    df = prepare_models_dataframe(models)

    st.dataframe(df,width='stretch')

    st.divider()

    st.subheader("Model Actions")

    for model in models:

        col1, col2, col3, col4 = st.columns(
            [5, 2, 2, 3]
        )

        with col1:

            active_text = (
                "🟢 ACTIVE"
                if model["is_active"]
                else "⚪ INACTIVE"
            )

            st.write(
                f"ID: {model['id']} | "
                f"{model['model_name']} "
                f"{active_text}"
            )

        with col2:

            activate_clicked = st.button(
                "Activate",
                key=f"activate_{model['id']}",
                disabled=model["is_active"]
            )

            if activate_clicked:

                try:

                    activate_model(model["id"])
                    st.success("Model activated.")
                    st.session_state.refresh_models = True
                    st.rerun()

                except Exception as e:

                    st.error(str(e))

        with col3:

            delete_clicked = st.button(
                "Delete",
                key=f"delete_{model['id']}",
                disabled=model["is_active"]
            )

            if delete_clicked:

                try:
                    delete_model(model["id"])
                    st.success("Model deleted.")
                    st.session_state.refresh_models = True
                    st.rerun()

                except Exception as e:

                    st.error(str(e))

        with col4:

            st.write(
                f"Uploaded: "
                f"{model['uploaded_at'][:10]}"
            )