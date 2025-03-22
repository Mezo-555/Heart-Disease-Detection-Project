import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

numerical_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
categorical_cols = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

# Load Dataset
def load_dataset(filepath):
    return pd.read_csv(filepath)

# Handle Missing Values
def handle_missing_values(df):
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].median())  # Fill numerical columns with median
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])  # Fill categorical columns with mode
    return df

# Normalize Numerical Features & Save Scaler
def normalize_features(df, numerical_cols, scaler_path):
    scaler = MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    joblib.dump(scaler, scaler_path)  # Save scaler for later use
    print(f"✅ Scaler saved to {scaler_path}")
    return df

# Encode Categorical Variables
def encode_categorical(df, categorical_cols):
    encoder = OneHotEncoder(sparse_output=False)
    encoded = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))
    df = df.drop(columns=categorical_cols).reset_index(drop=True)
    df = pd.concat([df, encoded_df], axis=1)
    return df

# Feature Selection using Correlation & Mutual Information
def select_features(df, target_column, threshold=0.09):
    correlation_matrix = df.corr()
    high_corr_features = correlation_matrix[target_column].abs() > threshold
    selected_features = correlation_matrix[target_column][high_corr_features].index.tolist()
    return df[selected_features]

# Main Function
def process_data(input_path, output_path, scaler_path):
    df = load_dataset(input_path)
    df = handle_missing_values(df)
    numerical_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    categorical_cols = ['cp', 'restecg', 'slope', 'ca', 'thal']
    df = normalize_features(df, numerical_cols, scaler_path)  # Now saves the scaler
    df = encode_categorical(df, categorical_cols)
    df = select_features(df, 'target')  # Selecting most relevant features
    df.to_csv(output_path, index=False)
    print(f'Processed data saved to {output_path}')

# Run processing if executed as a script
if __name__ == "__main__":
    process_data('data/heart.csv', 'data/cleaned_data.csv', 'utils/scaler.pkl')
