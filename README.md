
#### **Higgs Boson**

#### **Problem Statement**

- The task is to classify whether **signal or background**

|Variable          |Description         |
|------------------|--------------------|
|EventId           |An unique integer identifier of the event|
|DER_mass_MMC      |The estimated mass mH of the Higgs boson candidate, obtained through a probabilistic phase space integration.|
|DER_mass_transverse_met_lep |The transverse mass between the missing transverse energy and the lepton|
|DER_mass_vis      |The invariant mass of the hadronic tau and the lepton.|
|DER_pt_h          |The modulus of the vector sum of the transverse momentum of the hadronic tau, the lepton and the missing transverse energy vector.|
|DER_deltaeta_jet_jet|The absolute value of the pseudorapidity separation between the two jets (undefined if PRI_jet_num ≤ 1).|
|DER_mass_jet_jet |The invariant mass of the two jets (undefined if PRI_jet_num ≤ 1).|
|DER_prodeta_jet_jet	|The product of the pseudorapidities of the two jets (undefined if PRI_jet_num ≤ 1).|
|DER_deltar_tau_lep	|The R separation between the hadronic tau and the lepton.
|DER_pt_tot	|The modulus of the vector sum of the missing transverse momenta and the transverse momenta of the hadronic tau, the lepton, the leading jet (if PRI_jet_num ≥) and the subleading jet (if PRI jet num = 2) (but not of any additional jets).|
|DER_sum_pt	|The sum of the moduli of the transverse momenta of the hadronic tau, the lepton, the leading jet (if PRI jet num ≥ 1) and the subleading jet (if PRI jet num = 2) and the other jets (if PRI jet num = 3).|
|DER_pt_ratio_lep_tau	|The ratio of the transverse momenta of the lepton and the hadronic tau.|
|DER_met_phi_centrality	|The centrality of the azimuthal angle of the missing transverse energy vector w.r.t. the hadronic tau and the lepton.|
|DER_lep_eta_centrality	|The centrality of the pseudorapidity of the lepton w.r.t. the two jets (undefined if PRI_jet_num ≤ 1).|
|PRI_tau_pt	|The transverse momentum p2x+p2y−−−−−−√ of the hadronic tau.|
|PRI_tau_eta	|The pseudorapidity η of the hadronic tau.|
|PRI_tau_phi	|The azimuth angle ϕ of the hadronic tau.|
|PRI_lep_pt	|The transverse momentum p2x+p2y−−−−−−√ of the lepton (electron or muon).|
|PRI_lep_eta	|The pseudorapidity η of the lepton.|
|PRI_lep_phi	|The azimuth angle ϕ of the lepton.|
|PRI_met	|The missing transverse energy E→missT|
|PRI_met_phi	|The azimuth angle ϕ of the mssing transverse energy|
|PRI_met_sumet	|The total transverse energy in the detector.|
|PRI_jet_num	|The number of jets (integer with value of 0, 1, 2 or 3; possible larger values have been capped at 3).|
|PRI_jet_leading_pt	|The transverse momentum p2x+p2y−−−−−−√ of the leading jet, that is the jet with largest transverse momentum (undefined if PRI_jet_num = 0).|
|PRI_jet_leading_eta	|The pseudorapidity η of the leading jet (undefined if PRI jet num = 0).|
|PRI_jet_leading_phi	|The azimuth angle ϕ of the leading jet (undefined if PRI jet num = 0).|
|PRI_jet_subleading_pt	|The transverse momentum p2x+p2y−−−−−−√ of the leading jet, that is, the jet with second largest transverse momentum (undefined if PRI_jet_num ≤ 1).|
|PRI_jet_subleading_eta	|The pseudorapidity η of the subleading jet (undefined if PRI_jet_num ≤ 1).|
|PRI_jet_subleading_phi	|The azimuth angle ϕ of the subleading jet (undefined if PRI_jet_num ≤ 1).|
|PRI_jet_all_pt	|The scalar sum of the transverse momentum of all the jets of the events.|
|Weight	|The event weight wi|
|Label	|The event label (string) yi ∈ {s,b} (**s** for **signal**, **b** for **background**).
|KaggleSet	|String specifying to which Kaggle set the event belongs : ”t”:training, ”b”:public leaderboard, ”v”:private leaderboard,”u”:unused.|
|KaggleWeight	|Weight normalised within each Kaggle dataset.|



#### **Deployment Link**



