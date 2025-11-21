#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./update_api_url.sh <NEW_API_URL>"
  echo "Example: ./update_api_url.sh http://54.123.45.67:8000"
  exit 1
fi

NEW_URL=$1
echo "Updating Frontend to use API: $NEW_URL"

# MacOS sed requires an empty string for in-place editing
sed -i '' "s|http://localhost:8000|$NEW_URL|g" frontend/src/components/AgentInterface.jsx
sed -i '' "s|http://localhost:8000|$NEW_URL|g" frontend/src/components/UploadSection.jsx

echo "✅ Updated! Now run: cd frontend && npm run build && cd .. && aws s3 sync frontend/dist s3://titania-frontend-v1"
