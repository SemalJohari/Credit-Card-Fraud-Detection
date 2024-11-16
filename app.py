import streamlit as st
import pickle as pk
import numpy as np

model = pk.load(open('model.pkl', 'rb'))

introduction = """
### Credit Card Fraud Detection App:

This application predicts whether a credit card transaction is **fraudulent** or **legitimate** 
based on features derived from anonymized data. The model has been trained on the 
Credit Card Fraud Detection dataset, which includes features like time, amount, and anonymized
features V1-V28.

You can input the transaction details below:
"""

def display_instruction_window():
    with st.expander("💡 Information about the features", expanded=False):
        st.markdown("""
            ### Terminologies:
            1. Time: The seconds elapsed between this transaction and the first transaction in the dataset.
            2. Amount: The transaction amount in USD.
            3. V1 to V28: Anonymized features derived from the original transaction data using principal
                    component analysis (PCA) to protect sensitive information. These features capture 
                    patterns and relationships indicative of fraudulent or legitimate behavior.
            """)

def page():
    st.title("Credit Card Fraud Detection") 
    st.markdown(introduction)

    with st.sidebar:
        st.title("More Information")
        display_instruction_window()

page()

st.write("#### Transaction Details")

col1, col2 = st.columns(2)
time = col1.number_input('Time (seconds since first transaction)', min_value=0)
amount = col2.number_input('Transaction Amount ($)', min_value=0.0)

v_features = []
num_features = 28  
rows, cols = 7, 4

for r in range(rows):
    grid_cols = st.columns(cols)
    for c in range(cols):
        feature_index = r * cols + c + 1
        if feature_index <= num_features:  
            v_features.append(
                grid_cols[c].number_input(f'V{feature_index}', format="%.4f", step=0.01)
            )

if st.button('Predict'):

    features = [time] + v_features + [amount]
    features = np.array(features).reshape(1, -1)

    result = model.predict(features)
    
    if result[0] == 1:
        st.write("## Fraudulent Transaction Detected")
    else:
        st.write("## Legitimate Transaction")

    prob = model.predict_proba(features)
    st.write(f"#### Fraud Probability: {prob[0][1]:.3%}")
    st.write(f"#### Legitimate Probability: {prob[0][0]:.4%}")

