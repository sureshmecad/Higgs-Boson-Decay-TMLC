import streamlit as st
from streamlit.proto.NumberInput_pb2 import NumberInput
from model import predict
import joblib
import os
import numpy as np

st.set_page_config(page_title="HIGGS BOSON",
                   page_icon="📵", layout="wide")

curr_path = os.path.dirname(os.path.realpath(__file__))


feature_cols = joblib.load(curr_path + "/features.joblib")

with st.form("prediction_form"):
    st.header("Enter the Details about App")

    DER_mass_MMC = st.number_input("DER_mass_MMC: ")
    DER_mass_transverse_met_lep = st.number_input("DER_mass_transverse_met_lep: ")
    DER_mass_vis = st.number_input("DER_mass_vis: ")
    DER_deltar_tau_lep = st.number_input("DER_deltar_tau_lep: ")
    PRI_tau_pt = st.number_input("PRI_tau_pt: ")
    DER_met_phi_centrality = st.number_input("DER_met_phi_centrality:")
    DER_pt_h = st.number_input("DER_pt_h:")
    PRI_met = st.number_input("PRI_met:")
    submit_val = st.form_submit_button("Classify")


if submit_val:
    attributes = np.array([DER_mass_MMC, DER_mass_transverse_met_lep, DER_mass_vis, DER_deltar_tau_lep, PRI_tau_pt, DER_met_phi_centrality, DER_pt_h, PRI_met])

    print("attributes value")

    status = predict(attributes.reshape(1, -1))

    if status:
        st.error("The App is Background")
    else:
        st.success("The App is Signal")
        st.balloons()
