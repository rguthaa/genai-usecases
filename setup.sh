#!/bin/bash
echo "Starting setup..."

# === INPUT VALIDATION ===
if [ -z "$1" ]; then
  echo "❌ Usage: $0 <Model - OpenAI, VertexAI etc..>"
  exit 1
fi

MODEL="$1"

if ["$MODEL" == "VertexAI"]; then
    source vertex_ai_setup.sh
fi

# Step 2: Install the required packages
pip3 install -r "requirements.txt"

echo "✅ Setup complete."
