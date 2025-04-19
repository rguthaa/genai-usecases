#!/bin/bash

# Define paths
SERVICE_ACCOUNT_EMAIL="vertext-ai-auth@${PROJECT_ID}.iam.gserviceaccount.com"
KEY_OUTPUT_PATH="$HOME/keys/vertex-ai-auth.json"

echo "Starting setup..."

# Step 2: Install the required packages
pip3 install -r "requirements.txt"

# Step 3: Check if gcloud CLI is installed
if ! command -v gcloud &>/dev/null; then
    echo "gcloud CLI is not installed."
    echo "For macOS, install gcloud CLI using the following instructions:"
    echo "  https://cloud.google.com/sdk/docs/install-sdk"
    exit 1
fi

# Step 4: Authenticate gcloud (only if not already authenticated)
if gcloud auth application-default print-access-token &>/dev/null; then
    echo "Already logged into gcloud. Skipping authentication step."
else
    echo "You are not logged into gcloud. Please authenticate."
    gcloud auth application-default login
fi

# === Read PROJECT_ID from ADC file ===
ADC_JSON_PATH="${GOOGLE_APPLICATION_CREDENTIALS:-$HOME/.config/gcloud/application_default_credentials.json}"

if [ ! -f "$ADC_JSON_PATH" ]; then
    echo "Application credentials file not found at $ADC_JSON_PATH"
    exit 1
fi

PROJECT_ID=$(jq -r '.quota_project_id' "$ADC_JSON_PATH")

if [ -z "$PROJECT_ID" ] || [ "$PROJECT_ID" == "null" ]; then
    echo "quota_project_id not found in credentials file: $ADC_JSON_PATH"
    exit 1
fi

# Step 5: Download service account key if needed
if [ -f "$KEY_OUTPUT_PATH" ]; then
    echo "Service account key already exists at $KEY_OUTPUT_PATH. Skipping download."
else
    echo "Creating key for service account: $SERVICE_ACCOUNT_EMAIL"
    gcloud iam service-accounts keys create "$KEY_OUTPUT_PATH" \
      --iam-account="$SERVICE_ACCOUNT_EMAIL" \
      --project="$PROJECT_ID"

    if [ $? -ne 0 ]; then
        echo "Failed to create service account key. Exiting."
        exit 1
    fi
    echo "Key downloaded successfully."
fi

# Set GOOGLE_APPLICATION_CREDENTIALS if not already exported
if [ -z "$GOOGLE_APPLICATION_CREDENTIALS" ]; then
    export GOOGLE_APPLICATION_CREDENTIALS="$KEY_OUTPUT_PATH"
    echo "Exported GOOGLE_APPLICATION_CREDENTIALS"
else
    echo "GOOGLE_APPLICATION_CREDENTIALS already set: $GOOGLE_APPLICATION_CREDENTIALS"
fi

echo "Setup complete."
