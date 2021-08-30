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
    DER_mass_transverse_met_lep = st.number_input("DER_mass_transverse_met_lep: ", value=0, format="%d")
    DER_mass_vis = st.number_input("DER_mass_vis: ")
    DER_deltar_tau_lep = st.number_input("DER_deltar_tau_lep: ", value=0, format="%d")
    DER_met_phi_centrality = st.number_input("DER_met_phi_centrality:", value=0, format="%d")
    DER_pt_h = st.number_input("DER_pt_h:", value=0, format="%d")
    PRI_met = st.number_input("PRI_met:", value=0, format="%d")
    submit_val = st.form_submit_button("Classify")


if submit_val:
    per_d = dict(zip(feature_cols[0:11],np.zeros(30)))
    for p in permission:
        per_d[p] = 1
    permission = np.array(list(per_d.values()))
    cat = dict(zip(feature_cols[0:], np.zeros(15)))
    cat[Category] = 1
    Category = np.array(list(cat.values()))

    base_feats = np.array([DER_mass_MMC, DER_mass_transverse_met_lep, DER_mass_vis, DER_deltar_tau_lep, DER_met_phi_centrality, DER_pt_h, PRI_met])

    attributes = np.concatenate([base_feats, permission, Category])
    
    print("attributes value")

    status = predict(attributes.reshape(1, -1))

    if status:
        st.error("The App is Signal")
    else:
        st.success("The App is Background")
        st.balloons()
