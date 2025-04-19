#!/bin/bash

echo "Starting OpenAI setup..."

# Step 1: Validate that OPENAI_API_KEY is set
if [ -z "$OPENAI_API_KEY" ]; then
  echo "ERROR: OPENAI_API_KEY is not set. Please add it to your .env file before running this script."
  exit 1
fi

# Step 2: Update or append to .env (preserve existing contents)
if grep -q "^OPENAI_API_KEY=" .env 2>/dev/null; then
  # Replace existing line
  sed -i.bak "/^OPENAI_API_KEY=/c\\
OPENAI_API_KEY=$OPENAI_API_KEY
" .env
  echo "Updated OPENAI_API_KEY in .env"
else
  echo "OPENAI_API_KEY=$OPENAI_API_KEY" >> .env
  echo "Added OPENAI_API_KEY to .env"
fi

echo "OpenAI setup complete."
