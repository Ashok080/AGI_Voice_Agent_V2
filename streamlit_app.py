import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AGI Voice Agent V2", layout="wide")

st.title("🤖 AGI Voice Agent V2 - Dataset Explorer")

DATASET_FOLDER = 'datasets'

# Ensure datasets folder exists
if not os.path.exists(DATASET_FOLDER):
    os.makedirs(DATASET_FOLDER)

# List available datasets
dataset_files = [f for f in os.listdir(DATASET_FOLDER) if f.endswith(('.csv', '.xlsx'))]

if dataset_files:
    dataset_choice = st.selectbox("Select a dataset to load:", dataset_files)

    if dataset_choice:
        dataset_path = os.path.join(DATASET_FOLDER, dataset_choice)

        try:
            if dataset_choice.endswith('.csv'):
                df = pd.read_csv(dataset_path)
            elif dataset_choice.endswith('.xlsx'):
                df = pd.read_excel(dataset_path)
            else:
                st.error("Unsupported file format.")
                df = None

            if df is not None:
                st.success(f"Loaded dataset: {dataset_choice}")
                st.write(f"**Shape:** {df.shape}")
                st.dataframe(df.head(20))
        except Exception as e:
            st.error(f"Failed to load dataset: {e}")
else:
    st.warning("No datasets found. Please upload datasets to the `datasets/` folder.")

st.markdown("---")
st.markdown("Created by **Ashok Miji** | AGI Voice Agent V2 | Streamlit App")
