# TitanIA AWS Deployment Guide

This guide explains how to deploy the TitanIA platform to AWS using **Amazon ECR (Elastic Container Registry)** and **AWS App Runner** (for the simplest deployment) or **Amazon ECS (Elastic Container Service)**.

## Prerequisites

1.  **AWS CLI Installed**: Ensure you have the AWS CLI installed.
    ```bash
    aws --version
    ```
2.  **AWS Credentials Configured**: Run `aws configure` and enter your Access Key, Secret Key, Region (e.g., `us-east-1`), and Output format (`json`).
3.  **Docker Installed**: Ensure Docker is running on your machine.

## 💰 Cost & Free Tier Warning

| Service | Free Tier Eligible? | Notes |
| :--- | :--- | :--- |
| **EC2 (t2.micro)** | ✅ **YES** | 750 hours/month (12 months). Good for running local models. |
| **S3** | ✅ **YES** | 5GB storage. Good for frontend hosting & docs. |
| **CloudFront** | ✅ **YES** | 1TB transfer. Good for frontend delivery. |
| **Amazon Bedrock** | ❌ **NO** | **Paid per token**. Uses advanced models (Claude 3). |
| **App Runner** | ❌ **NO** | Paid per vCPU/hour. |

**Recommendation:**
- For **100% Free Tier**: Use **Option 1 (EC2)** and keep `USE_BEDROCK=false` (uses local HuggingFace models).
- For **Performance**: Use **Option 2 (Bedrock)**, but be aware of small usage costs.

## Deployment Script

We have provided a script `deploy_to_aws.sh` to automate the process.

### 1. Make the script executable
```bash
chmod +x deploy_to_aws.sh
```

### 2. Run the script
```bash
./deploy_to_aws.sh
```

## Manual Deployment Steps (If you prefer)

### 1. Create ECR Repositories
```bash
aws ecr create-repository --repository-name titania-backend
aws ecr create-repository --repository-name titania-frontend
```

### 2. Login to ECR
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <YOUR_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

### 3. Build and Push Backend
```bash
docker build -t titania-backend ./backend
docker tag titania-backend:latest <YOUR_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/titania-backend:latest
docker push <YOUR_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/titania-backend:latest
```

### 4. Build and Push Frontend
```bash
docker build -t titania-frontend ./frontend
docker tag titania-frontend:latest <YOUR_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/titania-frontend:latest
docker push <YOUR_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/titania-frontend:latest
```

### 3. Access the App
Once the instance is running, go to `http://<EC2-PUBLIC-IP>`.

## 🌟 Recommended Free Tier Configuration (Versatile)

To get the best of both worlds (**Free Cost** + **Cloud Versatility**), use this hybrid setup:

1.  **Compute**: **EC2 (t2.micro)** running the Backend & AI (Local Models).
    - *Cost*: Free (750 hrs/mo).
    - *Config*: `USE_BEDROCK=false`.
2.  **Storage**: **S3** for storing uploaded documents.
    - *Cost*: Free (5GB).
    - *Config*: `USE_REAL_S3=true`.
3.  **Frontend**: **S3 + CloudFront** for global fast delivery.
    - *Cost*: Free (1TB transfer).

### How to configure this on EC2:
Create a `.env` file in your EC2 `app` folder:
```bash
USE_REAL_S3=true
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
S3_BUCKET_NAME=your_bucket
USE_BEDROCK=false
```
Then run `docker-compose up`. from ECR.
    - Port: 8000.
    - Environment Variables: Add `CHROMA_DB_DIR=/tmp/chroma` (App Runner is ephemeral, so data won't persist long-term without EFS).
- Create a service for **Frontend**:
    - Source: Container Registry.
    - Image: Select `titania-frontend` from ECR.

### 5. Deploy to AWS App Runner
- Go to the AWS Console -> App Runner.
- Create a service for **Backend**:
    - Source: Container Registry.
    - Image: Select `titania-backend` from ECR.
    - Port: 8000.
    - Environment Variables: Add `CHROMA_DB_DIR=/tmp/chroma` (App Runner is ephemeral, so data won't persist long-term without EFS).
- Create a service for **Frontend**:
    - Source: Container Registry.
    - Image: Select `titania-frontend` from ECR.
    - Port: 80.

## Important Notes
- **Data Persistence**: The current setup uses a local ChromaDB inside the container. On AWS App Runner or Fargate, this data will be lost when the container restarts. For production, you should mount an **EFS (Elastic File System)** volume to the backend container.
- **CORS**: Once deployed, update the `allow_origins` in `backend/app/main.py` to include your new Frontend URL (e.g., `https://<your-app-runner-id>.awsapprunner.com`).
