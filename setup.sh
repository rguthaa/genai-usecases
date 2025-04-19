#!/bin/bash
echo "Starting setup..."

# === INPUT VALIDATION ===
if [ -z "$1" ]; then
  echo "Usage: $0 <Model - OpenAI, VertexAI etc..>"
  exit 1
fi

MODEL="$1"

# Auto-copy .env from .env.example if not present
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "Created .env file from .env.example"
    else
        echo "Missing .env and .env.example. Cannot continue."
        exit 1
    fi
fi

# Load environment variables
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
    echo "Loaded environment variables from .env"
fi

if [ "$MODEL" == "VertexAI" ]; then
    source vertex_ai_setup.sh
elif [ "$MODEL" == "OpenAI" ]; then
    source openai_setup.sh
else
    echo "Unsupported model: $MODEL"
    exit 1
fi

# Step 2: Install the required packages
pip3 install -r "requirements.txt"

echo "Setup complete."
