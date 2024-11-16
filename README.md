# Credit Card Fraud Detection

This application predicts whether a credit card transaction is fraudulent or legitimate based on 
features derived from anonymized data. The model has been trained on the Credit Card Fraud Detection 
dataset, which includes features like time, amount, and anonymized features V1-V28.

Information about the features:
1. Time: The seconds elapsed between this transaction and the first transaction in the dataset.
2. Amount: The transaction amount in USD.
3. V1 to V28: Anonymized features derived from the original transaction data using principal
   component analysis (PCA) to protect sensitive information. These features capture patterns
   and relationships indicative of fraudulent or legitimate behavior.

The project has been deployed at: [Streamlit app](https://credit-card-frauddetection.streamlit.app/)
