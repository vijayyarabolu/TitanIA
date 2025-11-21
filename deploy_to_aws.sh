#!/bin/bash

# Configuration
REGION="us-east-1"
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
BACKEND_REPO="titania-backend"
FRONTEND_REPO="titania-frontend"

echo "🚀 Starting TitanIA AWS Deployment..."
echo "Region: $REGION"
echo "Account ID: $ACCOUNT_ID"

# 1. Login to ECR
echo "🔑 Logging into ECR..."
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com

# 2. Create Repositories (if they don't exist)
echo "📦 Checking ECR repositories..."
aws ecr describe-repositories --repository-names $BACKEND_REPO || aws ecr create-repository --repository-name $BACKEND_REPO
aws ecr describe-repositories --repository-names $FRONTEND_REPO || aws ecr create-repository --repository-name $FRONTEND_REPO

# 3. Build and Push Backend
echo "🔨 Building Backend..."
docker build -t $BACKEND_REPO ./backend
echo "⬆️ Pushing Backend..."
docker tag $BACKEND_REPO:latest $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$BACKEND_REPO:latest
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$BACKEND_REPO:latest

# 4. Build and Push Frontend
echo "🔨 Building Frontend..."
docker build -t $FRONTEND_REPO ./frontend
echo "⬆️ Pushing Frontend..."
docker tag $FRONTEND_REPO:latest $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$FRONTEND_REPO:latest
docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$FRONTEND_REPO:latest

echo "✅ Build and Push Complete!"
echo "Now go to AWS App Runner (https://console.aws.amazon.com/apprunner) and deploy these images:"
echo "1. Backend Image: $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$BACKEND_REPO:latest"
echo "2. Frontend Image: $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$FRONTEND_REPO:latest"
